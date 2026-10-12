import fileinput


def main():
    # Read input
    A = [int(line) for line in fileinput.input(encoding="utf-8")]

    A = mergesort(A)

    # Print result
    for num in A:
        print(num)


def merge(A_1, A_2, A):
    i = 0
    j = 0
    while i < len(A_1) and j < len(A_2):
        if A_1[i] <= A_2[j]:
            A[i + j] = A_1[i]
            i += 1
        else:
            A[i + j] = A_2[j]
            j += 1
    while i < len(A_1):
        A[i + j] = A_1[i]
        i += 1
    while j < len(A_2):
        A[i + j] = A_2[j]
        j += 1
    return A


def mergesort(A):
    n = len(A)
    if n <= 1:
        return A
    i = n // 2
    A_1 = mergesort(A[:i])
    A_2 = mergesort(A[i:])

    return merge(A_1, A_2, A)


"""
Core idea: Divide (Split) and conquer (Merge)
Split original array into cirka two equally big arrays.
Continue splitting the obtained arrays recursivelly until you reach the base case, i.e. arrays of length one.
"""


if __name__ == "__main__":
    main()
