
from filereader import FileReader
from packethandler import PacketReader

import numpy as np

packets = [line for line in FileReader.get_lines(13, "input.txt") if len(line) > 1]

def is_list(x):

    return False if np.isscalar(x) else True

def compare(left, right):

    if not left and not right:
        return "inconclusive"
    if not left:
        return "valid"
    if not right:
        return "invalid"

    if not is_list(left) and not is_list(right):
        if left < right:
            return "valid"
        if left > right:
            return "invalid"

    if is_list(left) and is_list(right):

        verdict = compare(left[0], right[0])
        if verdict != "inconclusive":
            return verdict
            
        return compare(left[1:], right[1:])

    if is_list(left) and not is_list(right):
        return compare(left, [right])

    if not is_list(left) and is_list(right):
        return compare([left], right)

    return "inconclusive"

def correct_ordering(unpacked_a, unpacked_b):

    m = len(unpacked_a)
    n = len(unpacked_b)

    for i in range(min(m, n)):
        a_value = unpacked_a[i]
        b_value = unpacked_b[i]

        verdict = compare(a_value, b_value)
        if verdict == "invalid":
            return False
        if verdict == "valid":
            return True

    return True if (m <= n) else False



unpacked = [PacketReader.unpack_packet(packet) for packet in packets]
unpacked.append([[2]])
unpacked.append([[6]])
n = len(unpacked)


for i in range(n):
    swap = i
    for j in range(i+1, n):
        if correct_ordering(unpacked[j], unpacked[swap]):
            swap = j

    a = unpacked[i].copy()
    b = unpacked[swap].copy()

    unpacked[i] = b
    unpacked[swap] = a

dividers = []
for i in range(n):
    packet = unpacked[i]

    if packet == [[2]]:
        dividers.append(i+1)

    if packet == [[6]]:
        dividers.append(i+1)
    print(packet)

print(f"the dividers are {dividers}")

print(f"part two answer = {dividers[0] * dividers[1]}")

# 19261