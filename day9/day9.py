def txt_to_lines():
    with open('day9/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def parse(lines):
    # What if I just kept a list of x,y coords the tail touched?
    result = set([(0, 0)])
    head_coords = (0, 0)
    tail_coords = (0, 0)
    for line in lines:
        direction, n = line.split(' ')
        for _ in range(int(n)):
            head_coords, tail_coords = move_one(direction, head_coords, tail_coords)
            result.add(tail_coords)

    return result


def touching(tail_coords, new_head_coords):
    # (0, 0)
    # (1, 0)
    # Touching means the points are never more than one apart?
    # (2, 0)
    hx, hy = new_head_coords
    tx, ty = tail_coords

    if hx - tx > 1 or tx - hx > 1:
        return False
    if hy - ty > 1 or ty - hy > 1:
        return False
    return True


def move_one(direction, head_coords, tail_coords):
    # Returns new tail_coords and head_coords
    new_tail_coords = tail_coords
    match direction:
        case 'R':
            # (0, 0) -> (1, 0)
            new_head_coords = (head_coords[0] + 1, head_coords[1])
        case 'L':
            # (0, 0) -> (-1, 0)
            new_head_coords = (head_coords[0] - 1, head_coords[1])
        case 'U':
            # (0, 0) -> (0, 1)
            new_head_coords = (head_coords[0], head_coords[1] + 1)
        case 'D':
            # (0, 0) -> (0, -1)
            new_head_coords = (head_coords[0], head_coords[1] - 1)
        case _:
            print('Oops!')

    if not touching(tail_coords, new_head_coords):
        # Move tail to where the head used to be.
        # NOTE!!! THIS IS WRONG!!! UGH!!!
        new_tail_coords = head_coords
    return new_head_coords, new_tail_coords


lines = txt_to_lines()
res = parse(lines)
print(len(res))
