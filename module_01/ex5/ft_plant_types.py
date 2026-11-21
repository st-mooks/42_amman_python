class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height: float
        self._age: int
        self.set_height(height, initial_set=True)
        self.set_age(age, initial_set=True)
        print("Created:", end=' ')
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, growth: float) -> None:
        self._height = round(self._height + growth, 1)

    def age(self, days: int) -> None:
        self._age += days

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

    def produce_shade(self) -> None:
        print(f"Tree {self.name} has produced a shade",
              f"of {self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int = 0) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, height, age)

    def age(self, days) -> None:
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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    print("[asking the rose to bloom]")
    rose.bloom()
    print("\n===Tree")
    oak = Tree("Oak", 200, 365, 5)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n===Vegetables")
    tomato = Vegetable("Tomato", 5, 10, "April")
    print("[make tomato grow and age for 20 days]")
    tomato.simulate_growth(20, 2.1)
    tomato.show()
