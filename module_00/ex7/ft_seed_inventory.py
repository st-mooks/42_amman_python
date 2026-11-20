def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    remaining = {
        "packets": f"{quantity} {unit} available",
        "grams": f"{quantity} {unit} total",
        "area": f"covers {quantity} square meters"
    }
    print(f"{seed_type.capitalize()} seeds: {remaining[unit]}")
