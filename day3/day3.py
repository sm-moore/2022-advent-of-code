def txt_to_lines():
    with open('day3/input3.txt') as f:
        lines = f.read().splitlines()
    return lines


def priority_value(char):
    A_ = ord('A')
    a_ = ord('a')
    if char.isupper():
        return ord(char) - A_ + 27
    return ord(char) - a_ + 1


def sn(lines):
    priority = 0
    for line in lines:
        ls = [*line.strip()]

        half = int(len(ls)/2)
        left = ls[:half]
        right = ls[half:]

        # find common character between left and right
        for char in left:
            if char in right:
                priority += priority_value(char)
                break
    return priority


def find_pri_between_3_elves(elves):
    # Find the common chars between the first two elves
    common = []
    for char in elves[0]:
        if char in elves[1]:
            common.append(char)

    # which of these chars does elf 3 have?
    for char in common:
        if char in elves[2]:
            return priority_value(char)
    return -1000


def sn_2(lines):
    priority = 0
    idx = 0
    while True:
        # grab the next 3 lines
        elves = lines[idx:idx+3]

        # Find the common char between the three elves
        priority += find_pri_between_3_elves(elves)

        if idx+3 >= len(lines):
            break

        idx += 3

    return priority


lines = txt_to_lines()
print(sn(lines))
print(sn_2(lines))
