survey={}
filloi=True

while filloi:
    emri=input('Shkruaj emrin tend: ')

    survey[emri]=input("Shkruaj hobin tuaj: ")
    survey['profesioni']=input("Shkruaj profesionin tuaj: ")
    survey['mosha']=input("Shkruaj moshen: ")

    again=input("a doni apet P/J: ")
    if(again == 'J'):
        filloi=False

for key,value in survey.items():
    print(key,value)