import random

class arraylist:
    def __init__(self, filename):
        self.array = []
        self.current = -1
        self.filename = filename

        myfile = open(filename, 'r')
        for i in myfile:
            self.array.append(i.rstrip())

        self.randomize()

    def randomize(self):
        for i in range(10):
            a = random.randint(0, len(self.array)-1)
            b = random.randint(0, len(self.array)-1)

            temp = self.array[a]
            self.array[a] = self.array[b]
            self.array[b] = temp

    def getNext(self):
        if self.current < len(self.array)-1:
            self.current += 1
        else:
            self.current = 0
        return self.array[self.current]