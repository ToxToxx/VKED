class Node(object):
    def _init_(self,data):
        self.data = data
        self.next = None

class Stack(object):
    def _init_(self):
        self.top = None
    def push(self, data):
        #создаем новый узел и добавляем новое значени в него
        new_node = Node(data)
        #если стек был пуст, значит первый элемент и есть head
        if not self.top:
            self.top = new_node
            return
        #если не пуст, то устанавливаем head
        #в качестве параметра next для нового узла
        new_node.next = self.top
        #записываем в head новый узел
        self.top = new_node
        new_node.next,self.head = self.head,new_node
    def pop(self):
        #проверяем что наш стек содержит хотя бы вершину
        if not self.top:
            return None
        top = self.top
        if self.top.next:
            #переписываем значение вершины на след элемент
            self.top = self.top.next
        else:
            #если стек пуст, то ставим None в вершину
            self.top = None
        #возвращаем значение, хранящееся в вершине стека
        return top.data