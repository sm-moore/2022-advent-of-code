import day2_2 as sut


def test_sn2():
    lines = ['A Y', 'B X', 'C Z']
    score = sut.sn2(lines)
    assert score == 12


def test_day2_loss():
    lines = ['B X']
    score = sut.sn2(lines)
    assert score == 1


def test_day2_loss_loop():
    lines = ['A X']
    score = sut.sn2(lines)
    assert score == 3


def test_day2_win():
    lines = ['A Z']
    score = sut.sn2(lines)
    assert score == 8


def test_day2_win_loop():
    lines = ['C Z']
    score = sut.sn2(lines)
    assert score == 7


def test_day2_draw():
    lines = ['A Y']
    score = sut.sn2(lines)
    assert score == 4
