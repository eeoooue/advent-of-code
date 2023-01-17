
from monkey import Monkey

# 10605 is 20 round answer for example
# I said 88208 was answer for part 1

# I said 21115867968 was answer for part 2

## below code & classes only work for part 2 ahhhh

monkeys = {}

def load_example_monkeys():

    divisors = [23, 19, 13, 17]

    monkeys[0] = Monkey(0, [79, 98], divisors, 2, 3, True)
    monkeys[1] = Monkey(1, [54, 65, 75, 74], divisors, 2, 0, True)
    monkeys[2] = Monkey(2, [79, 60, 97], divisors, 1, 3, True)
    monkeys[3] = Monkey(3, [74], divisors, 0, 1, True)

def load_my_monkeys():

    divisors = [19, 2, 13, 5, 7, 11, 17, 3]

    monkeys[0] = Monkey(0, [71, 86], divisors, 6, 7, False)
    monkeys[1] = Monkey(1, [66, 50, 90, 53, 88, 85], divisors, 5, 4, False)
    monkeys[2] = Monkey(2, [97, 54, 89, 62, 84, 80, 63], divisors, 4, 1, False)
    monkeys[3] = Monkey(3, [82, 97, 56, 92], divisors, 6, 0, False)
    monkeys[4] = Monkey(4, [50, 99, 67, 61, 86], divisors, 5, 3, False)
    monkeys[5] = Monkey(5, [61, 66, 72, 55, 64, 53, 72, 63], divisors, 3, 0, False)
    monkeys[6] = Monkey(6, [59, 79, 63], divisors, 2, 7, False)
    monkeys[7] = Monkey(7, [55], divisors, 2, 1, False)

## example

load_my_monkeys()

n_monkeys = len(monkeys)
rounds = 10000

for r in range(rounds):
    for i in range(n_monkeys):
        active_monkey = monkeys[i]

        while active_monkey.holding:
            (item, friend) = active_monkey.take_action()
            friend_monkey = monkeys[friend]
            friend_monkey.recieve_item(item)


# current monkeys state

for i in range(n_monkeys):
    active_monkey = monkeys[i]
    print(f"monkey {i}: {active_monkey.holding}")


scores = []
for i in range(n_monkeys):
    active_monkey = monkeys[i]
    print(f"monkey {i} inspected {active_monkey.count_inspected} items")
    scores.append(active_monkey.count_inspected)

print(scores)

scores.sort(reverse=True)
print(f"monkey_business = {scores[0] * scores[1]}")