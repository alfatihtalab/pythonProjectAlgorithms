def solution(message, K):
    final_msg = ""

    listed_msg = message.split(" ")
    for i in listed_msg:
        if i == " ":
            listed_msg.remove(i)

    total_len_word = sum(len(i) for i in listed_msg)
    if total_len_word < K:
        print(listed_msg)
    for i in listed_msg:
        listed_msg.pop()
        total_len_word = sum(len(i) for i in listed_msg)
        if (total_len_word >= K):
            print(" ".join(listed_msg))



def solution2(P, S):
    # write your code in Python 3.6
    # write your code in Python 3.6
    p_len = len(P)
    # s_len = license
    free_s = 0
    no_s = 0
    for i in range(p_len):
        if S[i] > P[i]:
            free_s += 1
        no_s += 1

    if no_s == 1:
        return free_s
    elif no_s > 1 and free_s == 1:
        return p_len - free_s
    else:
        return free_s


if __name__ == '__main__':
    print(solution2([1, 4, 1], [1, 5, 1]))

