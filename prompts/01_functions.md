## 프롬포트 

```python
{
  "prompt_config": {
    "role": "Expert Python Tutor",
    "objective": "Complete the Python function based on the provided skeleton code and specific constraints.",
    "output_format": "Python Code Block"
  },
  "task_description": {
    "title": "Arithmetic Operations with List Data",
    "instructions": [
      "Implement the `calculate_all` function to perform addition, subtraction, multiplication, and division.",
      "Iterate through the provided list data to test the function."
    ]
  },
  "constraints": [
    "Data Structure: Input data must be provided as lists (test_a, test_b).",
    "Data Volume: Ensure there are exactly 10 items in the test data.",
    "Naming Convention: Use 'snake_case' (lowercase + underscore) for all variable names.",
    "Function Logic: The function must return a tuple containing results for (+, -, *, /) in that order.",
    "Exception Handling: If dividing by 0, the division result must be the string 'division_error'."
  ],
  "code_context": {
    "language": "python",
    "skeleton_code": "def calculate_all(num1, num2):\n    # 여기에 사칙연산 구현\n    # return (덧셈, 뺄셈, 곱셈, 나눗셈)\n    pass\n\n# 테스트 리스트 (10개)\ntest_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]\ntest_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]\n\n# 테스트 실행\nfor i in range(10):\n    a = test_a[i]\n    b = test_b[i]\n    result = calculate_all(a, b)\n    print(f\"{a}, {b} => {result}\")"
  }
}
```