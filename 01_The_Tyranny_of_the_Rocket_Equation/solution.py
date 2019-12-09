from functools import reduce


with open('input.txt') as f:
    puzzle_input = list(map(int, f.read().splitlines()))


def required_fuel(mass):
    return int(mass / 3) - 2


def mass_fuel(mass):
    fuel = required_fuel(mass)
    return fuel + mass_fuel(fuel) if fuel >= 0 else 0


def calc_total_fuel(array, option):
    def accumulator(total, module_mass):
        fuel_needed = required_fuel(module_mass)
        if option == 2:
            fuel_needed = mass_fuel(module_mass)
        return total + fuel_needed
    return reduce(accumulator, array, 0)


print('Part 1:', calc_total_fuel(puzzle_input, 1))
print('Part 2:', calc_total_fuel(puzzle_input, 2))
