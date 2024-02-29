def calculate_fuel(distance):
    if not isinstance(distance, (int, float)) or distance <= 0:
        return "100"
    fuel = distance * 2
    fuel = max(fuel, 100)
    return fuel
distance = 100
result = calculate_fuel(distance)
print(f"Обсяг палива для відстані {distance} км: {result} літрів")