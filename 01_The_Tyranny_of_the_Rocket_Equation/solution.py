from functools import reduce


with open('input.txt') as f:
    input_array = list(map(int, f.read().splitlines()))


def required_fuel(mass):
    return int(mass / 3) - 2


def mass_fuel(mass):
    fuel = required_fuel(mass)
    if fuel >= 0:
        return fuel + mass_fuel(fuel)
    return 0


def calc_total_fuel(array, option):
    def accumulator(total, module_mass):
        fuel_needed = required_fuel(module_mass)
        if option == 2:
            fuel_needed = mass_fuel(module_mass)
        return total + fuel_needed
    return reduce(accumulator, array, 0)


print('Part 1:', calc_total_fuel(input_array, 1))
print('Part 2:', calc_total_fuel(input_array, 2))
