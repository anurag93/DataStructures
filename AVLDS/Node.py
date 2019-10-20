class Node(object):
    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rightChild = None
        self.leftChild = None
        self.counter = 0

    def insert(self, data, parentNode):

        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data, parentNode)
            else:
                self.leftChild.insert(data, parentNode)

        else:
            if not self.rightChild:
                self.rightChild = Node(data, parentNode)
            else:
                self.rightChild.insert(data, parentNode)


    def traverseInOrder(self):
        if self.leftChild:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverseInOrder()

    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.getMin()

    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.getMax()

