"""
from pymongo import MongoClient
from src.config import DBURL

client = MongoClient(DBURL)
db = client.get_database()


def validateUsername(username):
    return (False, True)[db.user.find({"user_name":{"$eq":username}})]

def validateChat(chatname):
    return (False, True)[db.chats.find({"conversation name":{"$eq":chatname}})]

def validateUserInChat(userid, chatid):
    return (False, True)[db.chats.find({"_id":chatid, "participants":{"$eq":userid}})]

"""