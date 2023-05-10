from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .auth.base_config import auth_backend
from .auth.manager import get_user_manager
from .auth.models import User, user
from .auth.schemas import UserRead, UserCreate, UserUpdate
from .database import get_async_session
from .friends.modles import friend, FriendTable
from .friends.shemas import Friend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app = FastAPI(
    title="VK TESt"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.post("/friends")
async def create_friends(friends: Friend, db: AsyncSession = Depends(get_async_session)):
    friendUser = FriendTable(user_id=friends.user_id, friend_id=friends.friend_id)
    userFriend = FriendTable(user_id=friends.friend_id, friend_id=friends.user_id)
    db.add(friendUser)
    db.add(userFriend)
    await db.commit()
    await db.refresh(friendUser)
    await db.refresh(userFriend)


@app.get("users/{limit}")
async def get_all_users(limit, db: AsyncSession = Depends(get_async_session)):
    resultUser = await db.execute(select(user).limit(int(limit)))
    userArr = resultUser.all()
    resUse = []
    for userEl in userArr:
        resUse.append(UserRead(id=userEl.id, email=userEl.email, username=userEl.username,
                               surname=userEl.surname, avatar=userEl.avatar, bg_img=userEl.bg_img,
                               edu=userEl.edu,
                               num_telephone=userEl.num_telephone, info=userEl.info, city=userEl.info,
                               is_active=userEl.is_active,
                               is_superuser=userEl.is_superuser, is_verified=userEl.is_verified))
    return resUse


@app.get("/friends/users/{id}/{limit}")
async def get_user_friends(id, limit, db: AsyncSession = Depends(get_async_session)):
    resultFriends = await db.execute(select(friend).where(friend.c.user_id == int(id)).limit(int(limit)))
    userFriends = resultFriends.all()
    friendList = []
    for fr in userFriends:
        friendList.append(Friend(id=fr.id, user_id=fr.user_id, friend_id=fr.friend_id))

    resultUser = []
    for frL in friendList:
        result = await db.execute(select(user).where(user.c.id == int(frL.friend_id)))
        temp = result.all()
        resultUser.append(UserRead(id=temp[0].id, email=temp[0].email, username=temp[0].username,
                                   surname=temp[0].surname, avatar=temp[0].avatar, bg_img=temp[0].bg_img,
                                   edu=temp[0].edu,
                                   num_telephone=temp[0].num_telephone, info=temp[0].info, city=temp[0].info,
                                   is_active=temp[0].is_active,
                                   is_superuser=temp[0].is_superuser, is_verified=temp[0].is_verified))
    return resultUser


@app.delete("/friends/curUser/{id_cur_user}/friend/{id_friend}")
async def delete_friends(id_cur_user, id_friend, db: AsyncSession = Depends(get_async_session)):
    query1 = delete(friend).where(friend.c.user_id == int(id_cur_user), friend.c.friend_id == int(id_friend))
    query2 = delete(friend).where(friend.c.user_id == int(id_friend), friend.c.friend_id == int(id_cur_user))
    await db.execute(query1)
    await db.commit()
    await db.execute(query2)
    await db.commit()
