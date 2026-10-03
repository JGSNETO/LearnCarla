# 02 — Worlds & Maps

This section introduces the **simulation environment in CARLA**.

A CARLA simulation is built around a `World`, which contains the map, weather, actors, traffic infrastructure, and simulation settings. Understanding the World and Map APIs is essential before working with vehicles, sensors, perception, and autonomous driving.

---

## Learning Objectives

By completing this section, you will understand:

* What a CARLA `World` represents
* The relationship between a World and a Map
* How to load different maps
* How to inspect the current map
* How to modify weather conditions
* How to control the simulation time of day
* How world and simulation settings affect the simulation

---

## 2.1 — What is a World?

The **World** represents the current simulation environment.

It provides access to the main elements of the simulation, including:

* Map
* Vehicles
* Pedestrians
* Sensors
* Traffic lights
* Weather
* Simulation settings
* Other actors

The basic relationship can be visualized as:

```text
CARLA Server
     │
     ▼
   World
     │
     ├── Map
     ├── Vehicles
     ├── Pedestrians
     ├── Sensors
     ├── Traffic Lights
     ├── Weather
     └── Settings
```

The Python client obtains the current World through:

```text
Client → World
```

The World can then be used to access the current Map and other simulation objects.

### Key API

```text
client.get_world()
```

---

## 2.2 — What is a Map?

A **Map** defines the road environment in which the simulation takes place.

A map contains information such as:

* Roads
* Lanes
* Intersections
* Junctions
* Waypoints
* Spawn points
* Traffic infrastructure

The relationship is:

```text
Client
  │
  ▼
World
  │
  ▼
Map
  │
  ├── Roads
  ├── Lanes
  ├── Junctions
  ├── Waypoints
  └── Spawn Points
```

Maps become particularly important later when working with:

* Vehicle navigation
* Waypoint following
* Lane detection
* Route planning
* Autonomous driving
* Traffic simulation

### Key API

```text
world.get_map()
```

---

## 2.3 — Loading Maps

CARLA provides several predefined maps that can be loaded into the simulation.

Examples include:

* `Town01`
* `Town02`
* `Town03`
* `Town04`
* `Town05`
* `Town06`
* `Town07`
* `Town10HD`
* `Town12`

The current map can be inspected through the World.

A different map can be loaded using:

```text
client.load_world()
```

Loading a new map creates a new simulation environment.

This means that actors from the previous World should not be assumed to remain available after changing maps.

---

## 2.4 — Weather

CARLA allows the environment to simulate different weather conditions.

Weather parameters include:

* Cloudiness
* Precipitation
* Precipitation deposits
* Wind
* Sun altitude
* Sun azimuth
* Fog
* Wetness
* Dust

Weather is particularly important for autonomous-driving development because perception systems need to operate under changing environmental conditions.

For example:

```text
Clear
  ↓
Rain
  ↓
Wet roads
  ↓
Reduced visibility
  ↓
More difficult perception
```

Later, these capabilities can be used to create more realistic ADAS and autonomous-driving scenarios.

### Key API

```text
world.get_weather()
world.set_weather()
```

---

## 2.5 — Time of Day

CARLA allows the position of the sun to be controlled.

This makes it possible to simulate different lighting conditions, such as:

* Morning
* Midday
* Afternoon
* Sunset
* Night

Lighting conditions are especially relevant to camera-based perception.

For example:

```text
Daylight
   │
   ├── High visibility
   │
   ▼
Sunset
   │
   ├── Shadows
   ├── Glare
   └── Reduced contrast
   │
   ▼
Night
   │
   ├── Low illumination
   └── Artificial lighting
```

These conditions will become important later when working with cameras, object detection, lane detection, and semantic segmentation.

---

## 2.6 — World & Simulation Settings

CARLA provides settings that control how the simulation behaves.

Examples include:

* Synchronous mode
* Asynchronous mode
* Fixed simulation timestep
* Variable timestep
* Rendering settings
* Substepping
* Physics simulation

These settings become increasingly important when building automated testing and autonomous-driving systems.

For example, **synchronous mode** allows the client to control simulation progression one frame at a time.

This is useful for:

* Deterministic testing
* Sensor synchronization
* Automated scenarios
* Regression testing
* Reproducible experiments

---

# Exercises

The exercises in this folder progressively introduce the World and Map APIs.

| File                | Topic                                |
| ------------------- | ------------------------------------ |
| `01_load_town.py`   | Loading and inspecting CARLA maps    |
| `02_weather.py`     | Changing weather conditions          |
| `03_time_of_day.py` | Controlling lighting and time of day |

---

# Key Concepts

By the end of this section, you should understand the following relationship:

```text
CARLA Client
     │
     ▼
   World
     │
     ├───────────────┐
     ▼               ▼
   Map           Environment
     │               │
     ├── Roads       ├── Weather
     ├── Lanes       ├── Lighting
     ├── Waypoints   └── Time of Day
     └── Spawn Points
```

The **World** is the container for the current simulation environment.

The **Map** defines the road and navigation environment inside that World.

---

# Why This Matters for Autonomous Driving

Understanding Worlds and Maps is foundational for the rest of LearnCARLA.

Later sections will build on these concepts:

```text
World
  │
  ├── Map
  │    └── Roads / Lanes / Waypoints
  │
  ├── Vehicles
  │
  ├── Sensors
  │    ├── Camera
  │    ├── LiDAR
  │    ├── Radar
  │    └── GNSS / IMU
  │
  ├── Weather
  │
  └── Traffic Infrastructure
```

Eventually, these components will be combined into an autonomous-driving pipeline:

```text
CARLA World
     │
     ▼
   Sensors
     │
     ▼
 Perception
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
  Control
     │
     ▼
  Vehicle
```

This section establishes the environment in which all of those systems will operate.
