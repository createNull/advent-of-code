with open('input.txt') as f:
    puzzle_input = list(map(int, f.read().split(',')))


def get_result(array, noun=None, verb=None, output=None):
    if output:
        for noun in range(100):
            for verb in range(100):
                temp = get_output(array.copy(), noun, verb)
                if temp == output:
                    return 100 * noun + verb
    output = get_output(array.copy(), noun, verb)
    return output


def get_output(array, noun, verb):
    array[1], array[2] = noun, verb

    i = 0
    while i < len(array):
        opcode = array[i]
        noun, verb, output_pos = array[i + 1], array[i + 2], array[i + 3]

        if opcode == 99:
            break
        elif opcode == 1:
            array[output_pos] = array[noun] + array[verb]
        elif opcode == 2:
            array[output_pos] = array[noun] * array[verb]
        else:
            return "Opcode doesn't have a valid value."
        i += 4

    return array[0]


print('Part 1: ', get_result(puzzle_input, noun=12, verb=2))
print('Part 2: ', get_result(puzzle_input, output=19690720))
