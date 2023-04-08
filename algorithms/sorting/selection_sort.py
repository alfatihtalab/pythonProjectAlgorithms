# O(N^2)
'''
Algorithm:
SELECTION-SORT(A)
N = A.length
for i= 1 to N
    k = A[i]
    Min_index = i
    for j = i+1 to N
        if A[j] < A[Min_index]
            Min_index = j
    A[i] = A[Min_index]
    A[Min_index] = k

'''


def selection_sort(A):
    N = len(A)
    for i in range(N - 1):
        k = A[i]
        min_index = i
        for j in range(i + 1, N):
            if A[j] < A[min_index]:
                min_index = j
        A[i] = A[min_index]
        A[min_index] = k
    return A


if __name__ == '__main__':
    print(selection_sort([9, 8, 7, 5, 4, 7, 2, 3, 1]))
