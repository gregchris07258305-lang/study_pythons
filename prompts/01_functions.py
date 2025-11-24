import sys

def calculate_all(num1, num2):
    """
    두 숫자를 입력받아 사칙연산 결과를 반환하는 함수
    
    Args:
        num1 (int): 첫 번째 숫자
        num2 (int): 두 번째 숫자
        
    Returns:
        tuple: (덧셈, 뺄셈, 곱셈, 나눗셈_또는_에러메시지)
    """
    
    # 1. 덧셈 (Addition)
    add_result = num1 + num2
    
    # 2. 뺄셈 (Subtraction)
    sub_result = num1 - num2
    
    # 3. 곱셈 (Multiplication)
    mul_result = num1 * num2
    
    # 4. 나눗셈 (Division) - 예외 처리 요구사항 반영
    # 분모(num2)가 0일 경우 'division_error' 문자열 반환
    if num2 == 0:
        div_result = "division_error"
    else:
        div_result = num1 / num2
        
    return (add_result, sub_result, mul_result, div_result)

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    print(f"--- [System] 사칙연산 함수 테스트 시작 ---")
    
    # JSON 명세에 따른 테스트 데이터 (총 10개)
    test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
    test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

    # 데이터 정합성 체크 (Optional but recommended for veterans)
    if len(test_a) != len(test_b):
        print("Error: 두 테스트 리스트의 길이가 다릅니다.")
        sys.exit(1)

    # 테스트 실행 반복문
    # range(len(test_a))를 사용하여 인덱스로 접근
    for i in range(len(test_a)):
        a = test_a[i]
        b = test_b[i]
        
        # 함수 호출
        result = calculate_all(a, b)
        
        # 결과 출력 (가독성을 위해 포맷팅)
        print(f"Test #{i+1}: Input({a}, {b}) => Result: {result}")
        
    print(f"--- [System] 테스트 종료 ---")