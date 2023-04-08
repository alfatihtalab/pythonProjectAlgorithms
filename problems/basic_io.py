# //divisible
def solve(A):
    A = list(map(str, A))
    n_length = False
    i_size = False
    for i in A:
        if int(i) >= 1 and int(i) <= 100000:
            n_length = True
    for i in A:
        if int(i) >= 1 and int(i) <= 100000:
            i_size = True
    is_even = False
    if len(A) % 2 == 0:
        is_even = True

    if is_even and n_length and i_size:
        mid = len(A) // 2
        R, L = A[:mid], A[mid:]
        temp = ""
        for i in R:
            temp += i[0]
        for i in L:
            temp += i[-1]

        if int(temp) % 11 == 0:
            return "OUI"
        return "NON"
    return "NON"


if __name__ == '__main__':
    # N = int(input())
    # A = list(map(str, input().split()[:N]))
    #
    # print(N, A)
    # for i in A:
    #     print(i)
    # N = int(input())
    # A = map(int, input().split())
    #
    # out_ = solve(A)
    # print(out_)

    # set_one = set([1,1,1,2,3,55,5,6,2,3])
    # print(isinstance(7, int))
    #
    # car_complex = 5 + 8j
    # print(isinstance(car_complex, complex))
    # x,y,a,b = list(map(str, input().split()[:4]))
    # print(int(x) * int(y) == int(a) + int(b))

    # x_iter = iter([print('x') in range(9)])
    # print((type(x_iter)))
    my_list = ["google", "twitter", "amazon"]
    for i, v in enumerate(my_list):
        print(i, v)
    print()
    person1_information = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps"}
    print(person1_information.items())
    for i in person1_information.items():
        print(i)

    print(person1_information.values())

    for v in person1_information:
        print(v)
