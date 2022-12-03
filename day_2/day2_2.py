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


def sn(lines):
    score = 0
    for line in lines:
        left, outcome = line.split()
        lv = values[left]
        result = 0
        if outcome == 'Y':
            result = lv
        elif outcome == 'X':
            result = 6
        score += result + ri

    return score