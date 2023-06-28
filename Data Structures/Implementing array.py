# Implementation
# Although arrays are pre-defined in Python in the form of lists, we can implement our own arrays.

# Here, we will implement our own array with some common methods such as access, push, pop, insert, delete

class Array():
    def __init__(self):
        self.length = 0
        self.data = {}

    # The __str__ method is called when the following functions are invoked on the object and return a string:
    # print()
    # str()

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        self.length -= 1

# Use  print() for output

arr = Array()
print(arr)  # {'length': 0, 'data': {}}

arr.push('hi')
print(arr)  # {'length': 1, 'data': {0: 'hi'}}

print(arr.pop())  # hi
print(arr)   # {'length': 0, 'data': {}}

arr.push('yo')
arr.push('!')
print(arr)

arr.delete(1)
print(arr)
