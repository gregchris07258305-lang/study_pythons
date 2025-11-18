# ✅ 문제 1 — 문자열 포맷 오류 수정하기
# 아래 코드는 문자열을 합치는 과정에서 오류가 발생한다.
#  오류를 찾아서 올바른 코드로 수정하시오.
second = "Programming"
first = f"Welcome to Python Strings {second}"   # 오류 수정

print(first)


# ✅ 문제 2 — while 조건 오류 찾기
# 아래 코드는 first가 문자열인데, while 조건에서 비교 연산을 수행하려고 한다.
#  발생하는 오류를 설명하고, 정상 작동하도록 수정하시오.
first = "Hello Python"
while count > 0:
    print(first)
    count = count - 1


# ✅ 문제 3 — 리스트 누적 합 오류 찾기
# 아래 코드의 오류를 찾고 올바르게 수정하시오.
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_all = 0

for k in kor:
    sum_all = sum_all + k     # 오류 수정
for e in eng:
    sum_all = sum_all + e     # eng 점수도 누적

# 또는 sum() 함수를 사용하면 더 간단합니다.
# sum_all = sum(kor) + sum(eng)
print(f"전체 합계: {sum_all}")


# ✅ 문제 4 — for-range 인덱스 문제 해결
# 아래 코드에서 IndexError가 발생한다.
#  오류 원인을 설명하고 올바른 코드를 작성하시오.
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(len(kor)):    # 오류 수정
    sum_total = sum_total + kor[i] + eng[i]

print(f"과목 총점: {sum_total}")