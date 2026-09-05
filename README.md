# 🚗 LearnCARLA

A hands-on learning repository for **CARLA Simulator**, focused on learning autonomous driving, ADAS, computer vision, sensors, vehicle control, and simulation-based development with Python.

The goal of this repository is to progressively learn how to use CARLA — starting from the basics and eventually building autonomous-driving applications.

---

## 🎯 Objectives

This repository aims to build practical knowledge of:

* CARLA Simulator
* Python API
* Vehicle and pedestrian simulation
* CARLA maps and environments
* Sensors and sensor data
* RGB cameras
* Semantic segmentation
* Instance segmentation
* Depth cameras
* LiDAR
* Radar
* GNSS and IMU
* Vehicle control
* Traffic Manager
* Autonomous driving
* Computer vision
* Object detection
* ADAS algorithms
* CARLA + ROS 2
* Simulation-based testing

---

## ## 📂 Repository Structure

The repository is organized as a progressive learning path, starting with the CARLA fundamentals and gradually moving toward perception, ADAS, sensor fusion, autonomous driving, ROS 2, and simulation-based testing.

```text
LearnCARLA/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── 01_basics/
│   ├── 01_connect_to_carla.py
│   ├── 02_get_world.py
│   ├── 03_get_maps.py
│   ├── 04_load_map.py
│   └── README.md
│
├── 02_worlds/
│   ├── 01_load_town.py
│   ├── 02_weather.py
│   ├── 03_time_of_day.py
│   └── README.md
│
├── 03_actors/
│   ├── vehicles/
│   │   ├── list_vehicles.py
│   │   ├── spawn_vehicle.py
│   │   ├── spawn_multiple_vehicles.py
│   │   └── destroy_vehicles.py
│   │
│   ├── pedestrians/
│   │   ├── spawn_pedestrian.py
│   │   └── spawn_pedestrians.py
│   │
│   └── README.md
│
├── 04_traffic/
│   ├── 01_autopilot.py
│   ├── 02_traffic_manager.py
│   ├── 03_generate_traffic.py
│   └── README.md
│
├── 05_sensors/
│   ├── rgb_camera/
│   │   ├── rgb_camera.py
│   │   └── live_view.py
│   │
│   ├── semantic_segmentation/
│   │   ├── semantic_camera.py
│   │   └── live_view.py
│   │
│   ├── instance_segmentation/
│   │   └── instance_camera.py
│   │
│   ├── depth/
│   │   └── depth_camera.py
│   │
│   ├── lidar/
│   │   └── lidar.py
│   │
│   ├── radar/
│   │   └── radar.py
│   │
│   ├── gnss/
│   │   └── gnss.py
│   │
│   └── imu/
│       └── imu.py
│
├── 06_computer_vision/
│   ├── 01_opencv/
│   ├── 02_image_processing/
│   ├── 03_object_detection/
│   ├── 04_lane_detection/
│   └── 05_traffic_light_detection/
│
├── 07_yolo/
│   ├── 01_yolo_basics/
│   ├── 02_vehicle_detection/
│   ├── 03_pedestrian_detection/
│   └── 04_carla_yolo/
│
├── 08_vehicle_control/
│   ├── 01_manual_control.py
│   ├── 02_vehicle_control.py
│   ├── 03_steering.py
│   ├── 04_throttle_brake.py
│   └── pid/
│       ├── pid_controller.py
│       └── vehicle_pid.py
│
├── 09_adas/
│   ├── aeb/
│   │   ├── README.md
│   │   ├── aeb.py
│   │   └── scenario.py
│   │
│   ├── acc/
│   │   ├── README.md
│   │   ├── acc.py
│   │   └── scenario.py
│   │
│   ├── lane_assist/
│   │   ├── README.md
│   │   └── lane_assist.py
│   │
│   ├── traffic_light_assist/
│   │   └── traffic_light_assist.py
│   │
│   └── pedestrian_detection/
│       └── pedestrian_detection.py
│
├── 10_sensor_fusion/
│   ├── camera_lidar/
│   ├── camera_radar/
│   ├── lidar_radar/
│   └── multi_sensor_fusion/
│
├── 11_localization/
│   ├── gnss/
│   ├── imu/
│   ├── odometry/
│   └── localization.py
│
├── 12_planning/
│   ├── waypoint_planning/
│   ├── path_planning/
│   └── behavior_planning/
│
├── 13_autonomous_driving/
│   ├── perception/
│   ├── localization/
│   ├── planning/
│   ├── control/
│   └── autonomous_vehicle.py
│
├── 14_ros2/
│   ├── carla_ros_bridge/
│   ├── sensors/
│   ├── perception/
│   ├── vehicle_control/
│   └── autonomous_driving/
│
├── 15_scenarios/
│   ├── pedestrian_crossing/
│   ├── emergency_braking/
│   ├── cut_in/
│   ├── lane_change/
│   └── traffic_light/
│
├── 16_testing/
│   ├── scenario_testing/
│   ├── sensor_testing/
│   ├── perception_testing/
│   └── adas_testing/
│
├── common/
│   ├── carla_connection.py
│   ├── vehicle_utils.py
│   ├── sensor_utils.py
│   └── visualization.py
│
└── docs/
    ├── carla_architecture.md
    ├── coordinate_systems.md
    ├── sensors.md
    └── useful_commands.md
```

### 🧭 Learning Progression

The folder structure follows the development of an autonomous vehicle:

```text
CARLA Basics
     │
     ▼
Worlds & Actors
     │
     ▼
Traffic
     │
     ▼
Sensors
     │
     ▼
Computer Vision
     │
     ▼
Object Detection
     │
     ▼
Vehicle Control
     │
     ▼
ADAS
     │
     ▼
Sensor Fusion
     │
     ▼
Localization
     │
     ▼
Planning
     │
     ▼
Autonomous Driving
     │
     ▼
ROS 2 Integration
     │
     ▼
Scenario Testing
```

### 📁 Directory Overview

| Directory                | Purpose                                             |
| ------------------------ | --------------------------------------------------- |
| `01_basics/`             | CARLA fundamentals and Python API                   |
| `02_worlds/`             | Maps, weather, and simulation modes                 |
| `03_actors/`             | Vehicles, pedestrians, blueprints, and actors       |
| `04_traffic/`            | Traffic Manager, autopilot, and traffic generation  |
| `05_sensors/`            | CARLA sensors and sensor data                       |
| `06_computer_vision/`    | OpenCV and image-processing fundamentals            |
| `07_yolo/`               | YOLO-based object detection                         |
| `08_vehicle_control/`    | Vehicle control and PID controllers                 |
| `09_adas/`               | AEB, ACC, lane assistance, and other ADAS functions |
| `10_sensor_fusion/`      | Multi-sensor perception and object association      |
| `11_localization/`       | GNSS, IMU, odometry, and localization               |
| `12_planning/`           | Waypoint, path, and behavior planning               |
| `13_autonomous_driving/` | Complete autonomous-driving pipeline                |
| `14_ros2/`               | CARLA and ROS 2 integration                         |
| `15_scenarios/`          | Reusable autonomous-driving scenarios               |
| `16_testing/`            | Scenario, sensor, perception, and ADAS testing      |
| `common/`                | Reusable Python utilities shared across modules     |
| `docs/`                  | Technical documentation and reference material      |

```

This structure also separates **learning modules** (`01`–`16`) from reusable infrastructure (`common/`) and documentation (`docs/`), which should make the repository easier to grow as the projects become more advanced.

I would **not change the rest of your README**. Your existing roadmap already matches this structure; the detailed structure simply makes the GitHub repository organization much clearer.
```

---

## 🧠 Learning Roadmap

### 01 — CARLA Basics

Introduction to the CARLA simulator and its architecture.

Topics:

* What is CARLA?
* CARLA architecture
* Client–server architecture
* Starting the simulator
* Connecting with Python
* CARLA Python API
* Worlds and maps
* Actors
* Blueprints
* Spawn points

---

### 02 — Worlds and Maps

Working with CARLA environments.

Topics:

* Loading maps
* Town01
* Town02
* Town03
* Town04
* Town05
* Town06
* Town07
* Town10
* Town12
* Getting available maps
* Changing weather
* Synchronous vs asynchronous mode

Example:

```python
world = client.get_world()

world.load_world("Town01")
```

---

### 03 — Vehicles

Learn how to create and control vehicles.

Topics:

* Vehicle blueprints
* Vehicle brands and models
* Spawn points
* Spawning vehicles
* Destroying vehicles
* Vehicle transforms
* Vehicle physics
* Autopilot
* Traffic Manager

Example:

```python
vehicle_bp = blueprint_library.find("vehicle.tesla.model3")

vehicle = world.try_spawn_actor(
    vehicle_bp,
    spawn_point
)
```

---

### 04 — Traffic Simulation

Creating realistic traffic scenarios.

Topics:

* Traffic Manager
* Multiple vehicles
* Autopilot
* Vehicle behavior
* Traffic density
* Speed control
* Lane changes
* Following distance
* Traffic lights
* Pedestrians

Example:

```python
vehicle.set_autopilot(
    True,
    traffic_manager.get_port()
)
```

---

### 05 — CARLA Sensors

Understanding how autonomous vehicles perceive their environment.

Sensors covered:

* RGB Camera
* Semantic Segmentation Camera
* Instance Segmentation Camera
* Depth Camera
* LiDAR
* Radar
* GNSS
* IMU
* DVS Camera
* Optical Flow Camera

---

### 06 — RGB Camera

Working with camera images.

Topics:

* Camera blueprints
* Camera transforms
* Field of view
* Image resolution
* Camera callbacks
* OpenCV
* Live camera visualization
* Saving images

Example:

```python
camera.listen(
    lambda image: rgb_callback(
        image,
        sensor_data
    )
)
```

---

### 07 — Semantic Segmentation

Understanding the semantic information provided by CARLA.

Topics:

* Semantic segmentation
* CityScapes palette
* Pixel classification
* Semantic classes
* Live visualization
* OpenCV integration

Example:

```python
image.convert(
    carla.ColorConverter.CityScapesPalette
)
```

Live visualization:

```python
cv2.imshow(
    "Semantic Segmentation",
    sensor_data["sem_image"]
)
```

---

### 08 — Depth Camera

Understanding distance information from camera images.

Topics:

* Depth camera
* Depth encoding
* Depth visualization
* Distance estimation
* Depth-based obstacle detection

---

### 09 — LiDAR

Working with 3D point clouds.

Topics:

* LiDAR configuration
* Point clouds
* Ray casting
* Point visualization
* Object detection using LiDAR
* LiDAR-based obstacle detection

---

### 10 — Radar

Working with radar measurements.

Topics:

* Radar sensor
* Velocity measurements
* Detection points
* Relative velocity
* Object tracking

---

### 11 — Computer Vision

Using CARLA as a computer-vision dataset and simulation environment.

Topics:

* OpenCV
* Image processing
* Object detection
* Bounding boxes
* Image segmentation
* Feature extraction
* Camera-based perception

---

### 12 — YOLO + CARLA

Integrating modern object detection with CARLA.

Topics:

* YOLO
* Ultralytics
* Object detection
* Vehicle detection
* Pedestrian detection
* Bounding boxes
* Real-time perception

Example architecture:

```text
CARLA
  │
  ▼
RGB Camera
  │
  ▼
OpenCV
  │
  ▼
YOLO
  │
  ▼
Object Detection
  │
  ▼
ADAS / Autonomous Driving
```

---

### 13 — Vehicle Control

Learning how to control a vehicle programmatically.

Topics:

* Throttle
* Brake
* Steering
* Gear
* VehicleControl
* Manual control
* Automatic control
* PID controllers

Example:

```python
control = carla.VehicleControl()

control.throttle = 0.5
control.steer = 0.0
control.brake = 0.0

vehicle.apply_control(control)
```

---

### 14 — ADAS Projects

Applying CARLA to real automotive problems.

Planned projects:

#### 🚨 Automatic Emergency Braking

Detect an obstacle and automatically apply the brakes.

```text
Camera / LiDAR
      │
      ▼
Object Detection
      │
      ▼
Distance Estimation
      │
      ▼
Time To Collision
      │
      ▼
AEB Decision
      │
      ▼
Brake
```

#### 🚘 Adaptive Cruise Control

Maintain a target speed and safe distance from the vehicle ahead.

#### 🛣️ Lane Detection

Detect lane markings and estimate the vehicle's position inside the lane.

#### 🚦 Traffic Light Detection

Detect and classify traffic lights.

#### 🚶 Pedestrian Detection

Detect pedestrians and estimate collision risk.

---

### 15 — Sensor Fusion

Combining information from multiple sensors.

Examples:

```text
RGB Camera ─────┐
                │
LiDAR ──────────┼──► Sensor Fusion ──► Perception
                │
Radar ──────────┘
```

Topics:

* Camera + LiDAR
* Camera + Radar
* LiDAR + Radar
* Object association
* Tracking
* Sensor coordinates
* Coordinate transformations

---

### 16 — CARLA + ROS 2

Integrating CARLA with **ROS 2**.

Topics:

* ROS 2 bridge
* ROS 2 nodes
* Topics
* Publishers
* Subscribers
* Sensor topics
* Vehicle control
* TF
* RViz
* ROS 2 perception pipelines

Target architecture:

```text
                  CARLA
                    │
        ┌───────────┼───────────┐
        │           │           │
      Camera      LiDAR       Radar
        │           │           │
        └───────────┼───────────┘
                    │
                ROS 2 Bridge
                    │
        ┌───────────┼───────────┐
        │           │           │
     Perception   Planning   Control
        │           │           │
        └───────────┼───────────┘
                    │
              Vehicle Control
                    │
                  CARLA
```

---

## 🛠️ Technologies

The repository uses:

* **CARLA**
* **Python**
* **OpenCV**
* **NumPy**
* **YOLO / Ultralytics**
* **ROS 2**
* **C++**
* **Git**
* **VS Code**

---

## 💻 Environment

Current development environment:

```text
OS: Windows
Simulator: CARLA 0.9.16
Python: 3.12
IDE: VS Code
```

CARLA is accessed through its Python API.

---

## 🚀 Getting Started

### 1. Start CARLA

Start the CARLA simulator and wait until the server is running.

The default CARLA server port is:

```text
2000
```

---

### 2. Verify Python

Check Python:

```powershell
py --version
```

For CARLA 0.9.16:

```powershell
py -3.12 --version
```

---

### 3. Verify CARLA

```powershell
py -3.12 -c "import carla; print(carla.__version__)"
```

---

### 4. Connect to CARLA

```python
import carla

client = carla.Client(
    "localhost",
    2000
)

client.set_timeout(10.0)

world = client.get_world()

print(world.get_map().name)
```

---

## 📂 Repository Structure

```text
LearnCARLA/
│
├── 01_carla_basics/
│
├── 02_worlds_and_maps/
│
├── 03_vehicles/
│
├── 04_traffic/
│
├── 05_sensors/
│
├── 06_rgb_camera/
│
├── 07_semantic_segmentation/
│
├── 08_depth_camera/
│
├── 09_lidar/
│
├── 10_radar/
│
├── 11_computer_vision/
│
├── 12_yolo/
│
├── 13_vehicle_control/
│
├── 14_adas/
│   ├── aeb/
│   ├── acc/
│   ├── lane_detection/
│   └── traffic_light_detection/
│
├── 15_sensor_fusion/
│
├── 16_ros2/
│
├── README.md
│
└── requirements.txt
```

---

## 🧪 Projects

The repository will progressively move from simple experiments to complete autonomous-driving applications.

| Level           | Project                     | Main Technologies       |
| --------------- | --------------------------- | ----------------------- |
| 🟢 Beginner     | Spawn vehicles              | CARLA + Python          |
| 🟢 Beginner     | Traffic simulation          | CARLA + Traffic Manager |
| 🟢 Beginner     | RGB camera                  | CARLA + OpenCV          |
| 🟡 Intermediate | Semantic segmentation       | CARLA + OpenCV          |
| 🟡 Intermediate | LiDAR visualization         | CARLA + NumPy           |
| 🟡 Intermediate | Object detection            | CARLA + YOLO            |
| 🟡 Intermediate | Lane detection              | OpenCV                  |
| 🔴 Advanced     | Automatic Emergency Braking | CARLA + Python          |
| 🔴 Advanced     | Adaptive Cruise Control     | CARLA + Control         |
| 🔴 Advanced     | Sensor fusion               | Camera + LiDAR + Radar  |
| 🔴 Advanced     | Autonomous vehicle          | CARLA + ROS 2           |

---

## 📚 Learning Philosophy

This repository follows a **learn-by-building** approach.

Instead of only studying the CARLA API, each topic is connected to an automotive application.

The progression is:

```text
CARLA Basics
     ↓
Simulation
     ↓
Sensors
     ↓
Perception
     ↓
Object Detection
     ↓
Vehicle Control
     ↓
ADAS
     ↓
Sensor Fusion
     ↓
ROS 2
     ↓
Autonomous Driving
```

---

## 🔗 Useful Resources

* [CARLA Documentation](https://carla.readthedocs.io/)
* [CARLA Python API](https://carla.readthedocs.io/en/latest/python_api/)
* [CARLA GitHub](https://github.com/carla-simulator/carla)
* [Ultralytics YOLO](https://docs.ultralytics.com/)
* [OpenCV Documentation](https://docs.opencv.org/)
* [ROS 2 Documentation](https://docs.ros.org/)

---

## 📈 Progress

This repository is continuously evolving as new CARLA concepts and autonomous-driving projects are implemented.

### Current Focus

* [x] CARLA installation
* [x] CARLA Python API
* [x] Connecting to CARLA
* [x] Loading worlds
* [x] Spawning vehicles
* [x] Vehicle autopilot
* [x] Traffic Manager
* [x] RGB camera
* [x] Semantic segmentation
* [ ] Depth camera
* [ ] LiDAR
* [ ] Radar
* [ ] YOLO object detection
* [ ] Vehicle control
* [ ] AEB
* [ ] ACC
* [ ] Sensor fusion
* [ ] CARLA + ROS 2
* [ ] Autonomous driving pipeline

---

## 🚗 Final Goal

The ultimate goal of **LearnCARLA** is to build a complete simulation-based autonomous-driving stack:

```text
                 ┌──────────────┐
                 │    CARLA     │
                 │  Simulation  │
                 └──────┬───────┘
                        │
              ┌─────────┴─────────┐
              │      Sensors      │
              │ Camera/LiDAR/Radar│
              └─────────┬─────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ Perception  │
                 │ YOLO / CV   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   Planning  │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   Control   │
                 │ PID / AEB   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   Vehicle   │
                 └─────────────┘
```

**Learn → Build → Test → Improve → Repeat.** 🚗🤖
