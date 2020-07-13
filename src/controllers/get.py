from src.app import *
from pymongo import MongoClient
from src.config import DBURL
from flask import request
import re


client = MongoClient(DBURL)
db = client.get_database()


@app.route ("/")
def Welcome():
    return "Welcome to the Chat Sentiment Analysis Service API"

"""
@app.route ("/chat/<conversation_id>/list", method=["GET"])
#@errorHelper(["list"])
def GetConv(conversation_id): 
    print(f"Requesting info for conversation {conversation_id}")
    conversation = companies.find_one({"conversation_id": conversation_id}, text)
    return text

@app.route ("/chat/<conversation_id>/sentiment", method=["GET"])


@app.route ("/user/<user_id>/recommend", method=["GET"])
"""