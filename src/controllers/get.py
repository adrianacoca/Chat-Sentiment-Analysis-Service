from src.app import *
from pymongo import MongoClient
from src.config import *
from flask import request
import re
from flask import Flask
from bson.objectid import ObjectId

client = MongoClient(DBURL)
db = client.get_database()


@app.route ("/")
def Welcome():
    return "Welcome to the Chat Sentiment Analysis Service API"


@app.route ("/chat/<conversation_id>/list")
#@errorHelper(["list"])
def GetConv(conversation_id): 
    conv = ObjectId(conversation_id)
    conversation = [t for t in db.messages.find({"chat_id": conversation_id}, {"_id":0,"text":1})]
    print(conversation)
    return conversation