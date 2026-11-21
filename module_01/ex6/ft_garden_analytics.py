class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height: float
        self._age: int
        self.set_height(height, initial_set=True)
        self.set_age(age, initial_set=True)
        self._calls = self.Calls()
        print("Created:", end=' ')
        self.show()

    class Calls():
        def __init__(self) -> None:
            self._call_count = {
                "grow": 0,
                "age": 0,
                "show": 0,
            }

        def increment_call_count(self, func: str) -> None:
            self._call_count[func] += 1

    def get_calls(self) -> dict[str, int]:
        return self._calls._call_count

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")
        self._calls.increment_call_count("show")

    def grow(self, growth: float) -> None:
        self._height = self._height + growth
        self._calls.increment_call_count("grow")

    def age(self, days: int) -> None:
        self._age += days
        self._calls.increment_call_count("age")

    def simulate_one_week(self, growth_rate: float) -> None:
        self.age(7)
        initial_height = self._height
        for day in range(1, 8):
            self.grow(growth_rate)
            print(f"=== Day {day} ===")
            self.show()
        print(f"Growth this week: {round(self._height - initial_height, 1)}")

    def set_height(self, height: float, initial_set: bool = False) -> None:
        if height < 0:
            if initial_set:
                self._height = 0
                print(f"{self.name}: Error, height can't be negative",
                      "\nHeight set to 0")
            else:
                print(f"{self.name}: Error, height can't be negative",
                      "\nHeight update rejected")
        else:
            self._height = height
            if (not initial_set):
                print(f"Height updated: {self._height}cm")

    def set_age(self, age: int, initial_set: bool = False) -> None:
        if age < 0:
            if initial_set:
                self._age = 0
                print(f"{self.name}: Error, age can't be negative",
                      "\nAge set to 0")
            else:
                print(f"{self.name}: Error, age can't be negative",
                      "\nAge update rejected")
        else:
            self._age = age
            if (not initial_set):
                print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def is_older_than_one_year(age: float) -> None:
        print(f"Is {age} days older than a year? ->", end=' ')
        if age > 365.25:
            print("True")
        else:
            print("False")

    @classmethod
    def create_anon_plant(cls) -> Plant:
        anon_plant = cls("Uknown plant", 0, 0)
        return anon_plant


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 colour: str, blooming: bool = False) -> None:
        self.colour = colour
        self.blooming = blooming
        super().__init__(name, height, age)

    def bloom(self) -> None:
        self.blooming = True
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Colour: {self.colour}")
        if self.blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    class Calls(Plant.Calls):
        def __init__(self) -> None:
            super().__init__()
            self._call_count["shade"] = 0

    def produce_shade(self) -> None:
        print(f"Tree {self.name} has produced a shade",
              f"of {self._height}cm long and {self.trunk_diameter}cm wide.")
        self._calls.increment_call_count("shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int = 0) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, height, age)

    def age(self, days):
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}",
              f"\n Nutritional value: {self.nutritional_value}")

    def simulate_growth(self, days: int, growth_rate: float) -> None:
        self.age(days)
        for day in range(days):
            self.grow(growth_rate)
            day += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 colour: str, seeds: int, blooming: bool = False) -> None:
        self.seeds = seeds
        super().__init__(name, height, age, colour, blooming)

    def show(self) -> None:
        super().show()
        print(" Seed count:", end=' ')
        if self.blooming:
            print(f"{self.seeds}")
        else:
            print("0")


def show_stats(plant: Plant) -> None:
    stats_dict = plant.get_calls()
    print("Stats:", end=' | ')
    for key in stats_dict:
        print(f"{stats_dict[key]} {key}", end=' | ')
    print()


if __name__ == "__main__":
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    Plant.is_older_than_one_year(30)
    Plant.is_older_than_one_year(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    print("[statistics for Rose]")
    show_stats(rose)
    print("[asking the rose to bloom]")
    rose.grow(8)
    rose.bloom()
    print("[statistics for Rose]")
    show_stats(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    print("[statistics for Oak]")
    show_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    show_stats(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", 42)
    print("[make sunflower grow, age and bloom]")
    sunflower.age(20)
    sunflower.grow(30)
    sunflower.bloom()
    print("[statistics for Sunflower]")
    show_stats(sunflower)
    print("\n=== Anonymous")
    anon = Plant.create_anon_plant()
    print("[statistics for Unknown plant]")
    show_stats(anon)
