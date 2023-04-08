def swap_string_consecutive(S):
    for i in range(0, len(S) - 1):
        if S[i] == S[i+1]:
            continue
        # else:



if __name__ == '__main__':
    rest_char = [x for x in "customer"]
    print("".join([hex(ord(x))[2:] for x in rest_char]))