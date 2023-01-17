
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


def meet_criteria(left, right):

    flat_left = flatten_array(left)
    flat_right = flatten_array(right)

    print(f"{left} flattened = {flat_left}")
    print(f"{right} flattened = {flat_right}")

    m = len(flat_left)
    n = len(flat_right)

    for i in range(min(m, n)):
        a = flat_left[i]
        b = flat_right[i]
        if a < b:
            return True
        if a > b:
            return False
    
    return True if (m <= n) else False


def compare_pair(packet_a, packet_b):

    unpacked_a = PacketReader.unpack_packet(packet_a)
    unpacked_b = PacketReader.unpack_packet(packet_b)

    print(unpacked_a)

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
