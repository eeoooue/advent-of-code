
from filereader import FileReader
from packethandler import PacketReader
from jaggediterator import JaggedIterator

pairs = [line for line in FileReader.get_lines(13, "example.txt") if len(line) > 1]

# 6085 was WRONG and is TOO HIGH

def meet_criteria(a, b):

    m = len(a)
    n = len(b)
    for i in range(min(m, n)):
        if a[i] < b[i]:
            return True
        if a[i] > b[i]:
            return False

    return True if m <= n else False


def compare_packets(packet_a, packet_b):

    unpacked_a = PacketReader.unpack_packet(packet_a)
    unpacked_b = PacketReader.unpack_packet(packet_b)

    print(unpacked_a)

    a_iter = JaggedIterator(unpacked_a)
    b_iter = JaggedIterator(unpacked_b)

    m = a_iter.size()
    n = b_iter.size()

    min_size = min(m, n)

    for i in range(min_size):
        a = a_iter.next()
        b = b_iter.next()
        if a < b:
            return True
        if a > b:
            return False

    if m < n:
        return True

    if m > n:
        return False

    if a_iter.nests < b_iter.nests:
        return True
    if a_iter.nests > b_iter.nests:
        return False
    return True



correct_order = []

n = len(pairs)
pair_num = 0
for i in range(0, n, 2):
    pair_num += 1
    if compare_packets(pairs[i], pairs[i+1]):
        correct_order.append(pair_num)
    
print(correct_order)

print(f"the sum of these values is {sum(correct_order)}")



