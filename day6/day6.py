
def txt_to_lines():
    with open('day6/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def sn(line, n):
    last_n_chars = ''
    for i, char in enumerate(line):
        if char in last_n_chars:
            # Not unique, go back to last occurrence of this letter
            start = last_n_chars.index(char)+1
            last_n_chars = last_n_chars[start:] + char
        elif len(last_n_chars) < n:
            last_n_chars += char
        if len(last_n_chars) == n:
            return i + 1


print(sn(txt_to_lines()[0], 4))
print(sn(txt_to_lines()[0], 14))


# from collections import deque


# def s1(datastream):
#     window = deque(maxlen=4)
#     for index, char in enumerate(datastream):
#         window.append(char)
#         if len(set(window)) == 4:
#             return index + 1
