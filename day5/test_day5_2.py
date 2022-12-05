import day5_2 as sut


def test_move2():
    matrix = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    instruction = [2, 1, 2]
    expected = [[], ['M', 'C', 'D', 'Z', 'N'], ['P']]
    actual = sut.move2(matrix, instruction)
    assert actual == expected