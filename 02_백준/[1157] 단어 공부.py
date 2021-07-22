# https://www.acmicpc.net/problem/1157

word = [c.upper() for c in input()]
cnt = [0] * 26

for alphabet in word:
    cnt[ord(alphabet) - ord("A")] += 1

if cnt.count(max(cnt)) != 1:
    print("?")
else:
    print(chr(cnt.index(max(cnt)) + ord("A")))


'''
s=input().upper()

# 함수를 변수에 저장
c=s.count

# *_ --> 앞의 데이터들을 무시
# 즉, sorted의 결과의 마지막 데이터2개를 a, b에 저장
# {*s, '?'} --> 입력받은 문자열 s를 분할, '?'를 추가하고 {}을 통해 중복을 제거
# 중복을 제거한 알파벳이 s에 몇 개 있는지에 대해 출력을 받고 이를 토대로 정렬
# 마지막 2개를 확인하여 같은 개수의 알파벳이 있는지 확인할 수 있음
*_,a,b=v=sorted({*s,'?'},key=c)

# 인덱서 []에서 True는 1, False는 0을 의미함
# b가 a가 많다면 [-1]을 의미, 마지막 원소를 가리킨다
# 아니라면 [-0]을 가리키여 첫 번째 원소인 '?'를 가리킨다
print(v[-(c(a)<c(b))])
'''