import json
from flask import Flask,request

app=Flask(__name__)

class User:
    def __init__(self,id,firstName,email):
        self.firstName=firstName
        self.email=email
        self.id=id

userList=[]
user1=User("5abf6783","ABC","abc@abc.ca")
user2=User("5abf674563","XYZ","xyz@xyz.ca")

userList.append(user1)
userList.append(user2)

@app.route("/users",methods=['GET'])
def getusers():
    sampledict= { 
    'message' : "Users retrieved", 
    "success" : "true", 
    "users" : [ob.__dict__ for ob in userList]
    }

    return json.dumps(sampledict)

@app.route("/update/<userId>",methods=['PUT'])
def updateusers(userId):
    data = request.json
    for i in userList:
        if i.id==userId:
            i.firstName=data.get('firstName')
            i.email=data.get('email')
            successdict={
                'message' : "Users updated", 
                "success" : "true"
            }
            statusCode=200
        else:
            successdict={
            'message' : "Users not found", 
            "success" : "false"
             }
            statusCode=404
    return json.dumps(successdict),statusCode

@app.route("/add",methods=['POST'])
def addusers():
    data = request.json
    id=userList[-1].id+"1"
    user3=User(id,data.get('firstName'),data.get('email'))
    userList.append(user3)
    successdict={
        'message' : "Users added", 
        "success" : "true"
    }
    statusCode=200
    return json.dumps(successdict),statusCode

@app.route("/user/<userId>",methods=['GET'])
def getuserbyId(userId):
    for i in userList:
        if i.id==userId:
            user={
                "email":i.email,
               "firstName":i.firstName,
               "id":i.id 
            }
            sampledict= {  
            "success" : "true", 
            "users" : user
            }
            statusCode=200
        else:
            sampledict={
            'message' : "Users not found", 
            "success" : "false"
             }
            statusCode=404

    return json.dumps(sampledict),statusCode
