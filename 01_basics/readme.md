# 01 — CARLA Basics

This section introduces the fundamental concepts required to work with the CARLA Simulator through the Python API.

The goal is to understand how a Python program connects to CARLA, accesses the simulation world, discovers available maps, and loads a map.

---

## 🎯 Learning Objectives

By completing this section, you should understand:

* How the CARLA client connects to the simulator
* The CARLA client/server architecture
* How to access the current simulation world
* How to retrieve the current map
* How to list available CARLA maps
* How to load a different map
* How the CARLA Python API communicates with the simulator

---

## 🏗️ CARLA Client/Server Architecture

CARLA uses a client/server architecture.

```text
┌──────────────────────┐
│   CARLA Simulator    │
│                      │
│  Unreal Engine       │
│  World               │
│  Vehicles            │
│  Sensors             │
│  Traffic             │
└──────────┬───────────┘
           │
           │ TCP
           │ Port 2000
           │
┌──────────▼───────────┐
│   Python Client      │
│                      │
│   carla.Client()     │
│   Python API         │
└──────────────────────┘
```

The **CARLA Simulator** runs the simulation.

The **Python client** sends commands to the simulator and receives information from it.

The default CARLA server port is:

```text
localhost:2000
```

---

# 01 — Connect to CARLA

File:

```text
01_connect_to_carla.py
```

The first step is establishing a connection with the CARLA server.

```python
import carla

client = carla.Client("localhost", 2000)

client.set_timeout(10.0)

print(client.get_server_version())
```

The important object is:

```python
carla.Client()
```

It represents the connection between your Python program and the CARLA simulator.

### Run

Start the CARLA simulator first.

Then:

```powershell
py -3.12 01_connect_to_carla.py
```

---

# 02 — Get the World

File:

```text
02_get_world.py
```

After connecting to CARLA, we can access the current simulation world.

```python
world = client.get_world()
```

The `world` object gives access to many parts of the simulation, including:

* Map
* Actors
* Weather
* Settings
* Blueprints
* Traffic lights
* Sensors

For example:

```python
map_name = world.get_map().name

print(map_name)
```

### Concept

Think of the `world` as the main interface to the current CARLA simulation.

```text
CARLA Client
     │
     ▼
   World
     │
     ├── Map
     ├── Actors
     ├── Weather
     ├── Settings
     ├── Traffic Lights
     └── Sensors
```

### Run

```powershell
py -3.12 02_get_world.py
```

---

# 03 — Get Available Maps

File:

```text
03_get_maps.py
```

CARLA provides several maps that can be loaded into the simulator.

We can retrieve them using:

```python
maps = client.get_available_maps()
```

Then:

```python
for map_name in maps:
    print(map_name)
```

This is useful when you want your Python program to discover which maps are available instead of hardcoding a map name.

### Run

```powershell
py -3.12 03_get_maps.py
```

---

# 04 — Load a Map

File:

```text
04_load_map.py
```

A different map can be loaded using:

```python
world = client.load_world("Town01")
```

For example:

```python
client.load_world("Town03")
```

will load Town03.

The map is part of the simulation world:

```text
CARLA
 │
 └── World
      │
      └── Map
           │
           ├── Roads
           ├── Buildings
           ├── Junctions
           ├── Sidewalks
           └── Spawn Points
```

### Run

```powershell
py -3.12 04_load_map.py
```

---

# 🧪 Exercises

After completing the four examples, try the following.

### Exercise 1 — Change the map

Modify:

```python
map_name = "Town01"
```

to:

```python
map_name = "Town03"
```

Run the program and observe the change in CARLA.

---

### Exercise 2 — Print the current map

Modify `02_get_world.py` so that it prints:

```text
Current map: ...
```

---

### Exercise 3 — List all maps

Run:

```powershell
py -3.12 03_get_maps.py
```

and identify how many maps are available in your CARLA installation.

---

### Exercise 4 — Load different maps

Try:

```text
Town01
Town02
Town03
Town04
Town05
Town06
Town07
Town10
Town12
```

Observe the differences between the environments.

---

# 🧠 Key Concepts

| Concept                       | Description                              |
| ----------------------------- | ---------------------------------------- |
| `carla.Client`                | Connects Python to the CARLA server      |
| `localhost`                   | The local computer running CARLA         |
| `2000`                        | Default CARLA server port                |
| `client.get_world()`          | Gets the current simulation world        |
| `world.get_map()`             | Gets the current map                     |
| `client.get_available_maps()` | Lists available maps                     |
| `client.load_world()`         | Loads a different map                    |
| `world`                       | Main interface to the current simulation |

---

# ✅ Progress Checklist

* [X] Connect to CARLA
* [X] Understand client/server architecture
* [X] Get the current world
* [X] Get the current map
* [X] List available maps
* [X] Load a different map
* [X] Complete the exercises

---

## 🚀 Next Step

After completing these exercises, continue to:

```text
02 — Worlds & Maps
```

There we will go deeper into the CARLA world, including:

* Weather
* Time of day
* Simulation settings
* Map properties
* Spawn points
* Synchronous/asynchronous simulation
* World configuration
