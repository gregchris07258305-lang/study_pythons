# ✅ 문제 1 — return 누락 오류
# 아래 함수는 섭씨 변환 후 값을 반환해야 한다.
#  현재 코드에서 발생하는 오류를 찾고 수정하시오.
# def to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     return celsius

# result = to_celsius(77)
# print(result)

# ✅ 문제 2 — 매개변수 이름 오류
# 아래 프로그램은 실행 시 오류가 발생한다.
#  오류 위치를 찾고 올바르게 수정하시오.
# def convert(temp):
#     return (temp - 3) * 5 / 9   # 오타 수정: temps -> temp

# print(convert(95))
# ✅ 문제 3 — 함수 호출 인자 오류
# 아래 코드는 함수 호출이 잘못되어 있다.
#  오류를 설명하고 고치시오.
# def to_celsius(temp):
#     return (temp - 32) * 5 / 9

# value = to_celsius()# 오류 설명: to_celsius 함수는 하나의 인자를 필요로 하지만, 호출 시 인자가 제공되지 않음.
# print(value)

# ✅ 문제 4 — 타입 오류(TypeError)
# 아래 코드는 문자열을 함수에 전달하여 오류가 발생한다.
#  이 오류가 왜 발생하는지 설명하고 해결하시오.
# def to_celsius(temp):
#     return (temp - 3) * 5 / 9

# print(to_celsius(77)) # 오류 설명 : 문자열 타입은 "" 사용할 수 없기 때문에 TypeError가 발생함

# ✅ 문제 5 — 반복 구조 + 함수 사용 오류
# 아래 코드는 여러 값을 함수로 변환하려 하지만 오류가 발생한다.
#  오류 원인을 찾고 고치시오.(Option : for 문을 함수화)

def to_celsius(temp):
    """단일 온도를 변환하는 함수"""
    return (temp - 32) * 5 / 9

def process_temps(temp_list):
    """
    [Option 수행]
    리스트를 받아 내부에서 반복문(for)을 돌고,
    변환된 새 리스트를 반환하는 함수
    """
    converted_list = []
    for t in temp_list:
        val = to_celsius(t)
        converted_list.append(val)
    
    return converted_list

# 메인 실행 로직
temps = [77, 95, 50]
results = process_temps(temps)  # 함수 호출 한 번으로 처리

print(results)


