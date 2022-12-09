
def txt_to_lines():
    with open('day9/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def parse(lines):

    # What if I just kept a list of x,y coords the tail touched?
    tails = set([(0, 0)])
    rope_coords = [(0, 0) for _ in range(10)]
    for line in lines:
        direction, n = line.split(' ')
        for _ in range(int(n)):
            # breakpoint()
            rope_coords = move_ropes_one(direction, rope_coords)
            tails.add(rope_coords[-1])

    return tails


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
    # They are diagonal but not touching
    # h: (2, 1) t: (0, 0) -> (1, 1)
    # h: (5, 2) t: (4, 0) -> (5, 1)
    # Up and to the right

    # breakpoint()
    if up and right:
        return (tx+1, ty+1)

    # Up and to the left
    if up and left:
        return (tx-1, ty+1)

    # down and to the left
    if down and left:
        return (tx-1, ty-1)

    # down and to the right
    if down and right:
        return (tx+1, ty-1)


def move_one(direction, head_coords, tail_coords):
    # Returns new tail_coords and head_coords
    # ..##..
    # ...##.
    # .####.
    # ....#.
    # s###.. X (3, 0) -> (4,1) This is touching. (3, 0) -> (5,1) not touching
    # Y 
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
        new_tail_coords = move_tail(new_head_coords, tail_coords)
    return new_head_coords, new_tail_coords


def move_ropes_one(direction, rope_coords):
    # Returns new tail_coords and head_coords
    # ..##..
    # ...##.
    # .####.
    # ....#.
    # s###.. X (3, 0) -> (4,1) This is touching. (3, 0) -> (5,1) not touching
    # Y

    # Skip over pairs of coords
    # index 0 is the head
    new_coords = rope_coords.copy()

    # breakpoint()
    h, t = move_one(direction, rope_coords[0], rope_coords[1])

    new_coords[0] = h
    new_coords[1] = t

    # Now respond for each one after
    # breakpoint()
    for i in range(1, len(rope_coords) - 1):
        next = new_coords[i]
        tail = new_coords[i+1]

        nt = tail
        if not touching(next, tail):
            # Move tail to where the head used to be.
            nt = move_tail(next, tail)
        new_coords[i+1] = nt
    return new_coords
        

lines = txt_to_lines()
res = parse(lines)
print(len(res))
