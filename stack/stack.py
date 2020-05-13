#Node
# value
# next - pointer that points to the next node

class Node:
     def __init__(self, value=None, next_node=None):
          # the value at this linked list node
          self.value = value
          # reference to the next node in the list
          self.next_node = next_node

     def get_value(self):
          return self.value

     def get_next(self):
          return self.next_node

     def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
          self.next_node = new_next

   

class LinkedList:
     def __init__(self, head=None, tail=None):
          # first node in the list 
          self.head = head
          # last node in the list 
          self.tail = tail

     def length(self):
          current_node = self.head
          total = 0
          while current_node!=None:
               total+=1
               current_node = current_node.next_node
     
     #add to the tail
     def add_to_tail(self, value):
          # regardless of if the list is empty or not, we need to wrap the value in a Node 
          new_node = Node(value)
          # what if the list is empty? 
          if self.head is None:
               self.head = new_node
               return
          else:
          # what node do we want to add the new node to? 
          # the last node in the list 
          # we can get to the last node in the list by traversing it 
          # add the new node when you reach the end
               current_node = self.head
               while current_node.get_next() is not None:  #while it's not the last node
                    current_node = current_node.get_next()  # keep traversing, goig through the list
               current_node.set_next(new_node)  # finally when it reaches the last node set the next one to the new node. new node is now the tail
          self.tail = new_node
          return self.tail.value
     
     def add_to_head(self, value):
          new_node = Node(value)
          if self.head is None:
               self.head = new_node
               return
          else:
              new_node.next_node = self.head
              self.head = new_node
              return self.head.value

     def remove_from_tail(self, value):
          # Once you find the target, you want to link its previous and next nodes. 
          # This re-linking is what removes the target node from the list.
          if not self.head:
               return f"Empty List"
          
          if self.head.data == value: #Check if head is also tail, list has 1 value
               self.head = self.head.next_node # if the head is the one we want to delete, point the new head to the next_node
               return
          else: # traverse the list until you find the node you want to remove
               current_node = self.head
               for node in self:
                    if node.value == value:
                         current_node.next_node = node.next_node
                         return
                    current_node = node

               while current_node.get_next() is not None:
                    current_node = current_node.get_next()
               

     def remove_from_head(self):
        if not self.head:
            return None
        else:
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = self.head.get_next()
            return value


     def get_linkedlist(self):
         #traverse the linked list
         current_node = self.head
         nodes = []
         while current_node is not None:
              nodes.append(current_node.value)
              current_node = current_node.next_node
         nodes.append("None")
         return nodes
          



"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

#FILO 
#using a list(array)  ✔
""" class Stack:
    def __init__(self):
        self.size = 0
        self.storage = [] 

    def __len__(self):
        return len(self.storage)

    def push(self, value): #add to the stack, top elemenf
        self.storage.append(value) #added to the end of list
        self.size += 1

    def pop(self): #remove from the stack
        if len(self.storage) >= 1: 
            return self.storage.pop()
        return

    def get_stack(self):
        return self.storage

    def is_empty(self):
        return self.storage == []

    def peek(self): #peek the top of the stack
        if not self.is_empty():
            return self.storage[-1] #last entered
 """

#FILO
#using a LinkedList()
## add and remove from the same end
## add to head and remove from head
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    #append to tail
    def push(self, value): #add to the stack, top elemenf
        self.storage.add_to_head(value) #added to the end of list
        self.size += 1

    def pop(self): #remove from the stack, from tail
        if self.size > 0: 
            self.size -= 1
            return self.storage.remove_from_head()

    def get_stack(self):
        return self.storage

    def is_empty(self):
        return self.storage == []

    def peek(self): #peek the top of the stack
        if not self.is_empty():
            return self.storage[-1] #last entered
