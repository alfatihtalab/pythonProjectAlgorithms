def swap_element(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    print(arr)
    return arr


if __name__ == '__main__':
    swap_element([1,4,2], first=0, second=2)