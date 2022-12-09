
def txt_to_lines():
    with open('day9/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def parse(lines, n_ropes):
    tails = set([(0, 0)])
    rope_coords = [(0, 0) for _ in range(n_ropes)]
    for line in lines:
        direction, n = line.split(' ')
        for _ in range(int(n)):
            rope_coords = move_ropes_one(direction, rope_coords)
            tails.add(rope_coords[-1])
    return tails


def touching(tail_coords, new_head_coords):
    # Touching means the points are never more than one apart
    hx, hy = new_head_coords
    tx, ty = tail_coords

    if abs(hx - tx) > 1:
        return False
    if abs(hy - ty) > 1:
        return False
    return True


def move_tail(head, tail):
    # If the head is ever two steps directly up, down, left, or right from the tail,
    # the tail must also move one step in that direction so it remains close enough
    # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves
    # one step diagonally to keep up:
    hx, hy = head
    tx, ty = tail

    up = hy > ty
    left = tx > hx
    right = hx > tx
    down = hy < ty
    if hx == tx:
        # Move up or down
        if up:
            # h: (0, 2) t: (0, 0) -> (0, 1)
            return (tx, ty+1)
        elif down:
            # h: (0, 2) t: (0, 4) -> (0, 3)
            return (tx, ty-1)
    elif hy == ty:
        # Move left or right
        if right:
            # h: (2, 0) t: (0, 0) -> (1, 0)
            return (tx+1, ty)
        elif left:
            return (tx-1, ty)

    # diagonals
    if up and right:
        return (tx+1, ty+1)
    if up and left:
        return (tx-1, ty+1)
    if down and left:
        return (tx-1, ty-1)
    if down and right:
        return (tx+1, ty-1)


def move_head(direction, head_coords):
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
    return new_head_coords


def move_ropes_one(direction, rope_coords):
    new_coords = rope_coords.copy()

    h = move_head(direction, rope_coords[0])

    new_coords[0] = h

    # Now respond for each rope after
    for i in range(len(rope_coords) - 1):
        next = new_coords[i]
        tail = new_coords[i+1]

        nt = tail
        if not touching(next, tail):
            # Move tail to where the head used to be.
            nt = move_tail(next, tail)
        new_coords[i+1] = nt
    return new_coords


lines = txt_to_lines()

res_1 = parse(lines, 2)
# 6391 is the correct answer to part 1
print(len(res_1) == 6391)

res_2 = parse(lines, 10)
# 2593 is the correct answer to part 2
print(len(res_2) == 2593)
