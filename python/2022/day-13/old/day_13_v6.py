
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



def is_list(node):

    return True if node.children else False

def meet_criteria(left, right):


    










    return


def compare_packets(packet_a, packet_b):

    unpacked_a = PacketReader.unpack_packet(packet_a)
    unpacked_b = PacketReader.unpack_packet(packet_b)

    print(unpacked_a)
    print(unpacked_b)
    iter_a = JaggedIterator(unpacked_a)
    iter_b = JaggedIterator(unpacked_b)

    root_a = iter_a.root
    root_b = iter_b.root

    a_children = [node for node in root_a.children]
    b_children = [node for node in root_b.children]

    m = len(a_children)
    n = len(b_children)

    for i in range(min(m, n)):
        left = a_children[i]
        right = b_children[i]
        if not meet_criteria(left, right):
            return False

    return True if (m <= n) else False
    
correct_order = []

n = len(pairs)
pair_num = 0
for i in range(0, n, 2):
    pair_num += 1
    if compare_packets(pairs[i], pairs[i+1]):
        correct_order.append(pair_num)
    
print(correct_order)

print(f"the sum of these values is {sum(correct_order)}")



