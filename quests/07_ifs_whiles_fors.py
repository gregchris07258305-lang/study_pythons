## ✅ 중급 난이도 문제 1 — 문자열과 f-string 활용
first = 'python is fun'
second = 'python'

if first in second :
    print(f"welcome! {first}")

print(f"welcome! {first}")

# ✅ 중급 난이도 문제 2 — while 반복문 응용
# first 변수가 5부터 1까지 감소하도록 while문을 작성하고,
#  first == 2일 때만 "special"을 출력하도록 코드를 작성하시오.
first = 5
while first >= 1:   
    if first == 2:     # 실제로는 first == 3 에서 break해야 하는 문제 조건
        print("special")
    else :
        print(first)
    first = first -1

# ✅ 중급 난이도 문제 3 — 리스트 합계 및 평균 계산
# kor와 eng 리스트가 주어졌을 때,
# 각 학생 점수의 총합을 total_scores 리스트로 저장


# 각 학생 점수 평균을 avg_scores 리스트로 저장


kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
total_scores = []
avg_scores  = []

for t in range(5):
    total_scores = kor[t] + eng[t]
    print( total_scores, end=" ")
print(end="\n")
for e in range(5):
    avg_scores = (kor[e] + eng[e]) / 2
    print(avg_scores, end=" ")
print(end="\n")

# ✅ 중급 난이도 문제 4 — 누적 합과 조건문 결합
# kor 리스트에서 60점 이상인 점수만 누적 합계를 계산하고 출력하시오.
# 조건: for문 사용, 60점 미만은 제외


kor = [70, 80, 90, 40, 50]
total_sum = 0

for score in kor:
    if score >= 60:
        total_sum += score

print(f'누적합계 = {total_sum}')