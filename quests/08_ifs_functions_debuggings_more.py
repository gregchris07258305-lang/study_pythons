# ✅ 문제 6 — 함수 내부 변수 오타
# 아래 함수는 섭씨 값으로 변환해 반환해야 하지만, 내부 변수의 오타로 인해 오류가 발생한다.
#  오류를 찾고 해결하시오.
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9   # 오타 수정
    return celsius

print(to_celsius(77))


# ✅ 문제 7 — return 위치 오류
# 아래 프로그램은 반복문 안에서 함수를 호출하지만,
#  함수 내부의 return 위치가 잘못되어 의도한 값이 계산되지 않는다.
#  오류를 수정하시오.
def to_celsius(temp):
    if temp > 0:
        celsius = (temp - 32) * 5 / 9
        return celsius             # 잘못된 위치

print(to_celsius(50))


# ✅ 문제 8 — 함수 재사용 시 논리 오류
# 아래 코드는 temp 값을 3개 변환하려고 하지만,
#  변수 재사용과 return 값 처리에서 오류가 발생한다.
#  오류를 찾고 해결하시오.
def to_celsius(temp):
    celsius = (temp - 3) * 5 / 9
    return celsius

temp = 77
result1 = to_celsius(temp)

temp = 95
result2 = to_celsius(temp) 
temp = 50
result3 = to_celsius(temp)

print(result1, result2, result3)


# ✅ 문제 9 — 리스트 값 변환 시 타입 오류
# 아래 코드는 리스트의 모든 값을 to_celsius()로 변환하려 하지만,
#  리스트를 잘못 전달해서 오류가 발생한다.
#  오류를 고치시오.
def to_celsius(temp):
    return (temp - 3) * 5 / 9

temps = [77, 95, 50]
for t in temps:
    value = to_celsius(t)    # 리스트의 각 요소 전달
    print(value)


# ✅ 문제 10 — 함수 반환값을 활용한 조건문 오류
# 아래 코드에서 조건 검사 부분이 잘못되어 조건이 항상 False가 된다.
#  의도: 변환된 섭씨 값이 20보다 크면 "warm" 출력
#  오류를 수정하시오.
ss = input("온도를 입력하시오: ")

def to_celsius(temp):
    return (temp - 32) * 5 / 9

if to_celsius(int(ss)) > 20:       # 77은 임의의 온도값. 이 부분에 임의로 입력해야함.
    print("warm")
else:
    print("cold")

