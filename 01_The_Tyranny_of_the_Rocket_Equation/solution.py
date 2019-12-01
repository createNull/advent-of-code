def get_fuel(mass):
    return int(mass / 3) - 2

def get_additional_fuel(fuel):
    total = 0
    while fuel:
        fuel = get_fuel(fuel)
        if fuel < 0:
            break
        total += fuel
    return total

def get_total_fuel():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            try:
                num = int(line)
                fuel = get_additional_fuel(num)
                total += fuel
            except ValueError:
                print(f'{line} is not a number')
    return total
