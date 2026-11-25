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


class WaterError(GardenError):
    def __init__(self, *args) -> None:
        self.name = "water"
        super().__init__(name=self.name, *args)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    plant_error = PlantError("The tomato plant is wiliting!")
    water_error = WaterError("Not enough water in the tank!")
    print("Testing PlantError...")
    try:
        raise plant_error
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        raise water_error
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        raise plant_error
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise water_error
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    print("Testing generic errors...")
    try:
        raise PlantError
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        raise WaterError
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    try:
        raise GardenError
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    print("All custom error types work correctly!")
