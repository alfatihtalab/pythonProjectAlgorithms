'''
Partitioning the array

PARTITION(A, p, r)
1 x = A[r] // the pivot
2 i = p – 1 // highest index into the low side
3 for j = p to r – 1 // process each element other than the pivot
4 if A[j] ≤ x // does this element belong on the low side?
5 i = i + 1 // index of a new slot in the low side
6 exchange A[i] with A[j]
// put this element there
7 exchange A[i + 1] with
A[r]
// pivot goes just to the right of the low
side
8 return i + 1 // new index of the pivot
'''


# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


if __name__ == '__main__':
    arr= [234,3,2,5,1,1,2,5,6,7,9]
    # partition(arr, 0, len(arr) - 1)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)








