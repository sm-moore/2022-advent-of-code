def txt_to_lines():
    with open('day4/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def sn(lines):
    counter = 0
    for line in lines:
        left, right = line.split(',')

        ls, le = map(int, left.split('-'))
        rs, re = map(int, right.split('-'))

        # Right inside left or left inside right
        if (rs >= ls and re <= le) or (ls >= rs and le <= re):
            counter += 1

    return counter


def sn2(lines):
    counter = 0
    for line in lines:
        left, right = line.split(',')

        ls, le = map(int, left.split('-'))
        rs, re = map(int, right.split('-'))

        # overlap
        if (rs <= le and rs >= ls) or (ls >= rs and ls <= re):
            counter += 1

    return counter


lines = txt_to_lines()
print(sn(lines))
print(sn2(lines))
