
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


def meet_criteria(left, right):

    if compare(left, right) == "invalid":
        return False

    return True


def compare_pair(packet_a, packet_b):

    unpacked_a = PacketReader.unpack_packet(packet_a)
    unpacked_b = PacketReader.unpack_packet(packet_b)

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

correct_order = []

n = len(packets)
pair_num = 0
for i in range(0, n, 2):
    pair_num += 1
    if compare_pair(packets[i], packets[i+1]):
        correct_order.append(pair_num)
    
print(correct_order)
print(sum(correct_order))


# 1528 was wrong and is too LOW


# 5390 was finally the correct answer