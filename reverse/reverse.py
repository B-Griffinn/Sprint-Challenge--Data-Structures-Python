class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        ## PLAN ##
        # set node to be our head
        head = self.head
        # set prev to be none
        prev = None
        # loop thru list while node.next is not none
        while head is not None:
            # # update next_node to be node.next
            nxt_node = head.next_node
            # # udpate node.next to be prev
            head.next_node = prev
            # # udpate prev to be our node
            prev = head
            # # udpate node to be our next_node
            head = nxt_node
        # once we leave the while loop we can update our new head to be the last prev prop
        self.head = prev
