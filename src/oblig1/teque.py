from sys import stdin
from math import floor
from collections import deque


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

"""b
    I don't freaking know???

    def balance(self): O(67)

    def pushback(self, x): O(69)
    
    def pushfront(self, x): O(420)

    def pushmiddle(self, x): O(42)

    def get(self, i): O(1337)

"""
