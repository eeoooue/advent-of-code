
# Day 01: Calorie Counting

---

## Part 1

We are asked to find the most calories carried by any elf in the group.

Let's write a solution class, we want to:

1. Read the list of calories given in the input
2. Calculate total calories held by each elf
3. Find the elf with the most calories held

```py
class Solution:
    def __init__(self, item_list):
        pass

    def read_list(self):
        pass

    def add_elf(self):
        pass

    def get_elf_with_most_calories(self):
        pass
```


## Reading the input


I made this **FileReader** class to read the file to a line-by-line array of strings.

```py
class FileReader:

    @staticmethod
    def get_lines(filename):

        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines
```

We'll hand the array of strings to our **Solution** class, and have our constructor call read_list()

```py
item_list = FileReader.get_lines("example.txt")
solver = Solution(item_list)
```


## Calculate calories

We know we want to store calorie totals for each elf.

```py
def __init__(self, item_list):
        
    self.elves = []
    self.read_list(item_list)
```

```py
def read_list(self, item_list):

    calories = 0
    for item_value in item_list:
        if item_value == "":
            self.add_elf(calories)
            calories = 0
        else:
            calories += int(item_value)
    self.add_elf(calories)
```

Here we iterate through each line from the input.

If the line is a number, we'll add it to our current calories total.

If the line is empty or we reach the end of the input, we'll try to add a new elf to our collection with the current total of calories, then we'll reset calories to 0.

```py
def add_elf(self, calories):

    if calories > 0:
        self.elves.append(calories)
```

## Elf with the most calories

For our last step we can just take the maximum from our array of calorie totals.

```py
def get_elf_with_most_calories(self):

    return max(self.elves)
```

---

# Part 2

In Part 2, we want to find the sum of the 3 greatest calorie totals in the group of elves.

We could sort our array, but I want to try using a **heap**, which will give us access to the greatest value in constant time.



```py
import heapq

class Solution:
    def __init__(self, item_list):
        pass

    def read_list(self, item_list):
        pass

    def add_elf(self, calories):
        pass

    def sum_largest_elves(self, n):
        pass

    def get_n_largest_values(self, n):
        pass

    def heap_pop(self):
        pass

    def heap_push(self, calories):
        pass
```

We can use the **heapq** library for quick access to a MinHeap, and we can use this as a MaxHeap by treating our values as negative whenever we interact with the heap.

Here I've changed add_elf() to use our heap methods.

```py
def add_elf(self, calories):

    if calories > 0:
        self.heap_push(calories)

def heap_push(self, calories):

    heapq.heappush(self.elves, -calories)
    
def heap_pop(self):

    calories = -heapq.heappop(self.elves)
    return calories
```

Now we can look at the n largest values in our heap by popping n times & then putting the elements back.

```py
def get_n_largest_values(self, n):

    values = []
    for i in range(n):
        calories = self.heap_pop()
        values.append(calories)

    for calories in values:
        self.heap_push(calories)
    
    return values
```

Finally, let's write a generalised function that can be used to answer part one & two

```py
def sum_largest_elves(self, n):

    values = self.get_n_largest_values(n)
    return sum(values)
```
