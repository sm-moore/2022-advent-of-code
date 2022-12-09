import day8 as sut

# def test_parse():
#     input = [
#         '303',
#         '350',
#         '356'
#     ]
#     expected = [
#         sut.Tree(3, 0, 0, 5)
#     ]
#     assert sut.parse(input) == expected


def test_parse():
    input = [
        '303',
        '350',
        '356'
    ]
    expected = [
        [3, 0, 3],
        [3, 5, 0],
        [3, 5, 6]
    ]
    assert sut.parse(input) == expected


def test_tree_is_visible():
    input = [
        [3, 0, 3],
        [3, 5, 0],
        [3, 5, 6]
    ]
    tree_index = (1, 1)
    assert sut.tree_is_visible(input, tree_index)


def test_tree_is_visible2():
    input = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390']
    inn = sut.parse(input)
    tree_index = (1, 1)
    assert sut.tree_is_visible(inn, tree_index)

    tree_index = (2, 2)
    assert sut.tree_is_visible(inn, tree_index) == False


def test_sn():
    input = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390']
    inn = sut.parse(input)
    assert sut.sn(inn) == 21


def test_scenic_score():
    input = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390']
    inn = sut.parse(input)
    assert sut.scenic_score(inn, (1, 2)) == 4