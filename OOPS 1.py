print("Practicing oops inPython")
"Deep Dive Basic to Advance for Backend Development"

class User:
    def __init__(self,name,role,age=18):
        self.name=name
        self.role=role
        self.age=age
    def info(self):
        return f"Name:{self.name} , Role:{self.role}"
    def adult(self):
        return self.age>18
    
user1=User("Ravi" , "user" , 21)
print(user1.info())
print(user1.adult())  

class service:
    def __init__(self, username , password):
        self.username=username
        self.password=password

    def authenticate(self , input_password):
        if self.password==input_password:
            return f"Access granted"
        return f"Access Denied"
    
cse=service("ranjit" , "ranjit10")
print(cse.authenticate("ranjit10"))

class Student:
    def __init__(self , name , roll):
        self.name=name
        self.roll=roll
    def display_info(self):
        return f"Name :{self.name} , Roll No :{self.roll}" 

s1=Student("Sahil" , 701010)
print(s1.display_info()) 

class Bankaccount:
    def __init__(self,account_holder , balance):
        self.account_holder=account_holder
        self.balance=balance

    def login(self):
        return f"{self.account_holder} logged in successfully"    

    def deposit(self , amount):
         self.balance =self.balance+ amount
         return  self.balance
    
    def withdraw(self , amount):
        self.balance=self.balance-amount
        return self.balance

customer1=Bankaccount("Ritik" , 2100)
print(customer1.login())
print(customer1.deposit(80))
print(customer1.withdraw(45))

#ACCESS MODIFIERS IN OOPS
# DEFAULT PUBLIC

class emp:
    def __init__(self,name):
        self.name=name
emp1=emp("kit")        
print(emp1.name)

#PROTECTED
class emp2:
    def __init__(self,name):
        self._name=name
emp3=emp2("bit")        
print(emp3._name) #accessible but not recommended

#PRIVATE
class emp4:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

emp4=emp4("ritik")
#print(emp4.__name)# error
print(emp4.get_name())

# Code explaining encapsulation

class Bank:
    def __init__(self,username , balance):
        self.username=username
        self.__balance=balance
    def check_balance(self):
        return self.__balance
    def deposit(self , amount):
        if amount<0:
            return "Invalid amount"
        self.__balance+=amount
        return f"{amount}deposited succesfully "
    def withdraw(self , amount):
        if amount> self.__balance:
            return "Insufficient balance"
        self.__balance-=amount
        return f"{amount} withdrawn successfully"
    
acc = Bank("Ritik", 1000)
print(acc.check_balance())    # 1000
print(acc.deposit(500))     # 1500
print(acc.withdraw(2000)) # Insufficient balance
print(acc.withdraw(245))
print (acc.check_balance()) 

# Property Decorators


class User:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if "@" not in new_email:
            return "Invalid email"
        self.__email = new_email



u=User("ritik@gmail.com")
print(u.email)  # Accessing email using the getter
u.email = "ritiksharma.com"  # Trying to set an invalid email
print(u.email)  # Accessing email again to see if it changed



#Inheritance and types of inheritance for backend development
#in next one 
        







        