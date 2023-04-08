
def devide(A):
    print(A)
    if len(A) > 1:
        q = len(A) // 2
        devide(A[:q])
        devide(A[q:])


    return



if __name__ == '__main__':
    devide([1,2,3,4,4,5,6,7,9])