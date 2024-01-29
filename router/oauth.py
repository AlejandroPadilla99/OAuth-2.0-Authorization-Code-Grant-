from flask import Blueprint, redirect, request, session, jsonify

#services
from services.tokens_services import get_oauth_code, get_request_permission_data, valid_authorization_code, get_grant_token

oauth = Blueprint('oauth', __name__)

@oauth.route("/oauth/login", methods=['GET'])
def oauth_login():
    query_params = get_request_permission_data(args=request.args)
    if query_params:
        session['query_params'] = query_params
        return redirect("/login")
    else:
        error_response = {
            'message': "Error"
        }
        return jsonify(error_response), 500 
       

@oauth.route("/oauth/authorize", methods=['POST'])
def oauth_authorize():
    code = get_oauth_code()
    query_params = session.get('query_params')
    callback_url = query_params['redirect_uri']
    location = f"{callback_url}?code={code}"
    location += "&state=" + query_params['state']
    return redirect(location, code=302)

@oauth.route("/oauth/token", methods=['POST'])
def oauth_token():
    if valid_authorization_code(request.form):
        print("token endpoint")
        response = get_grant_token()
        return response
    else:
        error_response = {
            'message': "Error"
        }
        return jsonify(error_response), 500 



