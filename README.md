# Chat-Sentiment-Analysis-Service


url = f"http://localhost:3000/chat/{chat}/list
(choose chat from chats)
Chats: 
 - Business 
 - Politics
 - Forces
 - Persuade
 - Principles

res = requests.get(url)
print(res)
res.json
print(res.json)