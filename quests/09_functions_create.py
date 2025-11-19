# # 공통 사항 : 제출 문제마다 function 실행은 최소 3회 호출

# # 🔹 문제 1
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.
def to_celsius(temp): 
     return (temp - 32) * 5 / 9

def process_temps(temp_list):
    converted_list = []
    for t in temp_list:
        conL = to_celsius(t)
        converted_list = converted_list + [conL]
    return converted_list

def avg_celsius(t1, t2, t3):
    average = (t1 + t2 + t3) / 3
    return average

user_input1 = int(input("첫번째 화씨 온도를 입력하세요 : "))
user_input2 = int(input("두번째 화씨 온도를 입력하세요 : "))
user_input3 = int(input("세번째 화씨 온도를 입력하세요 : "))

temps_list = [user_input1, user_input2, user_input3]

converted_temps = process_temps(temps_list)

result = avg_celsius(converted_temps[0], converted_temps[1], converted_temps[2])

print(f"결과 : {result}")

# 🔹 문제 2
# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.
def print_preference(name, lang1, lang2):
    print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")

user_name = input("이름을 입력하세요 : ")
user_lang1 = input("첫 번째 좋아하는 언어를 입력하세요 : ")
user_lang2 = input("두 번째 좋아하는 언어를 입력하세요 : ")

info_list = [user_name, user_lang1, user_lang2]

print_preference(info_list[0], info_list[1], info_list[2])



# 🔹 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.

def sum_valid_scores(scores):
    total = 0
    for score in scores:
        if score >= 60:
            total += score
    return total

input_score1 = int(input("첫번째 점수를 입력하세요 : "))
input_score2 = int(input("두번째 점수를 입력하세요 : "))
input_score3 = int(input("세번째 점수를 입력하세요 : "))

score_list = [input_score1, input_score2, input_score3]

result = sum_valid_scores(score_list) 

print(f"60점 이상 합계 결과 : {result}")

# 🔹 문제 4
# 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.

def combine(str1, str2):
    return str1 + " " + str2

input_text1 = input("첫 번째 단어를 입력하세요 : ")
input_text2 = input("두 번째 단어를 입력하세요 : ")

text_list = [input_text1, input_text2]
result = combine(text_list[0], text_list[1])
print(f"결과 문장 : {result}")


# 🔹 문제 5
# 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.
def to_celsius_list(temps):
    new_temps = []
    for t in temps:
        celsius = (t - 32) * 5 / 9
        new_temps.append(celsius)
    return new_temps

input_temp1 = float(input("1번째 화씨 온도를 입력하세요 : "))
input_temp2 = float(input("2번째 화씨 온도를 입력하세요 : "))
input_temp3 = float(input("3번째 화씨 온도를 입력하세요 : "))

temp_list = [input_temp1, input_temp2, input_temp3]
result_list = to_celsius_list(temp_list)
print(f"변환된 섭씨 리스트: {result_list}")