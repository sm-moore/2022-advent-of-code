def txt_to_lines():
    with open('day10/input.txt') as f:
        lines = f.read().splitlines()
    return lines


# addx V takes two cycles to complete. After two cycles, the X register is
# increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.
def parse(lines):
    cycle_number = 1
    x_register = 1

    # the cycle number multiplied by the value of the X register
    signal_strengths = {}

    for line in lines:
        if line == 'noop':
            signal_strengths[cycle_number] = cycle_number*x_register
            cycle_number += 1
        else:
            n = int(line.split(' ')[1])
            # two cycles
            signal_strengths[cycle_number] = cycle_number*x_register
            cycle_number += 1
            signal_strengths[cycle_number] = cycle_number*x_register
            cycle_number += 1
            x_register += n
    return signal_strengths


def parse2(lines):
    cycle_number = 1
    x_register = 1

    # the cycle number multiplied by the value of the X register
    signal_strengths = {}

    for line in lines:
        if line == 'noop':
            signal_strengths[cycle_number] = x_register
            cycle_number += 1
        else:
            n = int(line.split(' ')[1])
            # two cycles
            signal_strengths[cycle_number] = x_register
            cycle_number += 1
            signal_strengths[cycle_number] = x_register
            cycle_number += 1
            x_register += n
    return signal_strengths


def intersects(cycle, registers):
    x_register = registers[cycle+1]
    cc = cycle % 40
    if x_register - 1 == cc or x_register == cc or x_register + 1 == cc:
        return True

    return False


def sn(registers):
    drawing = [[], [], [], [], [], []]
    lenn = 40
    outer_idx = 0
    for cycle in range(0, 240):
        if cycle % lenn == 0 and cycle > 0:
            # breakpoint()
            outer_idx += 1

        if intersects(cycle, registers):
            drawing[outer_idx].append('#')
        else:
            drawing[outer_idx].append('.')
    final = ''
    for draw in drawing:
        final += '\n' + ''.join(draw)
    return final


signal_strengths = parse(txt_to_lines())
# 20th, 60th, 100th, 140th, 180th, and 220th
s = [signal_strengths[20],
     signal_strengths[60],
     signal_strengths[100],
     signal_strengths[140],
     signal_strengths[180],
     signal_strengths[220]]
print(sum(s))
# 13860 part 1 answer

regs = parse2(txt_to_lines())
# print(regs)
print(sn(regs))
# RZHFGJCB

