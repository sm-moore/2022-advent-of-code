def txt_to_lines():
    with open('day_2/input2.txt') as f:
        lines = f.read().splitlines()
    assert len(lines) == 2500
    return lines


values = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3  # Scissors
}
# #  Wins
# 3 : 1
# 1 : 2
# 2 : 3


def win(left, right):
    return (left == 3 and right == 1) or (left == 1 and right == 2) or (left == 2 and right == 3)


def sn(lines):
    score = 0
    for line in lines:
        l, r = line.split()
        li = values[l]
        ri = values[r]
        result = 0
        if li == ri:
            result = 3
        elif win(li, ri):
            result = 6
        score += result + ri

    return score


lines = txt_to_lines()
print(sn(lines))
