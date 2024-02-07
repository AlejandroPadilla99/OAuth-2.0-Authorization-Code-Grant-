from daos.users_daos import daos_get_user


def user_exit(email: str, password: str) -> str:
    data = daos_get_user(email=email, password=password)
    if data:
        return data
    return "Error user don't exit"