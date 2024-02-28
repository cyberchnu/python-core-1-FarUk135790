def calculate_fuel(distance):
  # Type your code
  if distance <= 0:
    return 100
  else:
    fuel_needed = distance * 10
    if fuel_needed < 100:
      return 100
    else:
      return fuel_needed