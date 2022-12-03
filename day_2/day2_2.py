# X lose, Y draw, and Z win

def txt_to_lines():
    with open('day_2/input2.txt') as f:
        lines = f.read().splitlines()
    assert len(lines) == 2500
    return lines


values = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
}


def loose(left):
    if left == 1:
        return 3
    if left == 2:
        return 1
    return 2


def win(left):
    if left == 1:
        return 2
    if left == 2:
        return 3
    return 1


def sn2(lines):

    score = 0
    for line in lines:
        left, outcome = line.split()
        lv = values[left]
        result = lv + 3
        if outcome == 'Z':
            result = win(lv) + 6
        elif outcome == 'X':
            result = loose(lv)
        score += result

    return score


lines = txt_to_lines()
print(sn2(lines))
