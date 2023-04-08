from algorithms.sorting.swap_elements import swap_element


def bubbleSort(arr, n):
    for i in range(n):
        for j in range(i, 0, -1):
            print(arr[j], arr[j - 1])
            if arr[j] < arr[j -1]:
                arr = swap_element(arr, j , j -1)




if __name__ == '__main__':
    bubbleSort([2,5,3,2,9,7,2,9,1,1], 10)