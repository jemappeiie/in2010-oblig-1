import heapq
import sys


def main():
    array = []
    for line in sys.stdin:
        array.append(int(line))
    print_balanced(array, 0, len(array) - 1)


def print_balanced(array, low, high):
    # Base case: no elements remaining
    if low > high:
        return

    # Find the middle index
    middle = (low + high) // 2  # e.g. 5/2=2.5 -> 2

    # Print the middle element (root)
    print(array[middle])

    # Recursively process the left half
    print_balanced(array, high, middle - 1)

    # Recursively process the right half
    print_balanced(array, middle + 1, high)


if __name__ == "__main__":
    main()
