def txt_to_lines():
    with open('day5/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def append_or_add(lst, idx, element):
    if len(lst) <= idx:
        lst.append([element])
    else:
        lst[idx].append(element)
    return lst


def parse(lines):
    ins_start = lines.index('')

    instructions = []
    for idx in range(ins_start + 1, len(lines)):
        line = lines[idx]
        ins_idx = idx - (ins_start + 1)
        for word in line.split(' '):
            if word.isnumeric():
                instructions = append_or_add(instructions, ins_idx, int(word))

    # Parse the matrix
    mlines = lines[:ins_start]
    mlines.reverse()
    last_idx = int(mlines[0].replace(' ', '')[-1])
    matrix = [[] for _ in range(last_idx)]

    for ml in mlines[1:]:
        # For each stack in the matrix, push the value onto the stack.
        stack_index = 1

        for i in range(last_idx):
            if ml[stack_index] != ' ':
                matrix[i].append(ml[stack_index])
            stack_index += 4
    return matrix, instructions


def move2(matrix, instruction):
    # move 2 from 7 to 2
    # [2, 7, 2]
    n = instruction[0]
    fromm = instruction[1] - 1
    to = instruction[2] - 1

    # remove the last n crates
    cutoff_idx = len(matrix[fromm]) - n
    to_move = matrix[fromm][cutoff_idx:]
    matrix[fromm] = matrix[fromm][:cutoff_idx]
    matrix[to] = matrix[to] + to_move
    return matrix


def move_all(matrix, instructions):
    # move 2 from 7 to 2
    # [[2, 7, 2]]
    for ins in instructions:
        matrix = move2(matrix, ins)
    return matrix


def sn(matrix):
    result = []
    for stack in matrix:
        # TODO, what if the stack is empty at the end?
        if len(stack) != 0:
            result.append(stack.pop())
    return ''.join(result)    


lines = txt_to_lines()
mat, ins = parse(lines)
matt = move_all(mat, ins)
print(sn(matt))

# [H] [Q] [P] [L] [G] [V] [Z] [D] [B]
#     [S] [C]         [C]     [Q] [L]
# '    [C] [R] [Z]     [R]     [H] [Z]'
# '[H] [Q] [P] [L] [G] [V] [Z] [D] [B]'
# 0 at str[1]
#  + 4
# 1 at str[5]
# + 4
# 2 at str[9]
# + 4
# 3 at str[13]