class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')
print(queue.head.data)
print(queue.head.next_node.data)
print(queue.tail.data)
print(queue.tail.next_node)
#print(queue.tail.next_node.data)


