puzzle_input = '353096-843212'


def has_sorted_digits(element):
    return ''.join(sorted(element)) == element


def has_equal_adjacent_digits(element):
    if has_sorted_digits(element):
        return len(set(element)) <= len(element) - 1


def has_two_equal_adjacent_digits(element):
    if has_sorted_digits(element):
        for digit in set(element):
            if element.count(digit) == 2:
                return True
        # return 2 in Counter(element).values()  ## short version


def get_result(interval, option):
    up, low = list(map(int, puzzle_input.split('-')))
    # upper limit and lower limit of the interval
    count = 0
    for num in range(up, low):
        num_str = str(num)

        if option == 1 and has_equal_adjacent_digits(num_str):
            count += 1
        elif option == 2 and has_two_equal_adjacent_digits(num_str):
            count += 1

    return count


print('Part 1: ', get_result(puzzle_input, 1))
print('Part 2: ', get_result(puzzle_input, 2))
