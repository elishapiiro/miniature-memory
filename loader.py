import os
import json
import pymongo
from dataclasses import dataclass
from Typing import Dict

@dataclass
class User:
    _id: str
    username: str
    email: str
    password: str
    ssn: str
    home_address: Dict[str, str]
    age: int

client = pymongo.MongoClient(os.environ['MONGODB_CONNECTION_STRING'])
db = client.mydatabase
users_collection = db.users

raw_users = []
for user in users_collection.find():
    raw_users.append(user)

# Load the encrypted users into User objects
users = []
for user in raw_users:
    user_dict = {}
    for key, value in encrypted_user.items():
        if key == '_id':
            # Convert the ObjectId to a string
            value = str(value)
        user_dict[key] = value
    user = User(**user_dict)
    users.append(user)

# Print the user objects
for user in users:
    print(user)
