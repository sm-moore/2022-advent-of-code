import copy

import day11 as sut

# def test_parse_monkeys():
#     lines = [
#         'Monkey 0:',
#         'Starting items: 79, 98',
#         'Operation: new = old * 19',
#         'Test: divisible by 23',
#         '    If true: throw to monkey 2',
#         '    If false: throw to monkey 3',
#     ]
#     expected = [
#         sut.Monkey(0, [79, 98], lambda x: x*19, lambda x: 2 if x % 23 == 0 else 3)
#     ]
#     assert sut.parse_monkeys(lines) == expected

MONKEYS_TEST = {
    #     Monkey 0:
    #   Starting items: 79, 98
    #   Operation: new = old * 19
    #   Test: divisible by 23
    #     If true: throw to monkey 2
    #     If false: throw to monkey 3
    0: sut.Monkey(0, [79, 98], lambda old: old*19,
               lambda worry: 2 if worry % 23 == 0 else 3),
    # Monkey 1:
    #   Starting items: 54, 65, 75, 74
    #   Operation: new = old + 6
    #   Test: divisible by 19
    #     If true: throw to monkey 2
    #     If false: throw to monkey 0
    1: sut.Monkey(1, [54, 65, 75, 74], lambda old: old+6,
               lambda worry: 2 if worry % 19 == 0 else 0),
    # Monkey 2:
    #   Starting items: 79, 60, 97
    #   Operation: new = old * old
    #   Test: divisible by 13
    #     If true: throw to monkey 1
    #     If false: throw to monkey 3
    2: sut.Monkey(2, [79, 60, 97], lambda old: old*old,
               lambda worry: 1 if worry % 13 == 0 else 3),

    # Monkey 3:
    #   Starting items: 74
    #   Operation: new = old + 3
    #   Test: divisible by 17
    #     If true: throw to monkey 0
    #     If false: throw to monkey 1
    3: sut.Monkey(3, [74], lambda old: old + 3,
               lambda worry: 0 if worry % 17 == 0 else 1),
}


def test_play_round():
    result = sut.play_round(copy.deepcopy(MONKEYS_TEST), {mid: 0 for mid in MONKEYS_TEST.keys()})
    # Monkey 0: 20, 23, 27, 26
    # Monkey 1: 2080, 25, 167, 207, 401, 1046
    # Monkey 2: 
    # Monkey 3: 
    expected = {0: 2, 1: 4, 2: 3, 3: 5}
    assert result == expected


def test_20_rounds():
    result = sut.sn(copy.deepcopy(MONKEYS_TEST), 20)
    expected = {0: 101, 1: 95, 2: 7, 3: 105}
    assert result == expected
    insp = sorted(result.values())
    final = insp[-1] * insp[-2]
    assert final == 10605
