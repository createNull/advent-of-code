def path(data):
    x = 0
    y = 0
    points = []
    for elem in data:
        direction = elem[0]
        length = int(elem[1:])

        for _ in range(0, length):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            points.append((x, y))

    return points


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open('input.txt') as f:
    wire1 = f.readline().rstrip('\n').split(',')
    wire2 = f.readline().rstrip('\n').split(',')

path1 = path(wire1)
path2 = path(wire2)

intersections = list(set(path1).intersection(set(path2)))

distances = [manhattan_dist(p1, (0, 0)) for p1 in intersections]
total_steps = [path1.index(p) + 1 + path2.index(p) + 1 for p in intersections]

print('Part 1:', min(distances))
print('Part 2:', min(total_steps))
