from datetime import datetime, timedelta

from jose import jwt, JWTError
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from src.schemas import auth as auth_schemas
from src.core.settings import settings
from src.db.models.user import User
from src.repos.user import UserRepo


class Authenticator:
    _algorithm = "HS256"
    _access_token_expires_minutes = 60

    auth_scheme = OAuth2PasswordBearer(tokenUrl="auth/access-token")
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    _secret_key = settings.jwt_secret_key

    def validated_token_payload(self, access_token: str) -> auth_schemas.TokenPayload:
        try:
            payload = jwt.decode(
                access_token, key=self._secret_key, algorithms=[self._algorithm]
            )
            return auth_schemas.TokenPayload(**payload)
        except JWTError:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_access_token(self, user: User) -> str:
        to_encode = {
            "sub": auth_schemas.TokenPayload(user=user).model_dump_json(),
            "exp": datetime.utcnow()
            + timedelta(minutes=self._access_token_expires_minutes),
        }
        encoded_jwt = jwt.encode(to_encode, self._secret_key, algorithm=self._algorithm)
        return encoded_jwt

    async def authenticate_user(
        self, user_repo: UserRepo, username: str, password: str
    ) -> User | None:
        user = await user_repo.get_by_username(username)
        if not user:
            return

        if not self.verify_password(password, user.hashed_password):
            return

        return user
