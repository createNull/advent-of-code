from itertools import permutations


with open('input.txt') as f:
    puzzle_input = list(map(int, f.read().split(',')))


class IntcodeComputer:

    def __init__(self, array, phase_setting=None):
        self.array = array.copy()
        self.inputs = []
        self.pos = 0
        if phase_setting != None:
            self.inputs.append(phase_setting)

    def get_param(self, mode, param_no):
        if mode == '1':
            return self.pos + param_no
        else:
            return self.array[self.pos + param_no]

    def get_output_signal(self, signal=None):
        if signal != None:
            self.inputs.append(signal)

        while self.pos < len(self.array):
            code = str(self.array[self.pos]).zfill(5)

            opcode, mode1, mode2, mode3 = int(
                code[-2:]), code[2], code[1], code[0]

            if opcode == 99:
                break
            elif opcode in (3, 4):
                param1 = self.get_param(mode1, 1)
            elif opcode in (5, 6):
                param1 = self.get_param(mode1, 1)
                param2 = self.get_param(mode2, 2)
            else:
                param1 = self.get_param(mode1, 1)
                param2 = self.get_param(mode2, 2)
                param3 = self.get_param(mode3, 3)

            if opcode == 1:
                self.array[param3] = self.array[param1] + self.array[param2]
                self.pos += 4
            elif opcode == 2:
                self.array[param3] = self.array[param1] * self.array[param2]
                self.pos += 4
            elif opcode == 3:
                self.array[param1] = self.inputs.pop(0)
                self.pos += 2
            elif opcode == 4:
                self.pos += 2
                return self.array[param1]
            elif opcode == 5:
                if self.array[param1] != 0:
                    self.pos = self.array[param2]
                else:
                    self.pos += 3
            elif opcode == 6:
                if self.array[param1] == 0:
                    self.pos = self.array[param2]
                else:
                    self.pos += 3
            elif opcode == 7:
                if self.array[param1] < self.array[param2]:
                    self.array[param3] = 1
                else:
                    self.array[param3] = 0
                self.pos += 4
            elif opcode == 8:
                if self.array[param1] == self.array[param2]:
                    self.array[param3] = 1
                else:
                    self.array[param3] = 0
                self.pos += 4
            else:
                return f"Opcode {opcode} doesn't have a valid value."


def get_result(array, option):
    total = []
    if option == 1:
        for phase_setting_config in permutations(range(5)):
            amplifiers = [IntcodeComputer(array, phase_setting)
                          for phase_setting in phase_setting_config]

            previous_amplifier_output = 0

            for amplifier in amplifiers:
                previous_amplifier_output = amplifier.get_output_signal(
                    previous_amplifier_output)
                total.append(previous_amplifier_output)

    elif option == 2:
        for phase_setting_config in permutations(range(5, 10)):
            amplifiers = [IntcodeComputer(array, phase_setting)
                          for phase_setting in phase_setting_config]

            previous_amplifier_output = 0

            while True:
                for amplifier in amplifiers:
                    previous_amplifier_output = amplifier.get_output_signal(
                        previous_amplifier_output)

                if previous_amplifier_output:
                    total.append(previous_amplifier_output)
                else:
                    break
    return max(total)


print('Part 1:', get_result(puzzle_input, 1))
print('Part 2:', get_result(puzzle_input, 2))
