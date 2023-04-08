# [1,0,0,0,1,0]
def count_consecutive(A, p):
    max = 0
    count = 1
    first_zero_index = 0
    last_zero_index = 0

    for i in range(0, len(A) - 1):
        if A[i] == p and A[i + 1] == p:
            count = count + 1
            if count > max:
                max = count
        else:
            count = 1
    return max

def binary_gap(N):
    T = [int(x) for x in list(str(int(bin(N)[2:])))]
    k = 0
    count = 0
    max = 0
    for i in range(k, len(T) - 1):
        if T[i] == 1:
            k += 1
            count = 0
        else:
            count += 1
            if count > max:
                max = count
    if k >= 2:
        return max
    return 0



if __name__ == '__main__':
    print([int(x) for x in list(str(int(bin(1041)[2:])))])
    arr = [1,0, 0,0,0,0, 0]
    # print(count_consecutive(arr, 0))

    print(binary_gap(32))