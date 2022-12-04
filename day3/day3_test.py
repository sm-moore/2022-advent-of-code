import day3 as sut


def test_priority_value():
    assert sut.priority_value('a') == 1
    assert sut.priority_value('z') == 26
    assert sut.priority_value('A') == 27
    assert sut.priority_value('Z') == 52


def test_sn():
    lines = ['abcdec']
    assert sut.sn(lines) == 3


def test_sn2():
    lines = ['vJrwpWtwJgWrhcsFMMfFFhFp']
    assert sut.sn(lines) == 16


def test_sn3():
    lines = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
    ]
    assert sut.sn(lines) == 157


def test_find_pri_between_3_elves():
    lines = ['abc',
             'ebc',
             'gcj']
    assert sut.sn_2(lines) == 3


def test_sn_2():
    lines = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw'
    ]
    assert sut.sn_2(lines) == 70
