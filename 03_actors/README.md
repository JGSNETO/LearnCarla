# 03 — Actors

This section introduces the **Actor system in CARLA**.

Actors are the objects that exist and interact inside the CARLA simulation. Vehicles, pedestrians, sensors, traffic lights, and other simulation entities are represented as actors.

Understanding actors is essential for building autonomous-driving scenarios because perception, planning, control, and traffic simulation all interact with actors.

---

## Learning Objectives

By completing this section, you will learn:

* What an Actor is in CARLA
* How CARLA represents vehicles and pedestrians
* How to access actors in the simulation
* How to work with vehicle blueprints
* How to spawn vehicles
* How to spawn multiple vehicles
* How to spawn pedestrians
* How to retrieve actor information
* How to destroy actors
* How actors are managed inside the CARLA World

---

# 3.1 — What is an Actor?

An **Actor** is an object that exists inside the CARLA simulation and can have a position, orientation, state, and behavior.

Examples include:

* Vehicles
* Pedestrians
* Sensors
* Traffic lights
* Traffic signs

A simplified representation is:

```text
CARLA World
│
└── Actors
    │
    ├── Vehicles
    │
    ├── Pedestrians
    │
    ├── Sensors
    │
    ├── Traffic Lights
    │
    └── Traffic Signs
```

Each actor has a unique identifier and can be accessed through the CARLA Python API.

---

# 3.2 — Actor Blueprints

Before spawning an actor, CARLA uses a **Blueprint** that describes what should be created.

The Blueprint Library contains the available actor types.

For example:

```text
Blueprint Library
│
├── vehicle.*
│   ├── vehicle.tesla.model3
│   ├── vehicle.audi.tt
│   └── ...
│
├── walker.*
│   ├── walker.pedestrian.0001
│   └── ...
│
└── sensor.*
    ├── sensor.camera.rgb
    ├── sensor.lidar.ray_cast
    └── ...
```

Blueprints can also contain attributes that configure the actor before it is spawned.

---

# 3.3 — Vehicles

Vehicles are one of the most important actor types when working with autonomous driving.

CARLA provides many vehicle models that can be selected through the Blueprint Library.

The vehicle workflow is generally:

```text
Blueprint Library
       ↓
Select Vehicle Blueprint
       ↓
Select Spawn Point
       ↓
Spawn Vehicle
       ↓
Vehicle Actor
```

The vehicle actor can then be controlled, monitored, or used as part of a traffic scenario.

---

# 3.4 — Listing Vehicles

The first vehicle exercise focuses on finding the vehicles that already exist in the simulation.

File:

```text
vehicles/list_vehicles.py
```

This introduces:

* Actor retrieval
* Actor filtering
* Vehicle identification
* Vehicle IDs
* Vehicle types

The basic concept is:

```text
World
 ↓
Actors
 ↓
Filter vehicle.*
 ↓
Vehicles
```

---

# 3.5 — Spawning a Vehicle

After learning how to find vehicles, the next step is spawning a new vehicle.

File:

```text
vehicles/spawn_vehicle.py
```

The spawning process requires:

1. A vehicle blueprint
2. A spawn transform
3. The CARLA World

Conceptually:

```text
Vehicle Blueprint
       +
Spawn Point
       ↓
world.spawn_actor()
       ↓
Vehicle Actor
```

The resulting vehicle becomes part of the simulation.

---

# 3.6 — Spawning Multiple Vehicles

A single vehicle is useful for learning, but autonomous-driving scenarios usually contain multiple vehicles.

File:

```text
vehicles/spawn_multiple_vehicles.py
```

This exercise introduces:

* Multiple blueprints
* Multiple spawn points
* Loops
* Random vehicle selection
* `try_spawn_actor()`
* Managing multiple Actor objects

Conceptually:

```text
Vehicle Blueprints
        +
Spawn Points
        ↓
Multiple Spawn Requests
        ↓
Multiple Vehicle Actors
```

This is an important step toward creating realistic traffic scenarios.

---

# 3.7 — Pedestrians

Pedestrians are represented by **walker actors** in CARLA.

They are important for autonomous-driving scenarios because vehicles must detect and respond to people in the environment.

The pedestrian workflow is similar to vehicles:

```text
Pedestrian Blueprint
        +
Spawn Point
        ↓
Spawn Pedestrian
        ↓
Walker Actor
```

---

# 3.8 — Spawning a Pedestrian

File:

```text
pedestrians/spawn_pedestrian.py
```

This exercise introduces:

* Pedestrian blueprints
* Pedestrian spawn locations
* Walker actors
* Basic pedestrian creation

The goal is to understand how pedestrians are represented and created in CARLA.

---

# 3.9 — Spawning Multiple Pedestrians

File:

```text
pedestrians/spawn_pedestrians.py
```

This extends the previous exercise to multiple pedestrians.

It introduces:

* Multiple pedestrian blueprints
* Multiple spawn locations
* Randomized pedestrian selection
* Managing multiple walker actors

This provides the foundation for creating more realistic urban scenarios.

---

# 3.10 — Destroying Actors

Actors created during a simulation should eventually be removed.

For vehicles, this is demonstrated in:

```text
vehicles/destroy_vehicles.py
```

The general lifecycle is:

```text
Create Actor
     ↓
Use Actor
     ↓
Monitor Actor
     ↓
Destroy Actor
```

Destroying actors is important because actors from previous experiments can remain in the simulation if they are not explicitly removed.

This becomes especially important when developing automated simulations and testing scenarios.

---

# Actor Lifecycle

A simplified CARLA actor lifecycle is:

```text
Blueprint
    ↓
Spawn
    ↓
Actor
    ↓
Interact / Control / Monitor
    ↓
Destroy
```

For a vehicle:

```text
Vehicle Blueprint
       ↓
Spawn Point
       ↓
Vehicle Actor
       ↓
Control / Traffic / Sensors
       ↓
Destroy
```

---

# Project Structure

```text
03_actors/
│
├── vehicles/
│   ├── list_vehicles.py
│   ├── spawn_vehicle.py
│   ├── spawn_multiple_vehicles.py
│   └── destroy_vehicles.py
│
├── pedestrians/
│   ├── spawn_pedestrian.py
│   └── spawn_pedestrians.py
│
└── README.md
```

---

# Exercises

| File                                  | Description                                 |
| ------------------------------------- | ------------------------------------------- |
| `vehicles/list_vehicles.py`           | Find and inspect vehicles in the simulation |
| `vehicles/spawn_vehicle.py`           | Spawn a single vehicle                      |
| `vehicles/spawn_multiple_vehicles.py` | Spawn multiple vehicles                     |
| `vehicles/destroy_vehicles.py`        | Remove vehicles from the simulation         |
| `pedestrians/spawn_pedestrian.py`     | Spawn a single pedestrian                   |
| `pedestrians/spawn_pedestrians.py`    | Spawn multiple pedestrians                  |

---

# Key CARLA Concepts

By the end of this section, you should understand:

```text
Actor
  ↓
Blueprint
  ↓
Spawn Point
  ↓
Spawn Actor
  ↓
Actor Instance
  ↓
Control / Monitor
  ↓
Destroy
```

You should also understand the difference between:

* **Blueprint** — description/template of an actor
* **Spawn Point** — location and orientation where an actor can be created
* **Actor** — actual object currently existing in the simulation

---

# Connection to Autonomous Driving

Actors form the foundation of the autonomous-driving simulation.

A simplified autonomous-driving environment can be represented as:

```text
                 CARLA WORLD
                      │
        ┌─────────────┼─────────────┐
        │             │             │
     Vehicles     Pedestrians     Sensors
        │             │             │
        └─────────────┼─────────────┘
                      │
                  Perception
                      │
                  Planning
                      │
                   Control
                      │
                   Vehicle
```

Later sections will build on this foundation.

For example:

```text
03 Actors
     ↓
05 Sensors
     ↓
06 Computer Vision
     ↓
07 YOLO
     ↓
08 Vehicle Control
     ↓
09 ADAS
     ↓
10 Sensor Fusion
     ↓
12 Planning
     ↓
13 Autonomous Driving
```

Understanding how to create and manage actors is therefore an important foundation for the autonomous-driving projects developed later in this repository.
