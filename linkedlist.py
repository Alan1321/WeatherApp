class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self, filename):
        self.head = None
        self.current = None
        self.secondlast = None
        self.listlen = 0
        self.filename = filename

        myfile = open(filename, 'r+')
        for i in myfile:
            self.insert_bottom(i.rstrip())
        myfile.close()

    def insert_top(self,city):
        newnode = node(city)
        newnode.next = self.head
        self.head = newnode
        self.listlen += 1

    def insert_bottom(self,city):
        if self.head == None:
            newnode = node(city)
            newnode.next = self.head
            self.head = newnode
            self.secondlast = self.head
        else:
            newnode = node(city)
            newnode.next = None
            self.secondlast.next = newnode
            self.secondlast = newnode
        self.listlen = self.listlen + 1

    def delete(self,value):
        curr = self.head
        if self.listlen:
            if curr.data != value:
                while curr.next:
                    if curr.next.data == value:
                        to_delete = curr.next
                        curr.next = curr.next.next
                        del to_delete
                        self.listlen = self.listlen - 1
                        break
                    curr = curr.next
            else:
                to_delete = self.head
                self.head = self.head.next
                del to_delete
                self.listlen = self.listlen - 1

    def delete_insert(self,city):
        self.delete(city)
        self.insert_top(city)
        self.file_write()

    def getNext(self):
        current = self.current
        if current == None or current.next == None:
            self.current = self.head
        else:
            self.current = self.current.next
        return self.current.data

    def file_write(self):
        self.current = None
        myfile = open(self.filename, 'r+')
        myfile.truncate(0)
        for i in range(self.listlen):
            myfile.write(self.getNext()+'\n')
        myfile.close()