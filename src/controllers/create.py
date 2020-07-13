from src.app import *
from pymongo import MongoClient
from src.config import *
from flask import request
import re
from flask import Flask


client = MongoClient(DBURL)
db = client.get_database()

#User Endpoints
@app.route ("/user/create/<username>")
def createUser(username):
    user = {"name":f"{username}"}
    userinfo = db.user.insert_one(user)
    return f"New user created! name: {username} , user id: {userinfo.inserted_id}"

#Chat Endpoints
@app.route ("/chat/create/")
def createChat():
    participants = request.args.getlist("participants")
    conv_name = request.args.get("conv_name")
    conversation = db.chats.insert_one({"conversation name":conv_name, "participants":participants})
    return  f"New chat created! Chat name: {conv_name}, Chat id: {conversation.inserted_id}"

'''
@app.route ("/chat/<conversation_id>/adduser")
def user(conversation_id):
    new_user = request.args.get("user_id")
    return f"User {user_id} added to chat {conversation_id}!"


@app.route ("/chat/<conversation_id>/addmessage", methods=["POST"])
def createConv(conversation_id):
    conversation = 
    d={"text":text}
    message_id=db.conversation_id.insert_one(d)
    return message_id
'''
