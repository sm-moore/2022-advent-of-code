# class Tree:
#     top = 0
#     left = 0
#     right = 0
#     bottom = 0

#     def __init__(self, left, top, right, bottom):
#         self.top = top
#         self.left = left
#         self.right = right
#         self.bottom = bottom

#     def __eq__(self, other):
#     """Overrides the default implementation"""
#     return other.top == self.top and other.left == self.left and 

def txt_to_lines():
    with open('day8/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def parse(lines):
    result = []
    for line in lines:
        result.append(list(map(int, [c for c in line])))
    return result


def is_on_edge(matrix, left_to_right_idx, top_to_bottom_idx):
    return left_to_right_idx == 0 or top_to_bottom_idx == 0 or \
        left_to_right_idx == len(matrix) - 1 or \
        top_to_bottom_idx == len(matrix[0]) - 1


def tree_is_visible(matrix, tree_coords):
    left_to_right_idx, top_to_bottom_idx = tree_coords
    
    # make sure coords passed in are not on the edge
    if is_on_edge(matrix, left_to_right_idx, top_to_bottom_idx):
        return True

    tree_val = matrix[left_to_right_idx][top_to_bottom_idx]

    tree_row = matrix[left_to_right_idx]
    tree_col = [row[top_to_bottom_idx] for row in matrix]
    # Look left to right first
    left_max = max(tree_row[:top_to_bottom_idx])
    right_max = max(tree_row[top_to_bottom_idx+1:])
    l_to_r = tree_val > left_max or tree_val > right_max

    # Top to bottom
    top_max = max(tree_col[:left_to_right_idx])
    bottom_max = max(tree_col[left_to_right_idx+1:])
    t_to_b = tree_val > top_max or tree_val > bottom_max

    return l_to_r or t_to_b


def sn(matrix):
    visible = 0
    for ri, row in enumerate(matrix):
        # [3, 0, 3],
        # [3, 5, 0],
        # [3, 5, 6]
        for ti, tree in enumerate(row):
            if tree_is_visible(matrix, (ri, ti)):
                visible += 1
    return visible


lines = txt_to_lines()
matrix = parse(lines)
print(sn(matrix))


def sight_dist(list, height):
    dist = 0
    for li in list:
        if height <= li:
            return dist + 1
        dist += 1
    return dist


def scenic_score(matrix, tree_coords):
    left_to_right_idx, top_to_bottom_idx = tree_coords

    # Trees on edge will be 0
    if is_on_edge(matrix, left_to_right_idx, top_to_bottom_idx):
        return 0

    tree_val = matrix[left_to_right_idx][top_to_bottom_idx]

    tree_row = matrix[left_to_right_idx]
    tree_col = [row[top_to_bottom_idx] for row in matrix]

    # Look left to right first
    left = tree_row[:top_to_bottom_idx].copy()
    left.reverse()

    left_dist = sight_dist(left, tree_val)
    right_dist = sight_dist(tree_row[top_to_bottom_idx+1:], tree_val)

    # Top to bottom
    top = tree_col[:left_to_right_idx]
    top.reverse()
    top_dist = sight_dist(top, tree_val)
    bottom_dist = sight_dist(tree_col[left_to_right_idx+1:], tree_val)

    return left_dist*right_dist*top_dist*bottom_dist


def sn2(matrix):
    scenic_scores = []
    for ri, row in enumerate(matrix):
        for ti, tree in enumerate(row):
            scenic_scores.append(scenic_score(matrix, (ri, ti)))
    return max(scenic_scores)


print(sn2(parse(lines)))
