from connection import get_db_objects

connection, cursor = get_db_objects()

def daos_create_token_for_user(user_uuid: str) -> bool:
   query = """
        INSERT INTO tokens (user_uuid)
        VALUES (?)
    """
   try:
        cursor.execute(query, (user_uuid,))
        connection.commit()
        # Assuming you want to commit the changes after executing the query
        return True
   except Exception as e:
        print(f"Error creating token for user: {e}")
        # Return False if the insertion fails
        return False
 
def daos_insert_code(user_uuid: str, code: str) -> bool:
    query = """
        INSERT INTO tokens (code) 
        WHERE user_uuid = ?
        VALLUES ?
    """
    try:
        cursor.execute(query,(user_uuid))
    except Exception as e:
        return False

ans = daos_create_token_for_user(user_uuid="550e8400-e29b-41d4-a716-446655440000")
print(ans)