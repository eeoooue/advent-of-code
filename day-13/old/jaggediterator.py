
import numpy as np

class MyNode:

    def __init__(self):
        
        self.children = []
        self.val = 0


class JaggedIterator:

    def __init__(self, array):

        self.array = array
        self.nests = 0
        self.root = self.explore(array)

        print(self.root)
        
    def explore(self, arr):

        node = MyNode()

        if np.isscalar(arr):
            node.val = arr
        else:
            for x in arr:
                node.children.append(self.explore(x))

        return node
    
