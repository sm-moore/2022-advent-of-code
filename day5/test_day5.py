import day5 as sut


def test_parse():
    input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()
    matrix, instructions = sut.parse(input)
    assert [['Z', 'N'], ['M', 'C', 'D'], ['P']] == matrix
    assert [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]] == instructions


def test_move_one():
    matrix = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    fromm = 1
    to = 2
    expected = [['Z'], ['M', 'C', 'D', 'N'], ['P']]
    actual = sut.move_one(matrix, fromm, to)
    assert actual == expected


def test_move():
    matrix = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    instruction = [2, 1, 2]
    expected = [[], ['M', 'C', 'D', 'N', 'Z'], ['P']]
    actual = sut.move(matrix, instruction)
    assert actual == expected


def test_move_all():
    matrix = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    instruction = [[1, 2, 1]]

    expected_matrix = [['Z', 'N', 'D'], ['M', 'C'], ['P']]
    assert sut.move_all(matrix, instruction) == expected_matrix


def test_many_moves():
    matrix = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    instructions = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    expected_matrix = [['C'], ['M'], ['P', 'D', 'N', 'Z']]
    assert sut.move_all(matrix, instructions) == expected_matrix
