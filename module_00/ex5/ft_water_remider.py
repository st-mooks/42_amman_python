def ft_water_reminder():
    last_watered = int(input("Days since last watering: "))
    if last_watered > 2:
        print("Water plants!")
    else:
        print("Plants are fine")
