'''
Created on 18-Oct-2019

@author: anuragsengupta
'''
from BinarySearchTreeDS.BinarySearchTree import BinarySearchTree as BST

bst = BST()
bst.insert(12)
bst.insert(-2)
bst.insert(-3)
bst.insert(10)
bst.insert(8)
bst.insert(15)
bst.insert(22)
#bst.remove(12)

bst.traverseInOrder()