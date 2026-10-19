class Node:
    """Узел двусвязного списка."""

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    """Реализация двусвязного списка."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._length += 1

    def _get_node(self, index):
        if index < self._length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._length - 1 - index):
                current = current.prev
        return current

    def insert_at(self, index, value):
        if index < 0 or index > self._length:
            raise IndexError("Индекс выходит за пределы диапазона списка")

        if index == 0:
            self.prepend(value)
            return
        if index == self._length:
            self.append(value)
            return

        current = self._get_node(index)
        new_node = Node(value)

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self._length += 1

    def delete_at(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Индекс выходит за пределы диапазона списка")

        if self._length == 1:
            val = self.head.value
            self.head = self.tail = None
            self._length = 0
            return val

        if index == 0:
            val = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self._length -= 1
            return val

        if index == self._length - 1:
            val = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self._length -= 1
            return val

        current = self._get_node(index)
        val = current.value
        current.prev.next = current.next
        current.next.prev = current.prev
        self._length -= 1
        return val

    def forward_traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def backward_traverse(self):
        result = []
        current = self.tail
        while current:
            result.append(current.value)
            current = current.prev
        return result

    def find(self, value):
        current = self.head
        idx = 0
        while current:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        return -1

    def reverse(self):
        if self._length <= 1:
            return

        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.value
            current = current.prev

    def __repr__(self):
        if self.is_empty():
            return "DoublyLinkedList([])"
        return " <-> ".join(str(val) for val in self)
