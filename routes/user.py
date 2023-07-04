from bson import ObjectId
from fastapi import APIRouter

from config.db import conn
from models.user import User
from schemas.user import serializeDict, serializeList

user = APIRouter()

@user.get('/')
async def find_all_users():
    print(conn.shop.users.find())
    print(serializeList(conn.shop.users.find()))
    return serializeList(conn.shop.users.find())

@user.get('/{id}')
async def get_by_id(id):
    return serializeDict(conn.shop.users.find_one({'_id':ObjectId(id)}))

@user.post('/')
async def create_user(user:User):
    conn.shop.users.insert_one(dict(user))
    return serializeList(conn.shop.users.find().sort('_id',-1).limit(1))

@user.put('/{id}')
async def update_user(id, user:User):
    conn.shop.users.find_one_and_update(
        {'_id':ObjectId(id)},
        {'$set':dict(user)})
    return serializeDict(conn.shop.users.find_one({'_id':ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return serializeDict(conn.shop.users.find_one_and_delete({'_id':ObjectId(id)}))