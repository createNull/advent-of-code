problem_input = '353096-843212'


def get_result(interval, option):
    up, low = interval.split('-')
    # upper limit and lower limit of the interval
    count = 0
    for num in range(int(up), int(low)):
        list_num = list(str(num))
        done = False
        if sorted(list_num) == list_num:
            for i in range(len(list_num) - 1):
                if list_num[i] == list_num[i + 1]:
                    if option == 'part1':
                        done = True
                    elif option == 'part2':
                        adjacent = list_num[i]
                        if list_num.count(adjacent) == 2:
                            done = True
        if done:
            count += 1
    return count


print('Part 1: ', get_result(problem_input, 'part1'))
print('Part 2: ', get_result(problem_input, 'part2'))
