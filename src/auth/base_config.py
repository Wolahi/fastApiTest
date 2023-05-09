import os

from dotenv import load_dotenv
from fastapi_users.authentication import AuthenticationBackend, JWTStrategy, BearerTransport


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

load_dotenv()
JWT_KEY = os.environ.get("JWT_KEY")
SECRET = JWT_KEY


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=SECRET,
        lifetime_seconds=3600,
        algorithm="HS256",
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)










