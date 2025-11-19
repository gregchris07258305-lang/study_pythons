# temp = 77
# celsius = (temp - 32) * 5 / 9
# print(celsius)
# temp = 95
# celsius = (temp - 32) * 5 / 9
# print(celsius)
# temp = 50
# celsius = (temp - 32) * 5 / 9
# print(celsius)


# 변수 재활용 
# temp = 77
# celsius = (temp - 32) * 5 / 9
# print(celsius)
# temp = 95
# celsius = (temp - 32) * 5 / 9
# print(celsius)
# temp = 50
# celsius = (temp - 32) * 5 / 9
# print(celsius)

# 함수 사용
# def function_name(param_first, ... , param_last):
#     # 실행할 코드
#     return return_value

def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius

to_celsius(120)
temp1 = to_celsius(77)
print(temp1)
pass 