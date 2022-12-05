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
    # The index where the instructions start
    ins_start = lines.index('')

    # Parse the instructions into a 2D array, each instruction = 1 array.
    instructions = []
    for line in lines[ins_start + 1:]:
        words = line.split(' ')
        instructions.append(list(map(int, [words[1], words[3], words[5]])))

    # Parse the matrix
    matrix_lines = lines[:ins_start]
    # Start from the bottom, so each crate can be pushed onto the stack
    matrix_lines.reverse()
    crate_count = int(matrix_lines[0].replace(' ', '')[-1])

    matrix = [[] for _ in range(crate_count)]
    for ml in matrix_lines[1:]:
        # For each stack in the matrix, push the value onto the stack.
        stack_index = 1

        for i in range(crate_count):
            if ml[stack_index] != ' ':
                matrix[i].append(ml[stack_index])
            stack_index += 4
    return matrix, instructions


def move_one(matrix, fromm, to):
    element = matrix[fromm-1].pop()
    matrix[to-1].append(element)
    return matrix


def move(matrix, instruction):
    # move 2 from 7 to 2
    # [2, 7, 2]
    for _ in range(instruction[0]):
        matrix = move_one(matrix, instruction[1], instruction[2])
    return matrix


def move_all(matrix, instructions):
    # move 2 from 7 to 2
    # [[2, 7, 2]]
    for ins in instructions:
        matrix = move(matrix, ins)
    return matrix


def sn(matrix):
    result = []
    for stack in matrix:
        # what if the stack is empty at the end?
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