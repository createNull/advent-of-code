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
        _, fewest_zeros = min((layer.count('0'), layers[i])
                              for i, layer in enumerate(layers))
        return fewest_zeros.count('1') * fewest_zeros.count('2')

    elif option == 2:
        image = []
        for pixel in range(width * height):
            if pixel % width == 0:
                image.append('\n')
            for pos in range(pixel, len(string), width * height):
                if string[pos] != '2':
                    image.append(string[pos])
                    break
        return ''.join(image).replace('1', '█')


print('Part 1:', get_result(input_str, 1))
print('Part 2:', get_result(input_str, 2))
