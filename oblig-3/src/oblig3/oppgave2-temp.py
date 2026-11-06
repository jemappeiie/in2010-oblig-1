import sys


def balanced_order(numbers, left, right):
    # Base case: no elements remaining
    if left > right:
        return

    # Find the middle index
    middle = len(numbers) // 2  # e.g. 5/2=2.5 -> 2

    # Print the middle element
    print(numbers[middle])

    # Recursively process the left half
    print(balanced_order(numbers[0 : middle - 1], left, middle - 1))

    # Recursively process the right half
    print(balanced_order(numbers[middle + 1 : len(numbers) - 1], middle + 1, right))


def main():
    numbers = [int(line) for line in sys.stdin]
    balanced_order(numbers, 0, len(numbers) - 1)


if __name__ == "__main__":
    main()
