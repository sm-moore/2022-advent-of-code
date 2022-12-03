import day1 as sut


def test_highest_calories_carried():
    input = [[5], [6]]
    calories = sut.highest_calories_carried(input)
    assert calories == 6


def test_highest_calories_carried_mux():
    input = [[5, 4], [6]]
    calories = sut.highest_calories_carried(input)
    assert calories == 9


def test_lines_to_matrix():
    lines = ['5', '6']
    matrix = sut.lines_to_matrix(lines)
    assert matrix == [[5, 6]]


def test_lines_to_matrix_mux():
    lines = ['5', '6', '', '7']
    matrix = sut.lines_to_matrix(lines)
    assert matrix == [[5, 6], [7]]


def test_n_highest_calories_carried():
    input = [[5], [1], [6], [2]]
    calories = sut.n_highest_calories_carried(input, 2)
    assert calories == [5, 6]
