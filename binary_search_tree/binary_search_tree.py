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

    

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
