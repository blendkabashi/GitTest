fruits=["apple","banana","kiwi","pear"]
favorite_fruits=[]
for element in range(0,4):
    favorite_fruits.append(input("Shkruaj frutat e preferuara: "))
for favoriteF in favorite_fruits:
    if (favoriteF in fruits):
        print(favoriteF+" gjindet")
    else:
        print(favoriteF+" nuk gjindet")
