당신은 20년차 풀스텍 개발자입니다.

나는 vscode의 gemini cli를 활용하여, 하기의 문제를 풀 예정입니다.

하기의 문제를 해결할 수 있는 프롬포트를 제작해주세요.



--제작 조건- -

1. 각 문제에   if '__name__' == '__main__' : 코드  반드시 사용

2. json형식으로 출력

3. 작업 진행 폴더명 : prompts/02_DMLs_functions.py

4. 나의 데이터 베이스 정보 
```python
DB_HOST = "db_postgresql"
DB_NAME = "main_db"
DB_USER = "admin"
DB_PASSWORD = "admin123"
```

--문제--

📌 문제 1 — 테이블 생성 함수 만들기

아래 요구사항에 맞게 **Python 함수(create_books_table())**를 작성하시오.

함수 실행 시 PostgreSQL에 books 테이블이 생성되어야 한다.

✔ 요구사항

테이블명: books

컬럼명

자료형

id

UUID PRIMARY KEY DEFAULT uuid_generate_v4()

title

VARCHAR(100)

price

INT

✨ 출력 예

books 테이블이 생성되었습니다.



📌 문제 2 — INSERT 함수 만들기

아래 데이터를 books 테이블에 추가하는 insert_books() 함수를 작성하시오.

✔ 테스트용 데이터

id

title

price

1

파이썬 입문

19000

2

알고리즘 기초

25000

3

네트워크 이해

30000

🔥 id는 자동 UUID이므로 INSERT 시 제외

✨ 출력 예

3개 도서가 삽입되었습니다.



📌 문제 3 — SELECT 함수 만들기

아래 조건을 만족하는 조회용 Python 함수들을 작성하시오.

✔ 요구 함수

전체 조회 함수



함수명: get_all_books()



가격이 25000원 이상인 데이터 조회 함수



함수명: get_expensive_books()



title 이 “파이썬 입문”인 데이터 조회 함수



함수명: get_book_by_title()



parameter: title



📌 문제 4 — UPDATE 함수 만들기

저장된 순서에서 두 번째 도서의 가격을 27000으로 변경하는 함수를 만드시오.

함수명: update_second_book_price()



옵션:



두 번째 도서의 UUID를 SELECT 로 먼저 가져온 후



UPDATE 를 수행한다.



✨ 출력 예

두 번째 도서 가격이 27000으로 수정되었습니다.



📌 문제 5 — DELETE 함수 만들기

저장된 순서에서 세 번째 도서 데이터를 삭제하는 Python 함수를 작성하시오.

함수명: delete_third_book()



옵션:



SELECT로 UUID 조회 후 DELETE 수행



✨ 출력 예

세 번째 도서가 삭제되었습니다.