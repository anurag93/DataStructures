'''
Created on 18-Oct-2019

@author: anuragsengupta
'''

from LinkedListDS.LinkedList import LinkedList

linkedList = LinkedList()

linkedList.insertEnd(12)
linkedList.insertEnd(122)
linkedList.insertEnd(31)
linkedList.insertEnd(321)
linkedList.insertStart(43)

linkedList.traverseList()
print(linkedList.size())
linkedList.remove(31)
linkedList.traverseList()
print(linkedList.size())