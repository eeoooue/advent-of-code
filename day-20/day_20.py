
from filereader import FileReader
from mylist import MyList

def cycled_array(nums):

    i = nums.index(0)
    return nums[i:] + nums[:i]
    

def solve(filename, decryption_key, repetitions):

    lines = [line for line in FileReader.get_lines(20, filename)]
    array = [(int(x) * decryption_key) for x in lines]

    list = MyList(array)
    for i in range(repetitions):
        list.mix()

    queue = cycled_array(list.get_values())

    n = len(queue)
    total = 0
    for i in (1000, 2000, 3000):
        total += queue[i % n]

    return total


print(f"part 1 example = {solve('example.txt', 1, 1)} (should be 3)")
print(f"part 1 ans = {solve('input.txt', 1, 1)} (1087 for me)")

print(f"part 2 example = {solve('example.txt', 811_589_153, 10)} (should be 1623178306)")
print(f"part 2 ans = {solve('input.txt', 811_589_153, 10)} (13084440324666 for me)")
