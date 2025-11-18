# ✅ 문제 1 — 변수 이름 오류 찾기
# 다음 코드를 실행하면 오류가 발생한다.
#  오류 원인을 찾고 수정하시오.

first = 5   # 오타

while first > 0:
    print(f"while 값 : {first}")
    first = first - 1

# ✅ 문제 2 — 들여쓰기(Indentation) 오류 찾기
# 다음 코드는 while 문에서 들여쓰기 오류가 난다.
#  오류를 찾고 수정하시오.
first = 5

while first > 0:
    print(f"while 값 : {first}")  # 들여쓰기 문제
    first = first - 1

# ✅ 문제 3 — 논리적 오류(조건문) 찾기
# 다음 프로그램은 first가 3일 때 break가 실행되야 하는데,
#  현재는 잘못된 조건 때문에 break가 실행된다.
# 코드를 분석해 오류를 수정하시오.
first = 5

while first > 0:
    print(f"while 값 : {first}")
    if first == 3:     # 실제로는 first == 3 에서 break해야 하는 문제 조건
        print("break 실행")
        break
    first = first - 1

