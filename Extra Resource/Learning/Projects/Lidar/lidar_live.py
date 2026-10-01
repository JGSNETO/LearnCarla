#!/usr/bin/env python3
"""
CARLA: ego vehicle with roof LiDAR on autopilot, NPC traffic and pedestrians,
and a real-time point cloud viewer in a separate Open3D window.

Requirements:
    pip install carla numpy open3d

Usage:
    1. Start the CARLA server (e.g. ./CarlaUE4.sh)
    2. python carla_lidar_live.py [--vehicles 30] [--walkers 20]
Close the Open3D window or press Ctrl+C to stop; everything is cleaned up.
"""

import argparse
import random
import threading
import time

import carla
import numpy as np
import open3d as o3d


# ---------------------------------------------------------------------------
# LiDAR -> Open3D bridge
# ---------------------------------------------------------------------------
class LidarBuffer:
    """Thread-safe holder for the most recent LiDAR scan."""

    def __init__(self):
        self._lock = threading.Lock()
        self._points = None
        self._colors = None
        self._new = False

    def callback(self, point_cloud):
        # Raw data is float32 [x, y, z, intensity] per point
        data = np.frombuffer(point_cloud.raw_data, dtype=np.float32).reshape(-1, 4)
        points = data[:, :3].copy()
        intensity = data[:, 3]

        # CARLA is left-handed; flip Y so the view matches the simulator
        points[:, 1] = -points[:, 1]

        colors = intensity_to_color(intensity)

        with self._lock:
            self._points, self._colors, self._new = points, colors, True

    def get(self):
        """Return (points, colors) if a new scan arrived, otherwise None."""
        with self._lock:
            if not self._new:
                return None
            self._new = False
            return self._points, self._colors


def intensity_to_color(intensity):
    """Map LiDAR intensity [0..1] to a dark-blue -> cyan -> yellow gradient."""
    t = np.clip(intensity, 0.0, 1.0)
    stops = np.array([0.0, 0.5, 1.0])
    palette = np.array([[0.1, 0.1, 0.6], [0.0, 0.9, 0.9], [1.0, 0.9, 0.0]])
    return np.stack([np.interp(t, stops, palette[:, c]) for c in range(3)], axis=1)


def create_viewer():
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="CARLA LiDAR (live)", width=1100, height=700)

    opt = vis.get_render_option()
    opt.background_color = np.array([0.02, 0.02, 0.05])
    opt.point_size = 2.0

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.zeros((1, 3)))  # placeholder
    vis.add_geometry(pcd)
    vis.add_geometry(o3d.geometry.TriangleMesh.create_coordinate_frame(size=2.0))

    # Fixed camera behind and above the sensor (points are sensor-relative)
    ctr = vis.get_view_control()
    ctr.set_lookat([0, 0, 0])
    ctr.set_front([-1.0, 0.0, 0.6])
    ctr.set_up([0, 0, 1])
    ctr.set_zoom(0.2)
    return vis, pcd


# ---------------------------------------------------------------------------
# Scene population
# ---------------------------------------------------------------------------
def spawn_npc_vehicles(world, client, tm, count, spawn_points):
    bp_lib = world.get_blueprint_library()
    vehicle_bps = [
        bp for bp in bp_lib.filter("vehicle.*")
        if bp.get_attribute("number_of_wheels").as_int() == 4
    ]

    vehicles = []
    for sp in spawn_points[:count]:
        bp = random.choice(vehicle_bps)
        if bp.has_attribute("color"):
            bp.set_attribute("color", random.choice(bp.get_attribute("color").recommended_values))
        bp.set_attribute("role_name", "npc")
        vehicle = world.try_spawn_actor(bp, sp)
        if vehicle is not None:
            vehicle.set_autopilot(True, tm.get_port())
            vehicles.append(vehicle)
    print(f"Spawned {len(vehicles)} NPC vehicles.")
    return vehicles


def spawn_walkers(world, count):
    bp_lib = world.get_blueprint_library()
    walker_bps = bp_lib.filter("walker.pedestrian.*")
    controller_bp = bp_lib.find("controller.ai.walker")

    walkers, controllers = [], []
    for _ in range(count):
        loc = world.get_random_location_from_navigation()
        if loc is None:
            continue
        bp = random.choice(walker_bps)
        if bp.has_attribute("is_invincible"):
            bp.set_attribute("is_invincible", "false")

        walker = world.try_spawn_actor(bp, carla.Transform(loc))
        if walker is None:
            continue
        controller = world.spawn_actor(controller_bp, carla.Transform(), attach_to=walker)

        controller.start()
        controller.go_to_location(world.get_random_location_from_navigation())
        controller.set_max_speed(1.0 + random.random())  # 1-2 m/s

        walkers.append(walker)
        controllers.append(controller)
    print(f"Spawned {len(walkers)} pedestrians.")
    return walkers, controllers


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=2000)
    parser.add_argument("--vehicles", type=int, default=30, help="number of NPC vehicles")
    parser.add_argument("--walkers", type=int, default=20, help="number of pedestrians")
    args = parser.parse_args()

    ego = lidar = None
    npc_vehicles, walkers, controllers = [], [], []
    vis = None

    try:
        client = carla.Client(args.host, args.port)
        client.set_timeout(15.0)
        world = client.get_world()
        bp_lib = world.get_blueprint_library()

        tm = client.get_trafficmanager(8000)
        tm.set_global_distance_to_leading_vehicle(2.5)

        # --- Ego vehicle ---
        spawn_points = world.get_map().get_spawn_points()
        random.shuffle(spawn_points)
        ego_bp = bp_lib.find("vehicle.tesla.model3")
        ego_bp.set_attribute("role_name", "hero")
        ego = world.spawn_actor(ego_bp, spawn_points.pop())
        ego.set_autopilot(True, tm.get_port())
        print(f"Ego vehicle spawned (id={ego.id}), autopilot on.")

        # --- Roof LiDAR ---
        lidar_bp = bp_lib.find("sensor.lidar.ray_cast")
        lidar_bp.set_attribute("channels", "32")
        lidar_bp.set_attribute("range", "50")
        lidar_bp.set_attribute("points_per_second", "300000")
        lidar_bp.set_attribute("rotation_frequency", "20")
        lidar_bp.set_attribute("upper_fov", "10")
        lidar_bp.set_attribute("lower_fov", "-30")

        lidar = world.spawn_actor(
            lidar_bp,
            carla.Transform(carla.Location(x=0.0, y=0.0, z=2.2)),
            attach_to=ego,
        )
        buffer = LidarBuffer()
        lidar.listen(buffer.callback)
        print("LiDAR attached to the roof.")

        # --- Other actors ---
        npc_vehicles = spawn_npc_vehicles(world, client, tm, args.vehicles, spawn_points)
        walkers, controllers = spawn_walkers(world, args.walkers)

        # --- Live viewer + main loop ---
        vis, pcd = create_viewer()
        spectator = world.get_spectator()
        print("Running. Close the Open3D window or press Ctrl+C to stop.")

        while True:
            scan = buffer.get()
            if scan is not None:
                points, colors = scan
                pcd.points = o3d.utility.Vector3dVector(points)
                pcd.colors = o3d.utility.Vector3dVector(colors)
                vis.update_geometry(pcd)

            if not vis.poll_events():  # window closed
                break
            vis.update_renderer()

            # Keep the simulator's spectator camera behind the ego vehicle
            tf = ego.get_transform()
            spectator.set_transform(
                carla.Transform(
                    tf.location + carla.Location(z=25) - 10 * tf.get_forward_vector(),
                    carla.Rotation(pitch=-60, yaw=tf.rotation.yaw),
                )
            )
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nStopping...")

    finally:
        print("Cleaning up...")
        if vis is not None:
            vis.destroy_window()
        if lidar is not None:
            lidar.stop()
            lidar.destroy()
        for c in controllers:
            c.stop()
            c.destroy()
        for w in walkers:
            w.destroy()
        for v in npc_vehicles:
            v.destroy()
        if ego is not None:
            ego.destroy()
        print("Done.")


if __name__ == "__main__":
    main()