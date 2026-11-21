class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        print("Created:", end=' ')
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")

    def grow(self, growth: float) -> None:
        self.height = round(self.height + growth, 1)

    def age(self, days) -> None:
        self._age += days

    def simulate_one_week(self, growth_rate: float) -> None:
        self.age(7)
        initial_height = self.height
        for day in range(1, 8):
            self.grow(growth_rate)
            print(f"=== Day {day} ===")
            self.show()
        print(f"Growth this week: {round(self.height - initial_height, 1)}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
