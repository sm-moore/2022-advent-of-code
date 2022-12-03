def highest_calories_carried(input_matrix):
    # Could use flatten
    highest_so_far = 0

    for elf in input_matrix:
        calories = sum(elf)
        if calories > highest_so_far:
            highest_so_far = calories

    return highest_so_far


def n_highest_calories_carried(input_matrix, n):
    highest_so_far = []

    for elf in input_matrix:
        calories = sum(elf)
        if len(highest_so_far) < n:
            highest_so_far.append(calories)
        else:
            if calories > min(highest_so_far):
                # Find the index of the min and replace it, could use map here.
                idx = highest_so_far.index(min(highest_so_far))
                highest_so_far[idx] = calories
                # for i in range(len(highest_so_far)):
                #     if highest_so_far[i] == min(highest_so_far):
                #         highest_so_far[i] = calories

    return highest_so_far


def lines_to_matrix(lines):
    matrix = []
    curr_elf_idx = 0
    for line in lines:
        if line == '':
            # Move on to the next elf
            curr_elf_idx += 1
        else:
            if len(matrix) <= curr_elf_idx:
                matrix.append([])
            matrix[curr_elf_idx].append(int(line))
    return matrix


def txt_to_lines():
    with open('day_1/input1.txt') as f:
        lines = f.read().splitlines()
    return lines


lines = txt_to_lines()
matrix = lines_to_matrix(lines)
# highest_cals = highest_calories_carried(matrix)
# print(n_highest_calories_carried(matrix, 3))
# print(sum(n_highest_calories_carried(matrix, 3)))


def sn(lines):
    # Create an array of aggregated values and then sort them.
    aggregates = []
    idx = 0
    for line in lines:
        if line == '':
            # Move on to the next elf
            idx += 1
        else:
            if len(aggregates) <= idx:
                aggregates.append(0)
            aggregates[idx] = aggregates[idx] + int(line)
    return sorted(aggregates, reverse=True)


print(sn(lines)[0])
print(sum(sn(lines)[:3]))
