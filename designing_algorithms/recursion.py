def rec1(n: int):
    if n > 10:
        return
    print(n)
    rec1(n + 2)
    print(n)


def fib(n):
    # Stop condition
    if n == 0:
        return 0

    # Stop condition
    if n == 1 or n == 2:
        return 1

    # Recursion function
    else:
        return fib(n - 1) + fib(n - 2)


def printFib(n):
    for i in range(0, n):
        print(fib(i), end=" ")


# def towerOfHonai(A, )

if __name__ == '__main__':
    # rec1(1)
    printFib(10)
