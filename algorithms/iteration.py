def solution(T):
    for t in T:
        print(t)


def range_of_values(T, n):
    for t in range(0, n):
        print(t)


def recursive(Number):
    while Number > 2:
        # recursive(Number)
        print(Number)
        Number /= 2


if __name__ == '__main__':
    arr = [5, 3, 6, 9, 7, 5, 4, 2, 5, 4]
    # solution([5,3,6,8,72,2])
    # print(len(arr))
    # range_of_values(arr, 10)
    recursive(80)