#!/usr/bin/env python3
"""
Spawn a vehicle in CARLA, mount a LiDAR on its roof, and enable autopilot.

Usage:
    1. Start the CARLA server (e.g. ./CarlaUE4.sh)
    2. python carla_lidar_autopilot.py
Press Ctrl+C to stop; all actors are cleaned up automatically.
"""

import random
import time

import carla


def lidar_callback(point_cloud):
    """Called every time the LiDAR produces a new scan."""
    print(f"[LiDAR] frame={point_cloud.frame} points={len(point_cloud)}")
    # To save scans to disk (PLY format), uncomment:
    # point_cloud.save_to_disk(f"_out/{point_cloud.frame:06d}.ply")


def main():
    actors = []

    try:
        # --- Connect to the simulator ---
        client = carla.Client("localhost", 2000)
        client.set_timeout(10.0)
        world = client.get_world()
        blueprint_library = world.get_blueprint_library()

        # --- Spawn the vehicle ---
        vehicle_bp = blueprint_library.find("vehicle.tesla.model3")
        spawn_points = world.get_map().get_spawn_points()
        spawn_point = random.choice(spawn_points)

        vehicle = world.spawn_actor(vehicle_bp, spawn_point)
        actors.append(vehicle)
        print(f"Spawned vehicle: {vehicle.type_id} (id={vehicle.id})")

        # --- Configure and attach the LiDAR on the roof ---
        lidar_bp = blueprint_library.find("sensor.lidar.ray_cast")
        lidar_bp.set_attribute("channels", "32")
        lidar_bp.set_attribute("range", "50")
        lidar_bp.set_attribute("points_per_second", "300000")
        lidar_bp.set_attribute("rotation_frequency", "20")
        lidar_bp.set_attribute("upper_fov", "10")
        lidar_bp.set_attribute("lower_fov", "-30")

        # Position relative to the vehicle: centered, ~2.2 m up (above the roof)
        lidar_transform = carla.Transform(carla.Location(x=0.0, y=0.0, z=2.2))

        lidar = world.spawn_actor(lidar_bp, lidar_transform, attach_to=vehicle)
        actors.append(lidar)
        lidar.listen(lidar_callback)
        print("LiDAR attached to the roof.")

        # --- Enable autopilot via the Traffic Manager ---
        traffic_manager = client.get_trafficmanager(8000)
        vehicle.set_autopilot(True, traffic_manager.get_port())

        # Optional tuning:
        # traffic_manager.global_percentage_speed_difference(20.0)  # 20% slower than limit
        # traffic_manager.ignore_lights_percentage(vehicle, 0)

        print("Autopilot enabled. Press Ctrl+C to stop.")

        # --- Keep the spectator camera following the vehicle ---
        spectator = world.get_spectator()
        while True:
            v_tf = vehicle.get_transform()
            spectator.set_transform(
                carla.Transform(
                    v_tf.location
                    + carla.Location(z=30)
                    - 10 * v_tf.get_forward_vector(),
                    carla.Rotation(pitch=-60, yaw=v_tf.rotation.yaw),
                )
            )
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nStopping...")

    finally:
        # --- Cleanup ---
        for actor in reversed(actors):
            if actor.type_id.startswith("sensor."):
                actor.stop()
            actor.destroy()
        print("All actors destroyed.")


if __name__ == "__main__":
    main()