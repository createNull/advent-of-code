from math import gcd, atan2


with open('input.txt') as f:
    puzzle_input = f.read().splitlines()


def raycast(station, asteroids):
    hits = set()

    for asteroid in asteroids:
        if asteroid != station:
            dv, dh = asteroid[0] - station[0], asteroid[1] - station[1]
            g = abs(gcd(dv, dh))
            red = (dv // g, dh // g)
            hits.add(red)
    return hits


def get_asteroid_field(array):
    positions = set()

    for i, row in enumerate(array):
        for j, symbol in enumerate(row):
            if symbol == '#':
                positions.add((j, i))

    return positions


def get_result(array, option):
    asteroid_field = get_asteroid_field(array)
    station_candidates = []

    for candidate in asteroid_field:
        in_sight = raycast(candidate, asteroid_field)
        station_candidates.append((len(in_sight), candidate, in_sight))
    station_candidates.sort(reverse=True)
    result, station_coordinates, in_sight = station_candidates[0]

    if option == 1:
        return result

    elif option == 2:
        destroyed = [(atan2(dh, dv), (dv, dh)) for dv, dh in in_sight]
        destroyed.sort(reverse=True)
        dv, dh = destroyed[200-1][1]
        v, h = station_coordinates[0] + dv, station_coordinates[1] + dh
        while (v, h) not in asteroid_field:
            v, h = v + dv, h + dh

        return h * 100 + v


print('Part 1:', get_result(puzzle_input, 1))
print('Part 2:', get_result(puzzle_input, 2))
