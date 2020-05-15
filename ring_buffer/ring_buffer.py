from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.order = DoublyLinkedList()
        self.storage = dict()

    def append(self, key, value):
        # if item / key already exists
        if key in self.storage:
            # overwrite the value
            # wehre is the value sorted?
            # we can get the node fro mour storage key
            node = self.storage[key]
            # the nodes value is the new tuple with the old key and new value
            node.value = (key, value)
            # move value to the tail which is most recently used
            self.order.move_to_end(node)
            return  # xit the function

        # what if our storage is at its capacity??
        if len(self.order) == self.capacity:
            # remove the oldest node
            # we have to references to the last node - in our DLL and in our dict
            # remove from both
            index_of_oldest = self.order.head.value[0]
            # now delete the found index
            del self.storage[index_of_oldest]
            # now we may remove it from DLL
            self.order.remove_from_head()

        # finally add newest node to end/tail and add it back to storage
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail

    def get(self, key):
        # if key does not exist in our cache return none
        if key not in self.storage:
            return None
        else:
            # if key in cache
            # # then move it to most recently used
            # # create a place holder for our node in our storage
            node = self.storage[key]
            self.order.move_to_end(node)
            # return the value of node in its tuple whise is equal to index[1]
            return node.value[1]
