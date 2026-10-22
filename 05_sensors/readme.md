# CARLA Sensors

Sensors are one of the most important parts of CARLA for autonomous-driving development.

A vehicle in CARLA does not automatically "see" or "understand" its environment. Instead, sensors are attached to actors, usually vehicles, and generate measurements representing what a real vehicle's sensors might observe.

The sensor data can then be used for:

- Perception
- Object detection
- Object classification
- Localization
- Sensor fusion
- Vehicle control
- ADAS
- Autonomous driving
- Scenario testing

The general architecture is:

```text
CARLA World
     │
     ▼
   Vehicle
     │
     ├── RGB Camera
     ├── Semantic Camera
     ├── Instance Camera
     ├── Depth Camera
     ├── LiDAR
     ├── Radar
     ├── GNSS
     └── IMU
            │
            ▼
       Sensor Data
            │
            ▼
     Perception / Fusion
            │
            ▼
      Planning / Control
```

---

# 1. What is a Sensor?

In CARLA, a sensor is a special type of actor that retrieves information from its surroundings.

For example:

```text
RGB Camera
    ↓
Image

LiDAR
    ↓
Point Cloud

Radar
    ↓
Radar Detections

GNSS
    ↓
Latitude / Longitude / Altitude

IMU
    ↓
Acceleration / Angular Velocity / Compass
```

Sensors can produce data every simulation step or according to a configured sensor interval. Some event-based sensors only produce data when a specific event occurs.

---

# 2. Sensor Lifecycle

CARLA sensors generally follow the same lifecycle:

```text
1. Find Blueprint
       ↓
2. Configure Attributes
       ↓
3. Create Transform
       ↓
4. Attach to Vehicle
       ↓
5. Start Listening
       ↓
6. Receive Sensor Data
       ↓
7. Process Data
       ↓
8. Stop Sensor
       ↓
9. Destroy Sensor
```

For example:

```python
blueprint = world.get_blueprint_library().find(
    "sensor.camera.rgb"
)
```

Configure it:

```python
blueprint.set_attribute(
    "image_size_x",
    "1280"
)

blueprint.set_attribute(
    "image_size_y",
    "720"
)

blueprint.set_attribute(
    "fov",
    "90"
)
```

Create a transform:

```python
transform = carla.Transform(
    carla.Location(
        x=1.5,
        z=2.0
    )
)
```

Attach the sensor:

```python
camera = world.spawn_actor(
    blueprint,
    transform,
    attach_to=vehicle
)
```

Then listen for data:

```python
camera.listen(
    lambda data: process(data)
)
```

This pattern will be reused throughout this entire section.

---

# 3. Sensor Blueprints

Sensors are created from the CARLA Blueprint Library.

For example:

```python
blueprint_library = world.get_blueprint_library()
```

RGB camera:

```python
rgb_camera = blueprint_library.find(
    "sensor.camera.rgb"
)
```

Semantic segmentation:

```python
semantic_camera = blueprint_library.find(
    "sensor.camera.semantic_segmentation"
)
```

Depth:

```python
depth_camera = blueprint_library.find(
    "sensor.camera.depth"
)
```

LiDAR:

```python
lidar = blueprint_library.find(
    "sensor.lidar.ray_cast"
)
```

Radar:

```python
radar = blueprint_library.find(
    "sensor.other.radar"
)
```

GNSS:

```python
gnss = blueprint_library.find(
    "sensor.other.gnss"
)
```

IMU:

```python
imu = blueprint_library.find(
    "sensor.other.imu"
)
```

The blueprint defines the characteristics of the sensor before it is spawned.

---

# 4. Sensor Attributes

Sensor attributes determine how the sensor behaves.

For cameras, common attributes include:

```text
image_size_x
image_size_y
fov
sensor_tick
```

For example:

```python
camera_bp.set_attribute(
    "image_size_x",
    "1280"
)

camera_bp.set_attribute(
    "image_size_y",
    "720"
)

camera_bp.set_attribute(
    "fov",
    "90"
)
```

`image_size_x` and `image_size_y` define the output resolution.

`fov` defines the horizontal field of view.

`sensor_tick` determines the simulation-time interval between sensor measurements.

A `sensor_tick` of `0.0` means the sensor captures as fast as possible.

---

# 5. Attaching Sensors to Vehicles

Sensors are normally attached to a vehicle.

```text
             RGB Camera
                 │
                 │
                 ▼
        ┌─────────────────┐
        │     Vehicle     │
        └─────────────────┘
```

Example:

```python
camera_transform = carla.Transform(
    carla.Location(
        x=1.5,
        z=2.0
    )
)

camera = world.spawn_actor(
    camera_bp,
    camera_transform,
    attach_to=vehicle
)
```

The transform is relative to the parent vehicle when the sensor is attached.

This is extremely important.

For example:

```text
x = forward / backward
y = right / left
z = up / down
```

CARLA uses the Unreal Engine coordinate convention:

```text
X → Forward
Y → Right
Z → Up
```

Sensor coordinates are returned in this coordinate system.

---

# 6. Sensor Data

Every sensor produces a particular type of data.

Some common examples:

| Sensor | CARLA Output | Main Information |
|---|---|---|
| RGB Camera | `carla.Image` | Normal camera image |
| Semantic Camera | `carla.Image` | Semantic class per pixel |
| Instance Camera | `carla.Image` | Object class + instance ID |
| Depth Camera | `carla.Image` | Distance/depth |
| LiDAR | `carla.LidarMeasurement` | 3D point cloud |
| Radar | `carla.RadarMeasurement` | Detection + relative velocity |
| GNSS | `carla.GNSSMeasurement` | Latitude, longitude, altitude |
| IMU | `carla.IMUMeasurement` | Acceleration, angular velocity, compass |

CARLA also provides additional sensors such as optical flow, DVS, semantic LiDAR and event detectors.

---

# 7. Sensor Callbacks

Sensors generate data asynchronously through callbacks.

The basic pattern is:

```python
sensor.listen(
    lambda data: process(data)
)
```

For example:

```python
def process_image(image):
    print(
        f"Frame: {image.frame}"
    )

camera.listen(process_image)
```

Every time the camera generates a new image, CARLA calls:

```python
process_image(image)
```

This means sensor processing is fundamentally **data-driven**.

Instead of repeatedly asking:

```text
"Do I have new sensor data?"
```

the sensor tells your application:

```text
"Here is the next measurement."
```

---

# 8. Important Sensor Data Metadata

CARLA sensor measurements commonly contain information such as:

```text
frame
timestamp
transform
```

### Frame

The simulation frame in which the measurement was generated.

```python
data.frame
```

### Timestamp

Simulation time associated with the measurement.

```python
data.timestamp
```

### Transform

The sensor's transform at the time of measurement.

```python
data.transform
```

These fields become particularly important when working with **sensor fusion**.

For example:

```text
Camera Frame 1520
        │
        ├── timestamp
        │
        ▼
LiDAR Frame 1520
        │
        ├── timestamp
        │
        ▼
Radar Frame 1520
```

Later, we'll use these concepts when combining multiple sensors.

---

# 9. Camera Sensors

CARLA provides several camera types.

## RGB

```text
sensor.camera.rgb
```

Produces a normal color image.

Example:

```text
Road
Vehicles
Pedestrians
Traffic signs
Buildings
Traffic lights
```

This is the primary sensor we'll use for computer vision and YOLO.

---

## Semantic Segmentation

```text
sensor.camera.semantic_segmentation
```

Instead of producing a realistic image, every pixel represents a semantic class.

Conceptually:

```text
Road       → Road
Vehicle    → Vehicle
Pedestrian → Pedestrian
Building   → Building
Vegetation → Vegetation
```

This is extremely useful for understanding the ground truth of a scene.

---

## Instance Segmentation

```text
sensor.camera.instance_segmentation
```

This goes one step further.

Semantic segmentation answers:

```text
"What class is this pixel?"
```

Instance segmentation answers:

```text
"Which individual object does this pixel belong to?"
```

For example:

```text
Vehicle #1
Vehicle #2
Vehicle #3
Pedestrian #1
Pedestrian #2
```

This distinction becomes important for object-level perception.

---

## Depth

```text
sensor.camera.depth
```

Depth cameras provide information about the distance of objects from the camera.

Conceptually:

```text
Camera
   │
   ├── Car      → 25 m
   ├── Pedestrian → 15 m
   └── Building → 40 m
```

Depth information becomes particularly useful for:

- 3D perception
- Object distance estimation
- Sensor fusion
- Collision prediction

---

# 10. LiDAR

CARLA provides a ray-cast LiDAR sensor:

```text
sensor.lidar.ray_cast
```

LiDAR generates a point cloud.

Conceptually:

```text
                •
           •         •
      •                  •
   •          Vehicle       •
      •                  •
           •         •
                •
```

Each point contains spatial information.

LiDAR is particularly useful for:

- 3D object detection
- Obstacle detection
- Mapping
- Localization
- Sensor fusion

CARLA also provides semantic LiDAR, which adds semantic and instance information to LiDAR measurements.

---

# 11. Radar

Radar provides detections including:

```text
Distance
Azimuth
Altitude
Relative velocity
```

The relative velocity is particularly important.

For example:

```text
Target A
Distance: 30 m
Velocity relative to sensor: -12 m/s
```

This tells us that the target is approaching the vehicle.

Radar is therefore particularly interesting for:

- Adaptive Cruise Control
- Forward Collision Warning
- Automatic Emergency Braking
- Object tracking
- Sensor fusion

CARLA represents radar detections through `carla.RadarMeasurement` and `carla.RadarDetection`.

---

# 12. GNSS

GNSS provides geographic position:

```text
Latitude
Longitude
Altitude
```

CARLA provides this through:

```python
carla.GNSSMeasurement
```

Example:

```text
Latitude: 57.xxxxxx
Longitude: 11.xxxxxx
Altitude: 12.4 m
```

GNSS is useful for:

- Global localization
- Navigation
- Route planning
- Combining global and local position estimates

CARLA can also configure GNSS noise parameters to simulate imperfect measurements.

---

# 13. IMU

The IMU provides:

```text
Accelerometer
Gyroscope
Compass
```

CARLA exposes this through:

```python
carla.IMUMeasurement
```

The accelerometer measures linear acceleration:

```text
m/s²
```

The gyroscope measures angular velocity:

```text
rad/s
```

The compass provides orientation information.

IMU data becomes particularly important for:

- Localization
- Dead reckoning
- Vehicle dynamics
- Sensor fusion
- Autonomous navigation

CARLA also provides configurable noise parameters for the accelerometer and gyroscope.

---

# 14. Comparing the Sensors

A useful way to think about the sensors is:

```text
                    WHAT DOES THE VEHICLE KNOW?
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
       Vision              Geometry            Motion
          │                   │                   │
     RGB Camera          LiDAR / Depth          IMU
     Semantic            Radar                  GNSS
     Instance
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
                              ▼
                         Sensor Fusion
                              │
                              ▼
                         World Model
```

Each sensor provides a different view of the environment.

---

# 15. Why Sensor Fusion Matters

No individual sensor is perfect.

For example:

### Camera

Excellent at:

```text
Color
Objects
Traffic signs
Traffic lights
Semantic information
```

But a camera does not directly provide reliable metric distance in the same way LiDAR does.

### LiDAR

Excellent at:

```text
3D geometry
Distance
Object shape
```

But LiDAR does not naturally provide the rich color/appearance information of an RGB camera.

### Radar

Excellent at:

```text
Distance
Relative velocity
```

But provides much less detailed object appearance.

### GNSS

Excellent for:

```text
Global position
```

But does not tell us what is around the vehicle.

### IMU

Excellent for:

```text
Acceleration
Angular motion
Orientation
```

But position drifts when estimated over time without corrections.

Therefore:

```text
Camera
   +
LiDAR
   +
Radar
   +
GNSS
   +
IMU
   ↓
Sensor Fusion
   ↓
Better representation of the vehicle's environment
```

This will become **Stage 2 of your autonomous-driving stack**.

---

# 16. Sensors in Our LearnCARLA Project

We will focus on the sensors most relevant to autonomous driving.

Our implementation order is:

```text
05_sensors/
│
├── rgb_camera/
│   ├── rgb_camera.py
│   └── live_view.py
│
├── semantic_segmentation/
│   ├── semantic_camera.py
│   └── live_view.py
│
├── instance_segmentation/
│   └── instance_camera.py
│
├── depth/
│   └── depth_camera.py
│
├── lidar/
│   └── lidar.py
│
├── radar/
│   └── radar.py
│
├── gnss/
│   └── gnss.py
│
└── imu/
    └── imu.py
```

The learning progression is intentional:

```text
RGB
 │
 ├── Understand camera data
 │
 ▼
Semantic Segmentation
 │
 ├── Understand pixel-level ground truth
 │
 ▼
Instance Segmentation
 │
 ├── Understand individual objects
 │
 ▼
Depth
 │
 ├── Understand distance
 │
 ▼
LiDAR
 │
 ├── Understand 3D geometry
 │
 ▼
Radar
 │
 ├── Understand relative motion
 │
 ▼
GNSS
 │
 ├── Understand global position
 │
 ▼
IMU
 │
 └── Understand vehicle motion
```

After this section, we will be able to combine these measurements into the perception and localization pipelines used later in LearnCARLA.

---

# 17. The Most Important Concept

The key idea to remember throughout this section is:

```text
Sensor ≠ Intelligence
```

A camera does not detect a car by itself.

It produces:

```text
Pixels
```

LiDAR does not understand a pedestrian.

It produces:

```text
3D points
```

Radar does not understand traffic.

It produces:

```text
Detections + relative velocity
```

The intelligence comes from the software processing these measurements:

```text
Sensors
   ↓
Raw Data
   ↓
Signal / Image Processing
   ↓
Perception
   ↓
Object Representation
   ↓
Sensor Fusion
   ↓
Localization
   ↓
Planning
   ↓
Control
```

That distinction will be important as we move from **CARLA simulation** into **computer vision, YOLO, sensor fusion, and ADAS**.

---

## References

- [CARLA 0.9.16 — Sensors and data](https://carla.readthedocs.io/en/0.9.16/core_sensors/?utm_source=chatgpt.com)
- [CARLA — Sensors reference](https://carla.readthedocs.io/en/latest/ref_sensors/?utm_source=chatgpt.com)