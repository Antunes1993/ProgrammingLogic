class  MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndes(self, index):
        return index // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1
    def getRightChildIndex(self, index):
        return 2 * index + 2




