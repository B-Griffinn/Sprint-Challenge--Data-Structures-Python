"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create new_node with the value passed in
        new_node = ListNode(value)
        # if length is 0 - set head and tail to = new_node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # otherwise
        #  - set prev prop on head to be new_node
        #  - set next prop on new_node to be head
        #  - udpate head to be new node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        # increment length
        # return list
        self.length += 1
        return self

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # store cuurent head prop in a var called old_head
        old_head = self.head
        # if list is empty return None
        if self.length == 0:
            return None
        # if length of list is 1
        # set head AND tail to be none
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next  # update head to be next of the old_head
            self.head.prev = None     # set heads prev prop to be none
            old_head.next = None      # set old heads next to be none
        # decrement length
        self.length -= 1
        # return old head
        return old_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create new_node with the value passed in
        new_tail = ListNode(value)
        # if length is 0 - set head and tail to = new_tail
        if self.length == 0:
            self.head = new_tail
            self.tail = new_tail
        # otherwise
        #  - set prev prop on tail to be new_tail
        #  - set next prop on new_tail to be tail
        #  - udpate tail to be new node
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
        # increment length
        self.length += 1
        # return list
        return self

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return None
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return None
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head and not self.tail:
            return None
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # start at the head
        current = self.head
        # store the current value on a variable so we can udpate when we loop thru list
        max_val = current.value
        # loop thru list until we reach end of list
        while current is not None:
            # compare current's value to the max_value
            if current.value > max_val:
                # update max_val to be the current value
                max_val = current.value

            # update current to be currents next each loop so not only does current stay ahead by 1 but so we can find the end of the list and stop
            current = current.next

        return max_val
