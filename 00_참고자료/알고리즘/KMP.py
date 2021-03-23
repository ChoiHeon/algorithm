# https://www.acmicpc.net/problem/1305


def lps(p):
    table = [0] * l   # table[k] -> 0~k까지 부분 문자열에서 일치하는 접두사와 접미사가 있을 때,
                      #             접두사의 길이 또는 접두사 다음 인덱스를 의미
    j = 0  # 접두사, 접미사가 일치하는 길이를 의미
    for i in range(1, l): # i -> 부분 문자열의 길이를 의미
        # j > 0 -> 접두사, 접미사가 일치한 적이 있음
        # p[i] != p[j] ->
        while j > 0 and p[i] != p[j]:  # j > 0 -> 접두사, 접미사가 일치한 적이 있음
                                       # p[i] != p[j] ->
            j = table[j - 1]  # 더 이전 부분문자열의 접두사의 다음 인덱스를 j에 저장
        if p[i] == p[j]:
            j += 1
            table[i] = j

    return l - table[l-1]


l = int(input())
s = input()
print(lps(s))