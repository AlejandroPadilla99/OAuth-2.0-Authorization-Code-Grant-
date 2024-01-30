from connection import get_cursor

cursor = get_cursor()

def daos_get_user(email: str, password: str) -> str:
    query = """
        SELECT uuid FROM users
        WHERE email = ? AND password = ?
    """

    try:
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        return result[0] if result else None

    except Exception as e:
        print("something wrong on the daos")
