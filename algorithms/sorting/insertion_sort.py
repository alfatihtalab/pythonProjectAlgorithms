# O(N^2)
def insertion_sort(A, n):
    for i in range(1, n):
        k = A[i]
        j = i - 1
        while j >= 0 and A[j] > k:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = k
    print(A)


def insertion_sort2(A):
    N = len(A)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if A[j - 1] <= A[j]:
                break
            A[j], A[j - 1] = A[j - 1], A[j]


if __name__ == '__main__':
    insertion_sort([5, 4, 7, 5, 3, 8], 5)
