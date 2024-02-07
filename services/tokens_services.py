from flask import Flask, jsonify
from pprint import pprint
import jwt
from datetime import datetime, timedelta

from config import get_env

env = get_env()

def get_oauth_code() -> str:
    payload = {
        "expires_in": 3600,
    }

    code = jwt.encode(payload=payload, key=env.SECRET_KEY, algorithm="HS256")

    return code

def get_request_permission_data(args: dict) -> dict:
    try:
        query_params = {
            'client_id': args.get('client_id'),
            'redirect_uri': args.get('redirect_uri'),
            'response_type': args.get('response_type'),
            'scope': args.get('scope'),
            'state': args.get('state') 
        }
    except Exception as e:
        query_params = None
    return query_params

def get_client_token() -> str:
    return ""

def get_grant_token() -> str:
    #the following data is for test
    uuid = "550e8400-e29b-41d4-a716-446655440000"
    

    payload = {
        "uuid": uuid,
        "exp": datetime.utcnow() + timedelta(days=1),
        "permissions": ["read", "write"]
    }

    acces_token = jwt.encode(payload=payload, key=env.SECRET_KEY, algorithm="HS256")
    refresh_token = "12345"

    body_response = {
        "access_token": acces_token,
        "refresh_token": refresh_token,
        "expires_in": 3600,
        "token_type": "bearer"
    }
    response = jsonify(body_response)
    response.status_code = 200
    pprint(response)
    return response


def valid_authorization_code(data: str) -> bool:
    try:
       if env.EXPECTED_CLIENT_ID == data.get('client_id') and env.CLIENT_SECRETE == data.get("client_secret") and "123456" == data.get["code"]:
           print("is true")
           return True
    except Exception as e:
        return False
    
def valid_client_id(client_id: str) -> bool:
    if env.EXPECTED_CLIENT_ID == client_id:
        return True
    return False