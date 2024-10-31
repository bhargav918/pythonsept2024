#!/usr/bin/python
"""
Purpose: Double Linked List


  h  e  l  l  o
  3  4  6  8  9

            n1     n2   n3
pre_n_add   None   3    4
value       h      e    l    l   o
next_n_add  4      6    8

"""


class DoubleLinkedList:
    def __init__(self, data, prev_nd_addr=None, next_nd_addr=None):
        self.data = data
        self.prev_nd_addr = prev_nd_addr
        self.next_nd_addr = next_nd_addr

    def set_prev_node_address(self, prev_n_add):
        self.prev_nd_addr = prev_n_add

    def set_next_node_address(self, next_n_add):
        self.next_nd_addr = next_n_add

    def __repr__(self):
        return f"{self.prev_nd_addr}|{self.data}|{self.next_nd_addr}"



word = "hello"
list_of_nodes = []
previous_node = None

for char in word:
    node = DoubleLinkedList(char)

    if previous_node:  
        previous_node.set_next_node_address(id(node))
        node.set_prev_node_address(id(previous_node))

    
    list_of_nodes.append(node)
    previous_node = node  

for node in list_of_nodes:
    print(node)