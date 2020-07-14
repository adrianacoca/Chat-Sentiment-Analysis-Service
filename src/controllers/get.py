from src.app import *
from pymongo import MongoClient
from src.config import *
from flask import request
import re
from flask import Flask
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

client = MongoClient(DBURL)
db = client.get_database()


@app.route ("/")
def Welcome():
    return "Welcome to the Chat Sentiment Analysis Service API"


@app.route ("/chat/<conversation_id>/list")
#@errorHelper(["list"])
def GetConv(conversation_id): 
    conv = ObjectId(conversation_id)
    conversation = list(db.messages.find({"chat_id": conv}, {"_id":0,"user_id":1, "text":1}))
    return dumps(conversation)


#Intento de encontrar el nombre del user id
'''
@app.route ("/chat/<conversation_id>/list")
#@errorHelper(["list"])
def GetConv(conversation_id): 
    conv = ObjectId(conversation_id)
    conversation = list(db.messages.find({"chat_id": conv}, {"_id":0,"user_id":1, "text":1}))
    d = dumps(conversation)
    d=res.content.decode("utf-8")
    d=json.loads(d)
    users=[]
    messages=[]
    for i in range(len(d)):
        users.append(d[i]["user_id"]["$oid"])
        messages.append(d[i]["text"])
    return (users, messages)

def GetConv(users):
    for user in users: 
        usernames = list(db.user.find({"_id": ObjedtId(user)}, {"_id":0,"name":1}))
        return dumps(usernames)
'''