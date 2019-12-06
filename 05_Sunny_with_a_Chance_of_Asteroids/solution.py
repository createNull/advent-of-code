with open('input.txt') as f:
    input_array = list(map(int, f.read().split(',')))


def get_result(array, id):
    i = 0

    while i < len(array):
        # Read most-right 2 digits
        # First, fill 0 to make code 5 digits
        code = str(array[i]).zfill(5)
        opcode = code[-2:]

        if opcode == "99":
            break

        mode_1, mode_2, mode_3 = code[2], code[1], code[0]

        first_parameter = array[i + 1] if mode_1 == "0" else i + 1
        second_parameter = array[i + 2] if mode_2 == "0" else i + 2
        third_parameter = array[i + 3] if mode_3 == "0" else i + 3

        # Add opcode (3 arguments)
        if opcode == "01":
            array[third_parameter] = array[first_parameter] + \
                array[second_parameter]
            i += 4

        # Multiple opcode (3 arguments)
        elif opcode == "02":
            array[third_parameter] = array[first_parameter] * \
                array[second_parameter]
            i += 4

        # Input opcode (1 argument)
        elif opcode == "03":
            array[first_parameter] = id
            i += 2

        # Output opcode (1 argument)
        elif opcode == "04":
            output_value = array[first_parameter]
            i += 2

        # jump-if-true (2 arguments)
        elif opcode == "05":
            if array[first_parameter] != 0:
                i = array[second_parameter]
            else:
                i += 3

        # jump-if-false (2 arguments)
        elif opcode == "06":
            if array[first_parameter] == 0:
                i = array[second_parameter]
            else:
                i += 3

        # less than (3 arguments)
        elif opcode == "07":
            array[third_parameter] = 1 if array[first_parameter] < array[second_parameter] else 0
            i += 4

        # equals (3 arguments)
        elif opcode == "08":
            array[third_parameter] = 1 if array[first_parameter] == array[second_parameter] else 0
            i += 4

        else:
            return "Opcode doesn't have a valid value."

    return output_value


print('Part 1:', get_result(input_array.copy(), 1))
print('Part 2:', get_result(input_array.copy(), 5))
