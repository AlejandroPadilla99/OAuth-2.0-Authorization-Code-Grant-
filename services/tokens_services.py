from flask import Flask, jsonify
from pprint import pprint
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta

load_dotenv()

def get_oauth_code() -> str:
    #the following data is for test
    return "123456"

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
    secret_key = "your_secret_key"

    payload = {
        "uuid": uuid,
        "exp": datetime.utcnow() + timedelta(days=1),
        "permissions": ["read", "write"]
    }

    acces_token = jwt.encode(payload=payload, key=secret_key, algorithm="HS256")
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
    print(type(data))
    print(data)
    EXPECTED_CLIENT_ID = os.environ.get("EXPECTED_CLIENT_ID") 
    EXPECTED_CLIENT_SECRET = os.environ.get("EXPECTED_CLIENT_ID")
    try:
       if EXPECTED_CLIENT_ID == data.get('client_id') and EXPECTED_CLIENT_SECRET == data.get("client_secret") and "123456" == data.get["code"]:
           print("is true")
           return True
    except Exception as e:
        return False