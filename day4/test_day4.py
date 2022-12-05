import day4 as sut


def test_sn():
    lines = ['6-6,4-6']
    assert 1 == sut.sn(lines)

    lines = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8',
    ]

    assert 2 == sut.sn(lines)


def test_edge_cases():
    lines = ['6-6,6-6']
    assert 1 == sut.sn(lines)

    lines = [
        '19-81,6-19'
    ]
    assert 0 == sut.sn(lines)


def test_sn2():
    lines = ['6-6,4-6']
    assert 1 == sut.sn2(lines)

    lines = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8',
    ]

    assert 4 == sut.sn2(lines)