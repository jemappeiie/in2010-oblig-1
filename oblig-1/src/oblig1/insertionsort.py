import sys


def main():
    # Read input
    A = [int(line) for line in sys.stdin]

    insertionsort(A)

    # Print result
    for num in A:
        print(num)


def insertionsort(A):
    for i in range(len(A)):  # loop over the entire list (foreach elem)
        j = i  # pointer to current unsorted elem
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]  # swap A[j] with A[j-1]
            j = j - 1


"""
Core idea:
For each element in an unsorted array A, 
iterate from the beginning to the end.
For each unsorted element check the left element value and current element value (execept first index 0)
if the left element's value is higher than our current element value
then swap the left value and the current value (making the higher value go to the right / sort low-high)
go to the next iteration

Features: 
- Zero extra space complexity because of sorting in-place
"""

if __name__ == "__main__":
    main()
