def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    day = 1
    while day <= days:
        print(f"Day {day}")
        day += 1
    print("Harvest  time!")


def ft_count_harvest_recursive(days: int = -1):
    is_main_loop = False
    if days == -1:
        days = int(input("Days until harvest: "))
        is_main_loop = True
    if days > 1:
        ft_count_harvest_recursive(days - 1)
    print(f"Day {days}")
    if is_main_loop:
        print("Harvest time!")
