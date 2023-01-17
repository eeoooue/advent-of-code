

class ListNode:

    def __init__(self, x, i) -> None:
        
        self.val = x
        self.next = None
        self.sequence = i
    

class MyList:

    def __init__(self, array) -> None:
        
        self.root = ListNode(array[0], 0)
        self.n = len(array)

        node = self.root
        for i in range(1, self.n):
            node.next = ListNode(array[i], i)
            node = node.next

    def mix(self):

        self.sequence = 0

        for i in range(self.n):
            (position, value) = self.get_next_node()
            self.remove_current_node()

            j = (position + value) % (self.n - 1)

            if j == 0:
                j = self.n - 1

            self.add_node(j, value)
            self.sequence += 1

    def get_next_node(self):

        node = self.root
        pos = 0
        while node.sequence != self.sequence:
            node = node.next
            pos += 1

        return (pos, node.val)

    def remove_current_node(self):

        dummy = ListNode(0, -1)
        dummy.next = self.root

        node = dummy
        while node.next.sequence != self.sequence:
            node = node.next

        node.next = node.next.next
        self.root = dummy.next

    def add_node(self, position, value):

        dummy = ListNode(0, -1)
        dummy.next = self.root
        
        node = dummy
        for i in range(position):
            node = node.next
        
        new_node = ListNode(value, self.sequence)
        new_node.next = node.next

        node.next = new_node
        self.root = dummy.next

    def get_values(self):

        node = self.root
        nums = [node.val]
        while node.next:
            node = node.next
            nums.append(node.val)

        return nums

