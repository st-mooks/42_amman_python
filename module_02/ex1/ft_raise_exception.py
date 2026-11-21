class ExtremeTempError(ValueError):
    def __init__(self, temp: int, *args: object) -> None:
        self.temp = temp
        context = self.set_context()
        super().__init__(context, *args)

    def set_context(self) -> str:
        if self.temp < 0:
            return f"{self.temp}°C is too cold for plants (min 0°C)"
        else:
            return f"{self.temp}°C is too hot for plants (max 100°C)"


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0 or temp > 40:
        raise ExtremeTempError(temp)
    return temp


def test_temprature() -> None:
    temp_str = input("Enter temperature to test: ")
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ExtremeTempError as e:
        print(f"Caught input_temperature error: {e.args[0]}")
    except ValueError as e:
        print(f"Caught input_temperature error: {e.args[0]}")


if __name__ == "__main__":
    print("=== Gareden Temperature ===\n")
    test_temprature()
