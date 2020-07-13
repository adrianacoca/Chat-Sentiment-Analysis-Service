from src.app import *
from pymongo import MongoClient
from src.config import *
from flask import request
import re
from flask import Flask
from bson.objectid import ObjectId

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
    participants = [ObjectId(p) for p in request.args.getlist("participants")]
    conv_name = request.args.get("conv_name")
    p_dict={"conversation name":conv_name, "participants":participants}
    conversation = db.chats.insert_one(p_dict)
    return  f"New chat created! Chat name: {conv_name}, Chat id: {conversation.inserted_id}"

@app.route ("/chat/<conversation_id>/adduser")
def user(conversation_id):
    conversation_id = ObjectId(conversation_id)
    new_user = ObjectId(request.args.get("user_id"))
    db.chats.update({ "_id":conversation_id},{ "$push":{ "participants": new_user}})
    return f"User {new_user} added to chat {conversation_id}!"

#Message Endpoints

@app.route ("/chat/<conversation_id>/addmessage")
def createConv(conversation_id):
    conversation_id = ObjectId(conversation_id)
    participant = ObjectId(request.args.get("user_id"))
    text = request.args.get("text")
    conversation = {"chat_id":conversation_id, "user_id":participant, "text":text}
    db.messages.insert_one(conversation)
    return f"{text} said by participant: {participant} added to conversation {conversation_id}"
