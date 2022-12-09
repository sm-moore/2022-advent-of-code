import day9_2 as sut2

import day9 as sut

input = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2',
]


def test_parse():
    input = [
        'R 1'
    ]
    expected = set()
    expected.add((0, 0))
    assert sut.parse(input) == expected


def test_parse2():
    input = [
        'R 4'
    ]
    expected = set([(0, 0), (1, 0), (2, 0), (3, 0)])
    assert sut.parse(input) == expected


def test_parse3():
    r4 = [(0, 0), (1, 0), (2, 0), (3, 0)]
    u4 = [(4, 1), (4, 2), (4, 3)]
    l3 = [(3, 4), (2, 4)]
    d1 = []
    r4_ = [(3, 3), (4, 3)]
    d1_ = []
    l5 = [(4, 2), (3, 2), (2, 2), (1, 2)]
    r2 = []  # Whatever we've already touched these
    expected = set(r4 + u4 + l3 + d1 + r4_ + d1_ + l5 + r2)
    print(len(expected))
    assert sut.parse(input) == expected


def test_sn():
    assert len(sut.parse(input)) == 13


def test_move_tail():
    assert sut2.move_tail((0, 2), (0, 0)) == (0, 1)
    # h: (0, 2) t: (0, 4) -> (0, 3)
    assert sut2.move_tail((0, 2), (0, 4)) == (0, 3)
    # h: (2, 0) t: (0, 0) -> (1, 0)
    assert sut2.move_tail((2, 0), (0, 0)) == (1, 0)
    # h: (2, 0) t: (4, 0) -> (3, 0)
    assert sut2.move_tail((2, 0), (4, 0)) == (3, 0)
    # h: (5, 2) t: (4, 0) -> (5, 1)
    assert sut2.move_tail((5, 2), (4, 0)) == (5, 1)
    assert sut2.move_tail((5, 2), (4, 4)) == (5, 3)
    assert sut2.move_tail((0, 2), (0, 4)) == (0, 3)


def test_parse_2():
    input = [
        'R 5',
        'U 2'
        ]
    expected = set([(0, 0)])
    assert sut2.parse(input) == expected


def test_parse_3():
    input = [
        'R 5',
        'U 8'
        ]
    expected = set([(0, 0)])
    assert sut2.parse(input) == expected


def test_parse_2_2():
    input = [
        'R 5',
        'U 8',
        'L 8'
        ]
    expected = set([(0, 0), (1, 1), (2, 2), (1, 3)])
    assert sut2.parse(input) == expected


def test_sn_2():
    input = [
        'R 5',
        'U 8',
        'L 8',
        'D 3',
        'R 17',
        'D 10',
        'L 25',
        'U 20',
    ]
    assert len(sut2.parse(input)) == 36
