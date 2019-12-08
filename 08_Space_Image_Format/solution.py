width, height = 25, 6

with open('input.txt') as file:
    input_str = file.read().rstrip('\n')


def string_divide(string, div):
    arr = []
    for i in range(0, len(string), div):
        arr.append(string[i:i+div])
    return arr


def get_result(string, option):
    layers = string_divide(string, width * height)

    if option == 1:
        min_count, i = min((layer.count('0'), i)
                           for i, layer in enumerate(layers))
        return layers[i].count('1') * layers[i].count('2')

    elif option == 2:
        image = []
        for i in range(width * height):
            if i % width == 0 and i != 0:
                image.append('\n')
            for j in range(i, len(string), width * height):
                if string[j] != '2':
                    image.append(string[j])
                    break
        return ''.join(image).replace('1', '█')


print('Part 1:', get_result(input_str, 1))
print(f'Part 2: \n{get_result(input_str, 2)}')
