import psycopg2
import psycopg2.extras
import sys

# ==========================================
# Database Connection (Placeholder)
# ==========================================
DB_HOST = "db_postgresql"
DB_NAME = "main_db"
DB_USER = "admin"
DB_PASSWORD = "admin123"

def get_db_connection():
    """데이터베이스 연결을 생성하고 connection과 cursor를 반환합니다."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to the database. {e}")
        sys.exit(1)

# ==========================================
# Helper Function
# ==========================================
def print_books(title, books):
    """도서 목록을 보기 좋게 출력하는 함수"""
    print(f"\n--- {title} ---")
    if not books:
        print("  (No books found)")
        return
    for book in books:
        # book[0] is id (UUID), book[1] is title, book[2] is price
        print(f"  ID: {book[0]}, Title: {book[1]}, Price: {book[2]}")
    print("-" * (len(title) + 8))

# ==========================================
# Problem 1: Create Table
# ==========================================
def create_books_table(conn):
    """
    books 테이블을 생성합니다.
    - 스키마: id (UUID PK, default uuid_generate_v4()), title (VARCHAR 100), price (INT)
    """
    with conn.cursor() as cur:
        # Enable uuid-ossp extension if not exists
        cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
        
        # Drop table if it exists to ensure a clean slate for the script
        cur.execute("DROP TABLE IF EXISTS books;")
        
        create_table_query = """
        CREATE TABLE books (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            title VARCHAR(100) NOT NULL,
            price INT NOT NULL
        );
        """
        cur.execute(create_table_query)
        conn.commit()
    print("books 테이블이 생성되었습니다.")

# ==========================================
# Problem 2: Insert Data
# ==========================================
def insert_books(conn):
    """
    books 테이블에 3건의 데이터를 삽입합니다.
    """
    books_to_insert = [
        ('파이썬 입문', 19000),
        ('알고리즘 기초', 25000),
        ('네트워크 이해', 30000)
    ]
    
    insert_query = "INSERT INTO books (title, price) VALUES %s;"
    
    with conn.cursor() as cur:
        psycopg2.extras.execute_values(
            cur, insert_query, books_to_insert
        )
        conn.commit()
    print("3개 도서가 삽입되었습니다.")

# ==========================================
# Problem 3: Select Functions
# ==========================================
def get_all_books(conn):
    """books 테이블의 모든 데이터를 조회하여 반환합니다."""
    with conn.cursor() as cur:
        cur.execute("SELECT id, title, price FROM books ORDER BY price;")
        return cur.fetchall()

def get_expensive_books(conn):
    """가격이 25000원 이상인 도서를 조회하여 반환합니다."""
    with conn.cursor() as cur:
        cur.execute("SELECT id, title, price FROM books WHERE price >= 25000 ORDER BY price;")
        return cur.fetchall()

def get_book_by_title(conn, title):
    """제목으로 특정 도서를 조회하여 반환합니다."""
    with conn.cursor() as cur:
        cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
        return cur.fetchall()

# ==========================================
# Problem 4: Update Data
# ==========================================
def update_second_book_price(conn):
    """
    현재 저장된 순서(가격 기준)에서 2번째 도서의 가격을 27000으로 수정합니다.
    """
    all_books = get_all_books(conn)
    if len(all_books) < 2:
        print("Error: Not enough books to update the second one.")
        return

    second_book_id = all_books[1][0] # 0 for id
    
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE books SET price = %s WHERE id = %s;",
            (27000, second_book_id)
        )
        conn.commit()
    print("두 번째 도서 가격이 27000으로 수정되었습니다.")

# ==========================================
# Problem 5: Delete Data
# ==========================================
def delete_third_book(conn):
    """
    수정 후 현재 저장된 순서(가격 기준)에서 3번째 도서의 UUID를 가져와 삭제합니다.
    """
    all_books = get_all_books(conn)
    if len(all_books) < 3:
        print("Error: Not enough books to delete the third one.")
        return
        
    third_book_id = all_books[2][0] # 0 for id
    
    with conn.cursor() as cur:
        cur.execute("DELETE FROM books WHERE id = %s;", (third_book_id,))
        conn.commit()
    print("세 번째 도서가 삭제되었습니다.")


# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    conn = get_db_connection()
    try:
        # 문제 1: 테이블 생성
        create_books_table(conn)
        
        # 문제 2: 데이터 삽입
        insert_books(conn)
        
        # 문제 3: 조회
        all_books = get_all_books(conn)
        print_books("전체 도서 목록", all_books)
        
        expensive_books = get_expensive_books(conn)
        print_books("가격이 25000원 이상인 도서", expensive_books)

        book = get_book_by_title(conn, '파이썬 입문')
        print_books("'파이썬 입문' 검색 결과", book)

        # 문제 4: 데이터 수정
        update_second_book_price(conn)
        all_books_after_update = get_all_books(conn)
        print_books("수정 후 전체 도서 목록", all_books_after_update)
        
        # 문제 5: 데이터 삭제
        delete_third_book(conn)
        all_books_after_delete = get_all_books(conn)
        print_books("삭제 후 전체 도서 목록", all_books_after_delete)

    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")