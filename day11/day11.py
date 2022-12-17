import copy


class Monkey:
    def __init__(self, id, items, operation, test):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test

    def __eq__(self, other):
        ids_eq = self.id == other.id
        items_eq = sorted(self.items) == sorted(other.items)
        operation_eq = self.operation(5) == other.operation(5)
        test_eq = self.test(5) == other.test(5)
        test_eq2 = self.test(23) == other.test(23)
        return ids_eq and items_eq and operation_eq and test_eq and test_eq2


def _test(divisible_by, true_, false_):
    return lambda wl: true_ if wl % divisible_by == 0 else false_


MONKEYS = {
    0: Monkey(0, [71, 86], lambda x: x * 13, _test(19, 6, 7)),
    1: Monkey(1, [66, 50, 90, 53, 88, 85], lambda x: x + 3, _test(2, 5, 4)),
    2: Monkey(2, [97, 54, 89, 62, 84, 80, 63], lambda x: x + 6, _test(13, 4, 1)),
    3: Monkey(3, [82, 97, 56, 92], lambda x: x + 2, _test(5, 6, 0)),
    4: Monkey(4, [50, 99, 67, 61, 86], lambda x: x * x, _test(7, 5, 3)),
    5: Monkey(5, [61, 66, 72, 55, 64, 53, 72, 63], lambda x: x + 4, _test(11, 3, 0)),
    6: Monkey(6, [59, 79, 63], lambda x: x * 7, _test(17, 2, 7)),
    7: Monkey(7, [55], lambda x: x + 7, _test(3, 2, 1)),
}


def play_round(monkeys, inspections, modifier):
    for mid, monkey in monkeys.items():
        while True:
            if len(monkey.items) == 0:
                break
            item = monkey.items.pop(0)
            inspections[mid] += 1
            worry_level = monkey.operation(item)
            worry_level = worry_level // modifier
            next_monkey = monkey.test(worry_level)
            monkeys[next_monkey].items.append(worry_level)
    return inspections


def sn(monkeys, rounds=20, modifier=3):
    inspections = {mid: 0 for mid in monkeys.keys()}
    for i in range(rounds):
        inspections = play_round(monkeys, inspections, modifier)
    return inspections


inspections = sn(copy.deepcopy(MONKEYS), rounds=20, modifier=3)
insp = sorted(inspections.values())
result = insp[-1] * insp[-2]

assert result > 85263
assert result > 85554
assert result < 95770
print(result)


# 10000
inspections2 = sn(copy.deepcopy(MONKEYS), rounds=10000, modifier=1)
insp2 = sorted(inspections2.values())
result2 = insp2[-1] * insp2[-2]
print(result2)

# def parse_monkeys(lines):
    # monkeys = []
    # for line in lines:
    #     id = -1
    #     items = []
    #     operation = lambda x: x
    #     test = lambda x: x
    #     words = line.split(' ')
    #     if words[0] == 'Monkey':
    #         id = words[1][:1]
    #     elif words[1] == 'Starting':
    #         items = list(map(int, line.split('items: ')[1].split()))
    #     elif words[2] == 'Operation':