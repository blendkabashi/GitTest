import json

def get_stored_username():

    filepath = 'C:\\Users\\Fitore Muqaj\\Desktop\\firstfile.json'

    try:
        with open(filepath) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filepath = 'C:\\Users\\Fitore Muqaj\\Desktop\\firstfile.json'
    with open(filepath, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():

    username = get_stored_username()
    if username:
        print("Mireseerdhe prape "+username)
    else:
        username = get_new_username()
        filepath = 'C:\\Users\\Fitore Muqaj\\Desktop\\firstfile.json'
        with open(filepath,'w') as f_obj:
            json.dump(username,f_obj)



greet_user()