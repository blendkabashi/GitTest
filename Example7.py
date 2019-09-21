def create_car(manufacturer,model,**other):
    car={}
    car["Prodhuesi"]=manufacturer
    car["Modeli"]=model
    for key,value in other.items():
        car[key]=value
    return car

car=create_car('subaru','outback',color='blue',tow_package=True)
print(car)