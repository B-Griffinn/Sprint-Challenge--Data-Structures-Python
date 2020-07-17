from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # use our DLL to store the data
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):
        # adds item to the buffer
        # PLAN #
        # check to see if our storage length is 0
        if len(self.storage) == 0:
            # # if our storage length is 0 then we need to set the incoming item to the head
            self.storage.add_to_head(item)
        # # udpate our current variable to be the head as well
            self.current = self.storage.head
        # else if the length of our storage is < than capacity - menaing we have room
        elif len(self.storage) < self.capacity:
            # # add incoming item to the tail of the list
            self.storage.add_to_tail(item)
        # else if the storage is at capacity - check if the current.next prop is none
        elif len(self.storage) == self.capacity:
            if self.current.next is not None:
                # # replace the value of current with the item bc we are at capacity
                self.current.value = item
                # # update the curent item to be the next node
                self.current = self.current.next
            # otherwise replace current.value with incoming item
            else:
                self.current.value = item
            # # update the curent to be the head of our storage
                self.current = self.storage.head

    def get(self):
        # returns all of the elements in the buffer in a list in their given order
        # does not return any NONE values in the list even if present

        ## PLAN ##
        # create a list to hold all elements in ring buffer
        item_list = list()
        # create a var to track the head of our buffer
        head_node = self.storage.head
        # while we have a head / ring buffer
        while head_node is not None:
            # - append the value to our list
            item_list.append(head_node.value)
        # # udpate our var tracking the head to be the next node in the list so that each loop it moves to the next item
            head_node = head_node.next
        # once loop is exited we will return the list
        return item_list
