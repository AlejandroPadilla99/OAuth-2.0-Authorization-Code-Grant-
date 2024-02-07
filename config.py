import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    CLIENT_ID = os.getenv('CLIENT_ID', None),
    CLIENT_SECRETE = os.getenv('CLIENT_SECRETE', None),
    EXPECTED_CLIENT_ID = os.getenv('EXPECTED_CLIENT_ID', None),
    EXPECTED_CLIENT_SECRETE = os.getenv('EXPECTED_CLIENT_SECRETE', None),
    SECRET_KEY = os.getenv('SECRET_KEY', None)

env = None
def get_env() -> Env:
    if env:
        return env
    env = Env()
    return env