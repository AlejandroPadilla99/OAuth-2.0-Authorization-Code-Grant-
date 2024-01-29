OAuth 2.0 - Authorization Code Grant - Python
-

```text
     +----------+
     | Resource |
     |   Owner  |
     |          |
     +----------+
          ^
          |
         (B)
     +----|-----+          Client Identifier      +---------------+
     |         -+----(A)-- & Redirection URI ---->|               |
     |  User-   |                                 | Authorization |
     |  Agent  -+----(B)-- User authenticates --->|     Server    |
     |          |                                 |               |
     |         -+----(C)-- Authorization Code ---<|               |
     +-|----|---+                                 +---------------+
       |    |                                         ^      v
      (A)  (C)                                        |      |
       |    |                                         |      |
       ^    v                                         |      |
     +---------+                                      |      |
     |         |>---(D)-- Authorization Code ---------'      |
     |  Client |          & Redirection URI                  |
     |         |                                             |
     |         |<---(E)----- Access Token -------------------'
     +---------+ 
```

This code is base on [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) following are the steps.

Step 1: Client Identifier and Redirection URI
-
In this step, the web application requests permission from the user to authorize access to their account hosted at a third-party OAuth2 provider.

The web application constructs a URL like:
```
https://authorization_server.com/login
  ?response_type=code
  &client_id=123
  &redirect_uri=https://your-web-app.com/redirect
  &scope=write,read
  &state=1234-zyxa-9134-wpst
```
Information on the request permission
- **Response Type** - tells the authorization server which flow or grant to use (use code for the Web Application Flow)
- **Client ID** - identifies the web application
- **Redirect URI** - where to redirect the user back to
- **Scope** - specifies which portion(s) of the user profile the web application wishes to access
- **State** - is a randomly-generated string that the web application provides, which the authorization server will simply pass back so that the web application can then validate to mitigate fraud

Step 2: User authenticates
-
The authorization server authenticates the resource owner and establishes whether the resouce owner grants or denies the client's access request.

```
add a image here in the future please :3
```

Step 3: Authorization Code
-
Assuming the resource owner grants access, the authorization server redirects the user-agent back to the client using the redirection URI provided earlier. The redirection URI includes an authorization code and any additional state provided by the client earlier.

Example:
```
https://client_server.com/redirect 
  ?code=123456
  &state=1234-zyxa-9134-wpst
```

Step 4: Autorization Code
-
The client request an access token from the autorization server's token endpoint endpoint by including the authorization code received in the previous step.  When making the request, the client authenticates with the authorization server.  The client includes the redirection URI used to obtain the authorization code for verification.

Example:
```
POST authorization_server.com/oauth/token
 
code=123456
&grant_type=code
&client_id=mRkZGFjM
&client_secret=ZGVmMjMz
```

Step 5: Access token 
-
The authorization server authenticates the client, validates the authorization code, and ensures that the redirection URI received matches the URI used to redirect the client in step 3.  If valid, the authorization server responds back with an access token and, optionally, a refresh token.

Example:
```json
{
  "access_token": "AYjcyMzY3ZDhiNmJkNTY",
  "refresh_token": "RjY2NjM5NzA2OWJjuE7c",
  "token_type": "Bearer",
  "expires": 3600
}
```