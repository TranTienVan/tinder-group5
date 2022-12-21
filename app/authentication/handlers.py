import jwt
import datetime
import os
from rest_framework.exceptions import AuthenticationFailed

SECRET_KEY = os.environ.get("JWT_SECRET")
ALGORITHM = 'HS256'
EXP_TIME = 60
JWT_COOKIE = os.environ.get("JWT_COOKIE")

class JWTHandler():
    @staticmethod
    def generate_token(user, key = SECRET_KEY, algorithm = ALGORITHM):
        """ Generate JWT token """
        payload = {
            "id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes = EXP_TIME),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, key, algorithm)
        return token

    @staticmethod
    def verify_token(token, key = SECRET_KEY, algorithm = ALGORITHM):
        """ Verify JWT token """
        payload = jwt.decode(token, key, algorithm)
        return payload['id']

    @staticmethod
    def get_current_user(cookies, key = SECRET_KEY, algorithm = ALGORITHM):
        """ Get current user id """
        token = cookies.get(JWT_COOKIE)

        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        
        try:
            id = JWTHandler.verify_token(token)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")

        return id
    
