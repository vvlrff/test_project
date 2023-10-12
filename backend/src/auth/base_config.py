from fastapi_users import FastAPIUsers
from fastapi_users.authentication import BearerTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from ..auth.models import User
from ..auth.manager import get_user_manager

bearer_transport = BearerTransport(tokenUrl="auth/login")
SECRET = 'olimpiad_forever' # Поставить в файл .env


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=72000)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
