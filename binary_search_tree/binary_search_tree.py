from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


#Each Node is also a Binary Search Tree
#Recursion
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if it's empty
        #if empty put node at root
        #sel.value can't be none
        if value < self.value:
        #   if left doesn't exist
            if self.left is None:
        #       create left
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: #value > self.value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #at the start, self will be root
        #compare target against itself
        if  self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def contains(self, target):
        current = self
        if  self.value == target:
            return True
        while current:
            if target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right
            else:
                return True
        return False
        

    # Return the maximum value found in the tree
    #Recursively
    def get_max(self): #the "right most node"
        #if there's a right
        #   get max on right
        #else
        #   return node.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def get_max(self): #the "right most node"
        max = self.value
        current = self
        while current:
            if current.value > max:
                max = current.value
            current = current.right
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #if there are nodes, call the function on them
        fn(self.value) #calls the value

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def iterative_for_each(self, fn):
        stack = []

        #add root node
        stack.append(self)

        #loop as long has stack has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            fn(current.value)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Use Stack - FIlO  ✔
    def in_order_print(self, node): #lnr
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
   
   
    # in an iterative breadth first traversal
    # Use queue - FIFO   ✔

    def bft_print(self, node):

        if node is None:
            return
        #empty queue
        queue = []
        #add root node to queue
        queue.append(node)

        #loop as long has stack has elements
        while len(queue) > 0:
            #print first from queue
            print(queue[0].value)
            #remove it from queue
            node = queue.pop(0)
            #enqueue left
            if node.left:
                queue.append(node.left)
            #enqueue right    
            if node.right:
                queue.append(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    #use stack
    def dft_print(self, node):

        if node is None:
            return

        stack = []
        stack.append(node)

        while len(stack) > 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT ✔
    def pre_order_dft(self, node): #nlr  
        if node: 
            print(node.value)
            # First recur on left child 
            self.pre_order_dft(node.left)    
            # now recur on right child 
            self.pre_order_dft(node.right) 


    # Print Post-order recursive DFT ✔
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)



bst = BSTNode(0)
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(8)
bst.insert(20)


print(bst.dft_print(bst))