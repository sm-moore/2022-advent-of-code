
def txt_to_lines():
    with open('day6/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def sn(line, n):
    last_n_chars = ''
    for i, char in enumerate(line):
        if char in last_n_chars:
            # Not unique, go back to last occurrence of this letter
            last_n_chars = last_n_chars[last_n_chars.index(char)+1:] + char
        elif len(last_n_chars) < n:
            last_n_chars += char
        if len(last_n_chars) == n:
            return i + 1


print(sn(txt_to_lines()[0], 4))
print(sn(txt_to_lines()[0], 14))
