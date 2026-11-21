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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print("\nCurrent state:", end=' ')
    rose.show()
