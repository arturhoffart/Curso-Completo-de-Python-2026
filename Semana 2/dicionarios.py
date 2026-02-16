
#create a dictionary to store person information
person = {
    "name" : "Artur",
    "age" : 44,
    "city" : "Sorocaba"
}

#print from dictionary
print(person)
print(person["name"])

#add new field to dictionary
person["job"] = "Developer"

#remove field from dictionary
del person["age"]

#run loop to print dictionary values
for key, value in person.items():
    print(key, value)

#create a list of dicitionaries to store information
users = []
users.append({
    "name": "ana",
    "age" : 25

})

users.append({
    "name": "Carlos",
    "age" : 30
    
})

users.append({
    "name": "erico",
    "age" : 25
    
})



#print all users from list of dictionaries
for user in users:
    print(user["name"])


#condition with structures
for user in users:
    if user["age"] >=30:
        print(user["name"], "is 30 or older")
    else:
        print(user["name"], "is younger than 30")
