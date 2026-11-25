class GardenError(Exception):
    def __init__(self, *args, name: str = "garden") -> None:
        self.name = name
        args = self.get_context(args)
        super().__init__(*args)

    def get_context(self, args: tuple) -> tuple:
        if not args:
            args = (f"Unknown {self.name} error",)
        return args


class PlantError(GardenError):
    def __init__(self, *args) -> None:
        self.name = "plant"
        super().__init__(name=self.name, *args)


def water_plant(plant_name: str) -> str:
    if plant_name == plant_name.capitalize():
        return ("[OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    plants = ["Tomato", "Lettuce", "Carrots"]
    try:
        print(f"Watering {plants[0]}: {water_plant(plants[0])}")
        print(f"Watering {plants[1]}: {water_plant(plants[1])}")
        print(f"Watering {plants[2]}: {water_plant(plants[2])}")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")
    print("Testing invalid plants...")
    print("Opening watering system")
    plants = ["Tomato", "lettuce", "Carrots"]
    try:
        print(f"Watering {plants[0]}: {water_plant(plants[0])}")
        print(f"Watering {plants[1]}: {water_plant(plants[1])}")
        print(f"Watering {plants[2]}: {water_plant(plants[2])}")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n",
              ".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
