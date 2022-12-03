import day2 as sut


def test_day2():
    lines = ['A Y', 'B X', 'C Z']
    score = sut.sn(lines)
    assert score == 15


def test_day2_win():
    lines = ['A Y']
    score = sut.sn(lines)
    assert score == 8


def test_day2_loss():
    lines = ['B X']
    score = sut.sn(lines)
    assert score == 1


def test_day2_loss_loop():
    lines = ['A Z']
    score = sut.sn(lines)
    assert score == 3


def test_day2_win_loop():
    lines = ['C X']
    score = sut.sn(lines)
    assert score == 7


def test_day2_draw():
    lines = ['A X']
    score = sut.sn(lines)
    assert score == 4


def test_day2_larger():
    lines = [
        'C Y',  # 3 2 | 0 | 2
        'A Z',  # 1 3 | 0 | 3
        'B X',  # 2 1 | 0 | 1
        'B Y',  # 2 2 | 3 | 5
        'C X',  # 3 1 | 6 | 7
        'B Z',  # 2 3 | 6 | 9
    ]
    score = sut.sn(lines)
    assert score == 27
