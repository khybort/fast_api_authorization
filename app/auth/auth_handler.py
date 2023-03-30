import time 
from typing import Dict 

import jwt 
from app.util.settings import settings

# JWT_SECRET = config("edd85cfad0ebf288263854d4279d0d22f717fd4a35b45c6f85af45c40ed50611") 
# JWT_ALGORITHM = config("HS256")
# JWT_SECRET = os.environ["JWT_SECRET"]
# JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
JWT_SECRET = settings.JWT_SECRET 
JWT_ALGORITHM = settings.JWT_ALGORITHM

# Helper function for returning generated tokens
def token_response(token: str) -> dict:
    return {
        "access_token": token
    }

# Function for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id, 
        "expires": time.time() + 600
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

# Return a decoded token if it has not expired
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None 
    except:
        return {}