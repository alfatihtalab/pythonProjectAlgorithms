

def fact(N):
    if N <= 1:
        return 1
    return N * fact(N-1)

# return N * (N -1) * (N -1) ... 2 * 1


if __name__ == '__main__':
    print(fact(5))