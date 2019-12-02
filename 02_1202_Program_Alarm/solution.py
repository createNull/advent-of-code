from operator import add, mul


def get_result(noun=None, verb=None, output=None):
    with open('input.txt', 'r') as file:
        input_list = [int(elem) for elem in file.read().split(',')]
        if output:
            for noun in range(100):
                for verb in range(100):
                    temp = get_output(input_list, noun, verb)
                    if temp == output:
                        return 100 * noun + verb
        output = get_output(input_list, noun, verb)
        return output


def get_output(input_list, noun, verb):
    input_list[1], input_list[2] = noun, verb
    output_list = input_list[:]
    i = 0
    while i < len(output_list):
        instruction = output_list[i:i + 4]
        if instruction[0] == 99:
            break
        opcode, noun, verb, output_pos = instruction
        if opcode == 1:
            output_list[output_pos] = add(
                output_list[noun], output_list[verb])
        elif opcode == 2:
            output_list[output_pos] = mul(
                output_list[noun], output_list[verb])
        else:
            return "Opcode doesn't have a valid value."
        i += 4
    return output_list[0]


print(get_result(12, 2))
print(get_result(output=19690720))
