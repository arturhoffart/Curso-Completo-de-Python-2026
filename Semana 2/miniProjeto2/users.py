#create a dictionary and list to store user information
user = {}
users = []

#function to add user to list of dictionaries
def add_user(name, age, mail):
    user["name"] = name
    user["age"] = age
    user["mail"] = mail
    users.append(user.copy())

#function to list all users
def list_users():
    for user in users:
        print(user["name"], user["age"], user["mail"])

#function to list only 18+ users
def list_user_18():
    for user in users:
        if user["age"] >= 18:
            print(user["name"], "is 18 or older")

#function to search user by name
def search_user(name):
    for user in users:
        if user["name"] == name:
            print(user["name"], user["age"], user["mail"])
            return
        else:
            print("user not found")
