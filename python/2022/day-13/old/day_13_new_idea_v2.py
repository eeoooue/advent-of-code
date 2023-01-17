
from filereader import FileReader
from packethandler import PacketReader
from jaggediterator import JaggedIterator

import numpy as np

packets = [line for line in FileReader.get_lines(13, "example.txt") if len(line) > 1]


def flatten_array(arr):

    nums = []

    if np.isscalar(arr):
        nums.append(arr)
    else:
        for x in arr:
            for e in flatten_array(x):
                nums.append(e)

    return nums

def nesting_depth(arr, d):


    return

def is_list(x):

    return False if np.isscalar(x) else True


def meet_criteria(left, right):

    if not left and not right:
        return True
    if not left:
        return True
    if not right:
        return False

    if not is_list(left) and not is_list(right):
        if left < right:
            return True
        if left > right:
            return False

    if is_list(left) and is_list(right):
        if left[0] < right[0]:
            return True
        if left[0] > right[0]:
            return False
        return meet_criteria(left[1:], right[1:])

    if is_list(left) and not is_list(right):
        return meet_criteria(left, [right])

    if not is_list(left) and is_list(right):
        return meet_criteria([left], right)

    return True


def compare_pair(packet_a, packet_b):

    unpacked_a = PacketReader.unpack_packet(packet_a)
    unpacked_b = PacketReader.unpack_packet(packet_b)

    m = len(unpacked_a)
    n = len(unpacked_b)

    for i in range(min(m, n)):
        a_value = unpacked_a[i]
        b_value = unpacked_b[i]
        if not meet_criteria(a_value, b_value):
            return False

    return True if (m <= n) else False

correct_order = []

n = len(packets)
pair_num = 0
for i in range(0, n, 2):
    pair_num += 1
    if compare_pair(packets[i], packets[i+1]):
        correct_order.append(pair_num)
    
print(correct_order)
