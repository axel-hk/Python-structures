#класс Node для определения элемента списка
from Node import Node
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'
    def __getitem__(self, key):#поддержка обращения по ключу
        length =0
        current = None
        if self.first != None:
            current = self.first
            while (key!=length and current.next != None):
                current = current.next
                length +=1
            if key==length:current=current.value
        return current

    def clear(self):
        self.__init__()
#Добавление элементов в конец спискa
    def add(self, x):
         self.length += 1
         if self.first == None:
            #self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
         else:
            #здесь, указывают на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)
#Добавление элементов в начало списка
    def push(self, x):
            self.length+=1
            if self.first == None:
                self.last = self.first = Node(x,None)
            else:
                self.first = Node(x,self.first)
#Удаление выбранного элемента
    def Del(self,i):
        if (self.first == None):
          return
        curr = self.first
        count = 0
        if i == 0:
          self.first = self.first.next
          return
        while curr != None:
            if count == i:
              if curr.next == None:
                self.last = curr
              old.next = curr.next 
              break
            old = curr  
            curr = curr.next
            count += 1
#Удаление повторяющихся значений
 
    def RemoveDuplicates(self):
        if (self.first == None):
            return
        old=curr = self.first
        while curr != None:
            if curr.next != None:
                if old.value == curr.next.value:
                    curr.next = curr.next.next
            else:
                old=curr = old.next
            curr=curr.next
    def length(self):
        return self.length
