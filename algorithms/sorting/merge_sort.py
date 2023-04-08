# the subarray A[p : r] from A[1 : n]
# q = (p + r) /2
# O(N log N)
def merge(A, q):
    # q = len(A) // 2

    left, right = [], []

    for i in range(0, q):
        left.append(A[i])

    for i in range(q, len(A)):
        right.append(A[i])

    print("left = ", left, "right =", right)
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1

    print(A)
    # return A


'''
MERGE-SORT(A, p, r)
1 if p ≥ r // zero or one element?
2 return
3 q = ⌊(p + r)/2⌋ // midpoint of A[p : r]
4 MERGE-SORT(A, p, q) // recursively sort A[p : q]
5 MERGE-SORT(A, q + 1, r) // recursively sort A[q + 1 : r]
6 // Merge A[p : q] and A[q + 1 : r] into A[p : r].
7 MERGE(A, p, q, r)
'''

def merge_two(arr):
    mid = len(arr) // 2

    # Dividing the array elements
    L = arr[:mid]

    # into 2 halves
    R = arr[mid:]
    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(A):
    if len(A) > 1:
        q = len(A) // 2

        # Dividing the array elements
        L = arr[:q]

        # into 2 halves
        R = arr[q:]
        print(q)
        # q = q.__floor__()
        merge_sort(L)
        merge_sort(R)

        # merge_sort(A[q+1:], q)
        # print(A[q+1:])

        merge_two(A)
    return

    # merge_sort(A, q, r)
    # merge(A, p, q, r)


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [2, 4, 20, 7, 6, 7, 1, 2, 3, 5]
    # merge(arr,0)
    mergeSort(arr)
    # merge_sort(arr)
    # print((5 / 2).__floor__())
    print(arr)

    # print(7 // 2)  aaaaaaaaaaaa
