import carla


def main():
    # Connect to CARLA
    client = carla.Client("localhost", 2000)
    client.set_timeout(10.0)

    # Get world
    world = client.get_world()

    # Get blueprint library
    blueprint_library = world.get_blueprint_library()

    # Get vehicle blueprints
    vehicle_blueprints = blueprint_library.filter("vehicle.*")

    # Get spawn points
    spawn_points = world.get_map().get_spawn_points()

    # Number of vehicles to spawn
    number_of_vehicles = 5

    # Make sure there are enough spawn points
    if len(spawn_points) < number_of_vehicles:
        print("Not enough spawn points available.")
        return

    # Store successfully spawned vehicles
    vehicles = []

    # Spawn vehicles
    for i in range(number_of_vehicles):
        blueprint = vehicle_blueprints[i]
        spawn_point = spawn_points[i]

        vehicle = world.try_spawn_actor(blueprint, spawn_point)

        if vehicle is not None:
            vehicles.append(vehicle)

            print(
                f"Spawned vehicle {i + 1}: "
                f"{vehicle.type_id} | ID: {vehicle.id}"
            )
        else:
            print(f"Failed to spawn vehicle {i + 1}")

    print(f"\nTotal vehicles spawned: {len(vehicles)}")


if __name__ == "__main__":
    main()