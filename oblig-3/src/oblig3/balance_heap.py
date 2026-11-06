import heapq
import sys


def main():
    heap = PriorityQueue()
    for line in sys.stdin:
        heap.insert(int(line))

    print_balanced(heap)


def print_balanced(heap):
    # Base case
    if heap.size() == 0:
        return

    left_heap = PriorityQueue()

    # Move the smallest len(heap) // 2
    # elements from heap into left_heap
    left_count = heap.size() // 2
    for i in range(left_count):
        left_heap.insert(heap.removemin())

    # Pop and print the middle element
    print(heap.removemin())

    # Recursively process left_heap
    print_balanced(left_heap)

    # Recursively process the remaining heap
    print_balanced(heap)


class PriorityQueue:
    def __init__(self):
        self._items = []

    def insert(self, value):
        heapq.heappush(self._items, value)

    def removemin(self):
        return heapq.heappop(self._items)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    main()
