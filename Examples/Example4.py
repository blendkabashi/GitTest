def kontrolloUsername(username):
    while (username.lower() in current_users):
        print("Username ekziston, provo nje tjeter!")
        username=input("Shkruaj nje tjeter username: ")
    new_users.append(username)
    print("Jeni regjistruar me sukses!")

current_users=['blendkabashi','gentkabashi',"hamdikabashi","fitorekabashi"]
new_users=[]
stringu=input("Shkruaj username: ")
kontrolloUsername(stringu)