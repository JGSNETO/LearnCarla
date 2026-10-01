# 04 — Traffic Simulation

This section introduces **traffic simulation in CARLA**.

After learning how to create and manage individual actors, the next step is to create a dynamic traffic environment where multiple vehicles can move, interact, and follow traffic rules.

CARLA provides the **Traffic Manager** to control and coordinate autonomous vehicles inside the simulation.

Traffic simulation is an important foundation for autonomous-driving development because an autonomous vehicle must operate in an environment containing other road users.

---

## Learning Objectives

By completing this section, you will learn:

- How vehicle autopilot works in CARLA
- How to use the Traffic Manager
- How to configure autonomous vehicles
- How to generate multiple vehicles
- How to control traffic density
- How to configure vehicle speed
- How to configure following distance
- How to influence lane changes
- How traffic lights interact with vehicles
- How to create randomized traffic
- How to clean up generated traffic

---

# 4.1 — Vehicle Autopilot

CARLA vehicles can be placed into autonomous driving mode using:

```python
vehicle.set_autopilot(True)
```

When autopilot is enabled, CARLA controls the vehicle's basic driving behavior.

Conceptually:

```text
Vehicle Actor
      ↓
set_autopilot(True)
      ↓
CARLA Traffic System
      ↓
Vehicle follows roads
```

Autopilot is useful for quickly creating moving traffic without implementing a vehicle controller manually.

---

# 4.2 — Traffic Manager

The **Traffic Manager (TM)** is CARLA's system for controlling the behavior of multiple autonomous vehicles.

It manages aspects such as:

- Vehicle speed
- Following distance
- Lane changes
- Traffic lights
- Junction behavior
- Collision avoidance
- Traffic density
- Vehicle interactions

The basic architecture is:

```text
CARLA World
     │
     ├── Vehicles
     │
     └── Traffic Manager
             │
             ├── Speed
             ├── Distance
             ├── Lane Changes
             ├── Traffic Lights
             └── Vehicle Behavior
```

---

# 4.3 — Traffic Manager Port

The Traffic Manager runs on its own port.

The default port is:

```text
8000
```

A Traffic Manager instance can be obtained with:

```python
traffic_manager = client.get_trafficmanager(8000)
```

Vehicles can then be associated with that Traffic Manager:

```python
vehicle.set_autopilot(True, 8000)
```

Using the same Traffic Manager instance allows multiple vehicles to participate in the same traffic simulation.

---

# 4.4 — Generating Traffic

Instead of manually spawning one vehicle at a time, CARLA can be used to create larger traffic populations.

The general workflow is:

```text
Vehicle Blueprints
        +
Spawn Points
        ↓
Generate Vehicles
        ↓
Enable Autopilot
        ↓
Traffic Manager
        ↓
Dynamic Traffic
```

This allows us to create urban or highway environments with many moving vehicles.

---

# 4.5 — Traffic Density

Traffic density can be changed by controlling the number of vehicles generated.

For example:

```text
Low Density
    ↓
10 vehicles

Medium Density
    ↓
30 vehicles

High Density
    ↓
60+ vehicles
```

Traffic density is useful when testing autonomous-driving systems under different levels of environmental complexity.

---

# 4.6 — Vehicle Speed

The Traffic Manager allows the global speed behavior of vehicles to be modified.

For example:

```python
traffic_manager.global_percentage_speed_difference(10.0)
```

A positive value causes vehicles to drive below their recommended speed.

Different speed configurations can be used to simulate:

- Slow traffic
- Normal traffic
- Fast traffic
- Congested traffic

---

# 4.7 — Following Distance

The distance between vehicles can also be configured.

For example:

```python
traffic_manager.set_global_distance_to_leading_vehicle(3.0)
```

This influences how closely vehicles follow the vehicle ahead.

This concept becomes particularly important later when studying:

- Adaptive Cruise Control
- Forward Collision Warning
- Automatic Emergency Braking
- Time-to-Collision

---

# 4.8 — Lane Changes

The Traffic Manager can influence whether vehicles are allowed to change lanes.

This is useful for creating more realistic traffic behavior.

Conceptually:

```text
Vehicle
   │
   ├── Follow Lane
   │
   └── Change Lane
```

Later, lane-change behavior can be combined with autonomous-driving scenarios such as:

- Vehicle cut-ins
- Overtaking
- Highway traffic
- Lane-change conflicts

---

# 4.9 — Traffic Lights

Vehicles controlled by the Traffic Manager can interact with traffic lights.

A simplified interaction is:

```text
Traffic Light
      │
      ├── Green ──→ Continue
      │
      ├── Yellow ─→ Prepare to stop
      │
      └── Red ────→ Stop
```

Traffic-light scenarios will become particularly important later when working with perception and ADAS.

---

# 4.10 — Randomized Traffic

Real traffic is not deterministic.

Vehicles can have different:

- Models
- Speeds
- Following distances
- Routes
- Lane behavior
- Spawn locations

Randomized traffic allows us to create more varied simulation conditions.

A typical scenario might contain:

```text
        Vehicle A
             ↓
        Vehicle B ──────→
             ↓
Pedestrian → Road ← Vehicle C

       Traffic Light
             ↓
        Vehicle D
```

This is closer to the complexity an autonomous-driving system must handle.

---

# 4.11 — Traffic Scenarios

Traffic simulation becomes particularly useful when creating repeatable autonomous-driving scenarios.

Examples include:

### Urban Traffic

```text
Multiple vehicles
+
Traffic lights
+
Intersections
+
Pedestrians
```

### Highway Traffic

```text
Multiple lanes
+
High vehicle speeds
+
Following traffic
+
Lane changes
```

### Cut-In Scenario

```text
Vehicle A ──────────────→

Vehicle B ──→
              ↘
               ↘
                → Vehicle A
```

These scenarios will later be used for ADAS and autonomous-driving testing.

---

# 4.12 — Traffic Cleanup

Generated vehicles should be destroyed when the experiment finishes.

The basic lifecycle is:

```text
Generate Traffic
      ↓
Run Simulation
      ↓
Collect Results
      ↓
Destroy Vehicles
```

Cleaning up actors prevents old simulation objects from interfering with future experiments.

---

# Project Structure

```text
04_traffic/
│
├── 01_autopilot.py
├── 02_traffic_manager.py
├── 03_generate_traffic.py
└── README.md
```

---

# Exercises

| File | Description |
|---|---|
| `01_autopilot.py` | Enable autonomous driving for a vehicle |
| `02_traffic_manager.py` | Configure and control the Traffic Manager |
| `03_generate_traffic.py` | Generate and manage multiple traffic vehicles |

---

# Learning Progression

The exercises follow this progression:

```text
01_autopilot.py
       ↓
Understand vehicle autopilot
       ↓
02_traffic_manager.py
       ↓
Control vehicle behavior
       ↓
03_generate_traffic.py
       ↓
Create realistic traffic
```

---

# Key Concepts

By the end of this section, you should understand:

- **Autopilot**
- **Traffic Manager**
- **Traffic Manager port**
- **Traffic density**
- **Vehicle speed**
- **Following distance**
- **Lane changes**
- **Traffic lights**
- **Randomized traffic**
- **Traffic cleanup**

---

# Connection to Autonomous Driving

Traffic simulation is the first step toward creating realistic autonomous-driving environments.

The overall progression of the LearnCARLA project is:

```text
01 — CARLA Basics
        ↓
02 — Worlds & Maps
        ↓
03 — Actors
        ↓
04 — Traffic Simulation
        ↓
05 — Sensors
        ↓
06 — Computer Vision
        ↓
07 — YOLO
        ↓
08 — Vehicle Control
        ↓
09 — ADAS
        ↓
10 — Sensor Fusion
        ↓
11 — Localization
        ↓
12 — Planning
        ↓
13 — Autonomous Driving
```

At this stage, we move from simply placing actors in the world to creating a **dynamic road environment**.

Later, these traffic actors will become targets for perception systems, ADAS algorithms, planning systems, and autonomous-driving validation.