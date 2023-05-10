from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    surname: str
    avatar: str
    bg_img: str
    edu: str
    num_telephone: str
    info: str
    city: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserUpdate(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    surname: str
    avatar: str
    bg_img: str
    edu: str
    num_telephone: str
    info: str
    city: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    username: str
    surname: str
    avatar: str
    bg_img: str
    edu: str
    num_telephone: str
    info: str
    city: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
