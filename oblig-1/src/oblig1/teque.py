from sys import stdin
from collections import deque


"""Task 1a"""


class Teque:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def balance(self):
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        elif len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushback(self, x):
        self.right.append(x)
        self.balance()

    def pushfront(self, x):
        self.left.appendleft(x)
        self.balance()

    def pushmiddle(self, x):
        self.left.append(x)
        self.balance()

    def get(self, i):
        return self.left[i] if i < len(self.left) else self.right[i - len(self.left)]


if __name__ == "__main__":
    teque = Teque()
    N = int(stdin.readline())
    for _ in range(N):
        line = stdin.readline().split()
        cmd = line[0]
        num = int(line[1])
        if cmd == "push_back":
            teque.pushback(num)
        elif cmd == "push_front":
            teque.pushfront(num)
        elif cmd == "push_middle":
            teque.pushmiddle(num)
        elif cmd == "get":
            print(teque.get(num))

"""Task 1b
    def balance(self): O(1)
    I don't know how python implements deque(), but a normal deque remove/add/lookup is O(1)
    Dequeue is a dynamic list uses a head and tail pointer to achieve constant time completixy.
    balance() function is only using len(), append(), appendleft(), pop(), popleft(). All these methods by themselves are O(1), making balance() constant time as well

    def pushback(self, x): O(1)
    Constant time for pushback(), it uses balance() and <dequeue>.append() both of which are O(1)
    
    def pushfront(self, x): O(1)
    Constant time for pushfront(), it uses balance() and <dequeue>.appendleft() both of which are O(1)

    def pushmiddle(self, x): O(1)
    Constant time for pushmiddle(), it uses balance() and <dequeue>.append() both of which are O(1)

    def get(self, i): O(1)
    Lookup index[i], len() are all constant time making get() constant as well

    *Note that in reality these functions might not be constant depending on how python interpreter handles alloction.
    KISS 
"""
