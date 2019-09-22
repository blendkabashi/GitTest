import json

def greet_user():

    filepath = 'C:\\Users\\Fitore Muqaj\\Desktop\\firstfile.json'

    try:
        with open(filepath) as fileObject:
            username = json.load(fileObject)
    except FileNotFoundError:
        with open(filepath, 'w') as fileObject:
            username = input("Shkruaj username-in tend: ")
            json.dump(username, fileObject)
    else:
        print("Mireseerdhe prape "+username)

greet_user()