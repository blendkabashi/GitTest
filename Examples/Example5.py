hamburgerIngredients=[]

stringu=input("Shkruani produktet qe doni ne burger (vetem nje): ")

while(stringu!="PERFUNDO"):
    stringu=input("Perberesi tjeter: ")
    if (len(stringu.split(" "))==1):
        hamburgerIngredients.append(stringu.strip())
    else:
        stringu=input("Shkruani vetem nje perberes!! Vazhdoni: ")


llojiBurgerit=input("Tani shkruaj llojin e burgerit: ")
while(len(llojiBurgerit.split(" "))!=1):
    llojiBurgerit=input("Ju lutem shkruani vetem nje fjale! Provo perseri: ")
hamburgerIngredients.remove('PERFUNDO')
cmimi=len(hamburgerIngredients)

print("======================")
print("Hamburgeri u porosit!\nLloji: "+llojiBurgerit+"\nPerberesit: "+str(hamburgerIngredients)+"\nCmimi: "+str(cmimi)+"$")