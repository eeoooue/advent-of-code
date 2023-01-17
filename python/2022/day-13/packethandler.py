
import numpy as np

class PacketHandler:

    @staticmethod
    def unpack_packet(s):

        DIGITS = set("0123456789")

        nums = []
        n = len(s)

        stack = []

        i = 1
        while i < n:
            if s[i] in DIGITS:
                stack.append(s[i])
            elif stack:
                nums.append(int("".join(stack)))
                stack = []

            if s[i] == "[":
                j = PacketHandler.__find_closing_brace(s, i)
                if j != -1:
                    nums.append(PacketHandler.unpack_packet(s[i:j+1]))
                    i = j
                
            i += 1
        
        return nums

    def __find_closing_brace(s, i):

        n = len(s)
        table = {"[": 0, "]": 0}
        for j in range(i, n):
            x = s[j]
            if x in table:
                table[x] += 1
            if table["["] == table["]"]:
                return j

        return -1
    
    @staticmethod
    def packets_are_inorder(left_packet, right_packet):

        m = len(left_packet)
        n = len(right_packet)

        for i in range(min(m, n)):
            verdict = compare(left_packet[i], right_packet[i])
            if verdict != "inconclusive":
                return True if verdict == "valid" else False

        return True if (m <= n) else False


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

