
from filereader import FileReader
from packethandler import PacketHandler

packets = [PacketHandler.unpack_packet(line) for line in FileReader.get_lines(13, "input.txt") if len(line) > 1]

def solve_part2():

    n = len(packets)

    for i in range(n):
        swap = i
        for j in range(i+1, n):
            if PacketHandler.packets_are_inorder(packets[j], packets[swap]):
                swap = j

        a = packets[i].copy()
        b = packets[swap].copy()

        packets[i] = b
        packets[swap] = a

    dividers = []
    for i in range(n):
        packet = packets[i]
        if packet == [[2]]:
            dividers.append(i+1)
        if packet == [[6]]:
            dividers.append(i+1)

    return dividers[0] * dividers[1]

packets.append([[2]])
packets.append([[6]])
print(f"Part 2 = {solve_part2()}")

# 19261