mosha=int(input("Shkruaj moshen tuaj: "))
cmimi=0
if(mosha<12):
    cmimi=0
elif(mosha>=12 and mosha<=20):
    cmimi=5
else:
    cmimi=2
print("Bileta juaj kushton "+str(cmimi)+"$")
