"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BinarySearchTree class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BinarySearchTree class.
"""

# each node in a BST is a BST !!!


class BinarySearchTree:
    def __init__(self, value):
        # ROOT VALUE #
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # PLAN #
        # check if empty
        # if empty put node here/at root
        ## ** We cant do the above because our BTSNode is initialized with a value ** ##
        # if new < node.value
        # leftnode.insert value
        # if left does not exist
        # create left
        #   else:
        # leftnode.insert value
        # if >=
        # if right does not exist
        # create right
        # else:
        # rigtnode.insertvalue
        # rightnode.insert value
        # look left!!!
        if value < self.value:              # if our incoming value < the root value
            if self.left is None:           # and if self.left is None
                # then our left value is a new node/BST with the value passed in
                self.left = BinarySearchTree(value)
            else:
                # otherwise we call on our left node and recurse until left is none so we can insert the new node value
                self.left.insert(value)
        # look right!!
        else:   # if root value is >= the incoming value
            if self.right is None:
                # create a right node/BST
                self.right = BinarySearchTree(value)
            else:
                # otherwise we will recurse right until we can insert a value to the right
                self.right.insert(value)

##############            ##############
############## END INSERT ##############
##############            ##############

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # PLAN #
        # if node is none return False BASE CASE
        # if node.value == findvalue: return True
        # else:
        # if find < node.value:
        # if node.left then find on left node:
        # else:
        # if node.right: find on right node
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                # we must return our function call in order to get an output
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # follow the right until the end
        # if we have a right node then return it recursively
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def iterative_get_max(self):
        # have the current max = the root value to start
        current_max = self.value
        # set a current pointer to the node we are ond
        current_pointer = self
        # traverse our tree
        while current_pointer is not None:
            # udpate out current_max variable when we see a larger value
            if current_pointer.value > current_max:
                current_max = current_pointer.value
            current_pointer = current_pointer.value
    # Call the function `fn` on the value of each node
    # DEPTH FIRST TRAVERSAL

    def for_each(self, fn):
        # call the fn function on each node
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # PLAN #
        # traverse the BST on the left side while there is a left and print the root value
        if self.left is not None:
            self.left.in_order_print(node)
        print(self.value)
        # traverse the BST on the right side while there is a right and print the root value
        if self.right is not None:
            self.right.in_order_print(node)
        # print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        ## PLAN ##
        # we need to utilize a queue and set it to a var
        storage_q = Queue()
        # add root to the Q
        storage_q.enqueue(self)
        # while Q is not empty:
        while (len(storage_q) > 0):
            # dequeue our node in order to remove from front of line and print it
            # dq method returns the value of our first item in the Q
            node = storage_q.dequeue()
            print(node.value)
            # check the nodes left and put it in line to be dequed and printed
            if node.left is not None:
                storage_q.enqueue(node.left)
            # check the nodes right and put it in line to be dequed and printed
            if node.right is not None:
                storage_q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node=None):
        # create a stack
        storage = Stack()
        # assign root of tree to stack
        storage.push(node)
        # loop thru stack while > 0
        while (len(storage) > 0):
            # # node = popped top of stack
            popped_node = storage.pop()
            # # print node.value
            print(popped_node.value)
            # # check left: add to stack
            if popped_node.left is not None:
                storage.push(popped_node.left)
            # # check right: add to stack
            if popped_node.right is not None:
                storage.push(popped_node.right)

        # Stretch Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
