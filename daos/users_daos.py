from connection import get_db_objects

conection, cursor = get_db_objects()

def daos_insert_user(username: str, email: str, password: str) -> dict:
    query = """
        INSERT INSTO USER (username, email, password)
        VALUES (?,?,?)
    """
    try:
        cursor.execute(query, (email, password))
        result = cursor.fetchone
    except Exception as e:
        print("somthing wrong on the daos")

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
