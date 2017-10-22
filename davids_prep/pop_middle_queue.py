"""
Implement a stack with push, poll, findMiddle, and deleteMiddle all in O(1) time
"""
from collections import deque

NONE_TYPE = type(None)

class MiddleStack:
    def __init__(self, data=None):
        self.__Queue = deque()
        self.__Stack = []
        self.__push_to_stack = True
        self.__last_elem = None
        if not isinstance(data, NONE_TYPE):
            for el in data:
                self.push(el)

    def push(self, el):
        self.__Queue.append(el)
        if self.__push_to_stack:
            self.__Stack.append(self.__Queue.popleft())

        self.__push_to_stack = not self.__push_to_stack
        self.__last_elem = el

        return el

    def poll(self):
        return self.__last_elem

    def is_empty(self):
        return len(self.__Stack)


    def find_middle(self):
        if len(self.__Stack) > 0:
            return self.__Stack[-1]
        else:
            assert (len(self.__Queue) == 0)
            raise IndexError("Cannot Poll Empty Stack")

    def delete_middle(self):
        el = self.__Stack.pop()

        if self.__push_to_stack:
            self.__Stack.append(self.__Queue.popleft())

        self.__push_to_stack = not self.__push_to_stack
        return el

if __name__ == "__main__":
    m = MiddleStack(data=range(1,11))
    print(m.poll())
    print(m.find_middle())
    for i in range(5):
        print(m.delete_middle())