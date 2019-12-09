with open('input.txt') as f:
    puzzle_input = list(map(int, f.read().split(',')))


def get_result(array, id):
    i = 0
    while i < len(array):
        # Make code 5 digits
        code = str(array[i]).zfill(5)
        # Read last 2 digits
        opcode = int(code[-2:])

        if opcode == 99:
            break

        mode_1, mode_2, mode_3 = code[2], code[1], code[0]

        param1 = array[i + 1] if mode_1 == "0" else i + 1
        param2 = array[i + 2] if mode_2 == "0" else i + 2
        param3 = array[i + 3] if mode_3 == "0" else i + 3

        if opcode == 1:
            array[param3] = array[param1] + array[param2]
            i += 4
        elif opcode == 2:
            array[param3] = array[param1] * array[param2]
            i += 4
        elif opcode == 3:
            array[param1] = id
            i += 2
        elif opcode == 4:
            output_value = array[param1]
            i += 2
        elif opcode == 5:
            i = array[param2] if array[param1] != 0 else i + 3
        elif opcode == 6:
            i = array[param2] if array[param1] == 0 else i + 3
        elif opcode == 7:
            array[param3] = 1 if array[param1] < array[param2] else 0
            i += 4
        elif opcode == 8:
            array[param3] = 1 if array[param1] == array[param2] else 0
            i += 4
        else:
            return "Opcode doesn't have a valid value."

    return output_value


print('Part 1:', get_result(puzzle_input.copy(), 1))
print('Part 2:', get_result(puzzle_input.copy(), 5))
