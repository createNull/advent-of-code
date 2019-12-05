with open('input.txt') as f:
    input_array = list(map(int, f.read().split(',')))


def get_result(array, id):
    i = 0
    while i < len(array):
        cmd = format(array[i], '05d')
        op = int(cmd[3:])
        m1 = int(cmd[2])
        m2 = int(cmd[1])
        m3 = int(cmd[0])

        if op == 99:
            break
        elif op == 1:  # add
            i1 = array[i+1] if m1 == 0 else i+1
            i2 = array[i+2] if m2 == 0 else i+2
            i3 = array[i+3] if m3 == 0 else i+3
            array[i3] = array[i1] + array[i2]
            i += 4
        elif op == 2:  # multiply
            i1 = array[i+1] if m1 == 0 else i+1
            i2 = array[i+2] if m2 == 0 else i+2
            i3 = array[i+3] if m3 == 0 else i+3
            array[i3] = array[i1] * array[i2]
            i += 4
        elif op == 3:
            i1 = array[i+1] if m1 == 0 else i+1
            array[i1] = id  # input id
            i += 2
        elif op == 4:
            i1 = array[i+1] if m1 == 0 else i+1
            print(array[i1])
            i += 2
        elif op == 5:  # jump-if-true
            i1 = array[i+1] if m1 == 0 else i+1
            i2 = array[i+2] if m2 == 0 else i+2
            if array[i1] != 0:
                i = array[i2]
            else:
                i += 3
        elif op == 6:  # jump-if-false
            i1 = array[i+1] if m1 == 0 else i+1
            i2 = array[i+2] if m2 == 0 else i+2
            if array[i1] == 0:
                i = array[i2]
            else:
                i += 3
        elif op == 7:  # less than
            i1 = array[i+1] if m1 == 0 else i+1
            i2 = array[i+2] if m2 == 0 else i+2
            i3 = array[i+3] if m3 == 0 else i+3
            if array[i1] < array[i2]:
                array[i3] = 1
            else:
                array[i3] = 0
            i += 4
        elif op == 8:  # equals
            i1 = array[i+1] if m1 == 0 else i+1
            i2 = array[i+2] if m2 == 0 else i+2
            i3 = array[i+3] if m3 == 0 else i+3
            if array[i1] == array[i2]:
                array[i3] = 1
            else:
                array[i3] = 0
            i += 4
        else:
            i += 1
    return array[0]


print('Part 1:', get_result(input_array, 1))
print('Part 2:', get_result(input_array, 5))
