

from collections import deque

class Monkey:

    def __init__(self, id, starters, divisor_arr, a, b, example) -> None:
        
        self.id = id
        self.holding = deque([])
        self.divisor_arr = divisor_arr

        for x in starters:
            modarr = [x % self.divisor_arr[i] for i in range(len(self.divisor_arr))]
            self.holding.append(modarr)

        self.is_example = example

        self.count_inspected = 0

        self.divisor = self.divisor_arr[self.id]
        self.a = a
        self.b = b

    def take_action(self):

        mod_arr = self.get_inspected_item()
        friend = self.choose_friend(mod_arr)
        return (mod_arr, friend)

    def recieve_item(self, item):

        self.holding.append(item)

    def get_inspected_item(self):

        self.count_inspected += 1

        modarr = self.holding.popleft()

        new_arr = []
        for i in range(len(modarr)):
            x = self.operate(modarr[i])
            new_arr.append(x % self.divisor_arr[i])

        return new_arr

    def choose_friend(self, mod_arr):

        if mod_arr[self.id] == 0:
            return self.a
        return self.b

    def example_operation(self, old):

        match self.id:
            case 0:
                return old * 19
            case 1:
                return old + 6
            case 2:
                return old * old
            case 3:
                return old + 3

    def operate(self, old):

        if self.is_example:
            return self.example_operation(old)
                
        match self.id:
            case 0:
                return old * 13
            case 1:
                return old + 3
            case 2:
                return old + 6
            case 3:
                return old + 2
            case 4:
                return old * old
            case 5:
                return old + 4
            case 6:
                return old * 7
            case 7:
                return old + 7

    def test(self, value):

        return True if (value % self.divisor == 0) else False