class Node:
    def _init_(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def _init_(self):
        self.head = Node()
        self.tail = Node()
        #при инициализаци head указывает на tail
        self.head.next = self.tail
        #tail ссылается на head
        self.tail.prev = self.head
        #размер очереди при ее создании ставим на 0
        self.size = 0
    def push(self, value):
        #создаем новый узел
        new_node = Node(value)
        #теперь надо менять 4 ссылки
        #новый элемент ссылается в качестве следующего на последний в очереди
        new_node.next = self.head.next
        #новый элемент в качекстве предыдущего ссылается на head
        new_node.prev = self.head
        #первый элемент ранее теперь в качестве предыдущего ссылается на новый элемент
        self.head.next.prev = new_node
        #остается заменить только последнюю сылку где head ссылается на новый элемент
        self.head.next = new_node
        self.size += 1