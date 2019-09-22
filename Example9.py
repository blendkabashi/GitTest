from random import randint

filepath = 'C:\\Users\\Fitore Muqaj\\Desktop\\username.txt'
string=''
with open(filepath,'w') as file_object:
    for i in range (0,10):
        for j in range (0,5):
            file_object.write(str(randint(0,9)))
        file_object.write('\n')