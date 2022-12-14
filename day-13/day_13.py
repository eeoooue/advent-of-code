
from filereader import FileReader
from packethandler import PacketHandler

packets = [PacketHandler.unpack_packet(line) for line in FileReader.get_lines(13, "input.txt") if len(line) > 1]

def solve_part1():

    n = len(packets)
    correct_pairs = []
    for pair in range(0, n//2):
        i = pair*2
        if PacketHandler.packets_are_inorder(packets[i], packets[i+1]):
            correct_pairs.append(pair+1)

    return sum(correct_pairs)

def solve_part2():

    n = len(packets)
    for i in range(n):
        swap = i
        for j in range(i+1, n):
            if PacketHandler.packets_are_inorder(packets[j], packets[swap]):
                swap = j
        temp = packets[i].copy()
        packets[i] = packets[swap]
        packets[swap] = temp

    dividers = []
    for i in range(n):
        packet = packets[i]
        if packet == [[2]]:
            dividers.append(i+1)
        elif packet == [[6]]:
            dividers.append(i+1)

    return dividers[0] * dividers[1]

print(f"Part 1 = {solve_part1()} (5390 for me)")

packets.append([[2]])
packets.append([[6]])

print(f"Part 2 = {solve_part2()} (19261 for me)")