import json

#creating a dictionary
person = {
    "name" : "Artur",
    "age" : 44,

}

#dumps transforms string in json format
json_string = json.dumps(person)

print(person)


#loads transform json string in dictionary
dados = json.loads(json_string)

print(dados["name"])

#creating a list of dictionaries
users = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 32}
]

#save list of dictionaries in json file
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

#read json file and transform in list
with open("users.json", "r") as file:
    users_from_file = json.load(file)

    

