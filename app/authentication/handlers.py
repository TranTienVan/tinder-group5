import jwt
import datetime
import os

SECRET_KEY = os.environ.get("JWT_SECRET")
ALGORITHM = 'HS256'
EXP_TIME = 60

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

    
