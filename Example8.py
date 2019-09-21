class User():
    """Objekt per nje user te caktuar"""

    def __init__(self,first_name,last_name,username,age):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.age=age
    
    def describe_user(self):
        print("Emri: "+self.first_name)
        print("Mbiemri: "+self.last_name)
        print("Username: "+self.username)
        print("Mosha: "+str(self.age))
    
    def greet_user(self):
        print("Pershendetje i/e nderuar "+self.first_name+"!")
    
useri1=User("Blendar","Kabashi","blendkabashi",20)
useri2=User("Gent","Kabashi","gentkabashi",18)
useri3=User("Hamdi","Kabashi","hamdik",28)
useri4=User("Fitore","Kabashi","fitorem",22)

useri1.describe_user()
useri1.greet_user()
print("======================================")

useri2.describe_user()
useri2.greet_user()
print("======================================")

useri3.describe_user()
useri3.greet_user()
print("======================================")

useri4.describe_user()
useri4.greet_user()
print("======================================")