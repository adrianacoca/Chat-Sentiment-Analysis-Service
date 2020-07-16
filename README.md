# Chat-Sentiment-Analysis-Service
  
This project creates an api of converations between famous people of the 20th century incluing:   
 - Al Capone  
 - Albert Einstein  
 - Abraham Lincoln  
 - Adolf Hitler  
 - Donald Trump  

**src controllers create** -- to introduce information in the API  
1. Create a collection for users. *createUser(username)*   
2. Create a collection for chats and introduce participants for each chat through usesr ObjectId. *createChat()*  
3. Add new users to a chat. *user(conversation_id)*  
4. Create a collection for messages introduce chat_id and user_id for which the message ocurred *createConv(conversation_id)*  

**src controllers get** -- to get information from the API   
1. Function to get messages from a char*GetConv(conversation_id)*   

**To get information from the api run: **    
url = "http://localhost:3000/chat/topic/list"     

choose (topic) from:      
 - business   
 - politics   
 - forces   
 - persuade   
 - principles    
 