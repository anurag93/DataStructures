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
bst.insert(11)
bst.insert(22)
bst.insert(254)

bst.traverseInOrder()

bst.remove(11)

bst.traverseInOrder()