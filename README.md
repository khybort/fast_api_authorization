<div style="text-align:center">
<h1>FastAPI Authorization App</h1>
<h2>Security and Routing</h2>
</div>
<hr style="border: 3px solid #393e46; width:70%; margin:0 auto;">

### Setup 
- Start with the requirements.txt Python libraries: 
    python3 -m venv jwt-venv
    source jwt-venv/bin/activate
    pip3 install -r requirements.txt
python3 main.py
- ```shell
  $ # Create the following structure
  $ tree
  .
  ├── LICENSE
  ├── README.md
  ├── app
  │   ├── __init__.py
  │   ├── api.py
  │   ├── auth
  │   │   └── __init__.py
  │   └── model.py
  ├── main.py
  └── requirements.txt
  
  2 directories, 8 files
  ```
  - In <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">main.py</span> define an entrypoint for the app

### Adding Pydantic models (Schemas)
- Add pydantic schemas for data validation to <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">app.model</span>

### Defining the routes
- Start by importing <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">PostSchema</span> then adding a list of dummy posts and an empty user list variable
    - Add some GET routes to read the fake posts
    - Add a POST route for creating a new post

### JWT Authentication
- Create a JWT token handler and a class to handle bearer tokens 
- Add the following libraries:
    - <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">PyJWT==1.7.1</span>
    - <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">python-decouple==3.3</span>
        - Used for reading environment variables
- JWT Handler
    - The JWT handler will be responsible for signing, encoding, decoding, and returning JWT tokens
    - Add a new module <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">app.auth.auth_handler</span>
    - Define a function that will return generated tokens: <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">token_response</span>
    - Define a function that will sign the token: <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">signJWT</span>
     - Define a function that will decode a token: <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">decodeJWT</span>

### User Registration and Login
Go docs api and signup with example creadentials. Copy the jwt acces token.

### Securing Routes 
- Now, you can protect the route, by checking whether the request is authorized or not. This is done by scanning the request for the JWT in the `Authorization` header. 
- FastAPI provides the basic validation via the `HTTPBearer` class. This class is uesed to extract and parse the token. 
- Then verify the token using the <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">decodeJWT</span> function. 
- Add <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">fastapi_jwt.app.auth.auth_bearer</span>
    - The `JWTBearer` class is a subclass of FastAPI's HTTPBearer class that will be used to persist authentication on the routes
    - The <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">\_\_init__</span> method enables automatic error reporting by setting the boolean `auto_error` to True.
    - In the <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">\_\_call__</span> you define a variable called `credentials` of type `HTTPAuthorizationCredentials`, which is created with the `JWTBearer` class is invoked. You then proceed to check if the credentials passed in during the course of invoking the class are valid:
        - If the credential scheme isn't a bearer scheme, raise an exception for an invalid token scheme.
        - If a bearer token is passed, verify that the JWT is valid 
        - If no credential are received, raise an invalid authorization error.
    - The <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">\_\_verify_jwt__</span> method verifies whether a token is valid. The method takes a `jwttoken` string which it then passes to the `decodeJWT` function and returns a boolean value based on the outcome of `decodeJWT` 
- Dependency Injection 
    - To secure the routes, you'll leverage dependency injection via FasAPI's `Depends`
    - Update imports by adding the `JWTBearer` and `Depends`
        
----------------------------------------------------------------------------
<span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;"></span>

### Reference
- [Authentication in FastAPI](https://testdriven.io/blog/fastapi-jwt-auth/)
