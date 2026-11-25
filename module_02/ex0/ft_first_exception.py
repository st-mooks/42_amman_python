def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    temp_str = input("Enter temperature to test: ")
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print("Caught input_temperature error:",
              f"invalid literal for int() with base 10: '{temp_str}'")


if __name__ == "__main__":
    print("=== Gareden Temperature ===\n")
    test_temperature()
