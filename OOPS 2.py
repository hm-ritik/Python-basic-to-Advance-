print("Inheritance Backend Development")
"Deep Dive Basic to Advance for Backend Development"

#inheritance means inheriting data memebers and methods of 
# one class in another to improve reuseability

class Service:                              #Parent Class
    def __init__(self, username):
        self.username=username

    def login(self):
        return f"{self.username} has logged in"

class amdmin(Service):                       #Child Class
    pass

s1=amdmin("Ritik")
print(s1.login())


#Single Inheritance basic to pro 
class Parent:
    def func1(self):
        return "This is function 1 from Parent Class"
    def func2(self):
        return "This is function 2 from Parent Class"
class Child(Parent):
    def func3(self):
        return "This is function 3 from Child Class"
    def func4(self):
        return "This is function 4 from Child Class"
c1=Child()
print(c1.func1())
print(c1.func3())
print(c1.func4())
print(c1.func2())

#single level inheritance with constructor and attributes and super keyword
class Parent1:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def func1(self):
        return f"This is {self.name} and age is {self.age}"
class Child1(Parent1):
    def __init__(self, name, age,grade):
        super().__init__(name , age)
        self.grade=grade
    def info(self):
        print(self.name)
        print(self.age)
        print(self.grade)

s1=Child1('Ritik' , 26 , 'A')     
s1.info()     

#multilevel inheritance

class Mining:
    company="Chotis Coal"
    def __init__(self,m_id ):
        self.m_id=m_id
       
    def basic_info(self):
        return{
            "Mining Id":self.m_id,
            "Company Name":self.company
        }    
    
class dhanbad(Mining):
    def __init__(self, m_id, name , no_worker):
        super().__init__(m_id)  
        self.name=name
        self.no_worker=no_worker 

    def info(self):
        return {
            "Name": self.name ,
            "No of Worker " : self.no_worker
        } 

class girdi(dhanbad):
    def __init__(self, m_id, name,sub_name, salary , no_worker):
        super().__init__(m_id, name, no_worker) 
        self.sub_name=sub_name
        self.salary=salary 

    def subcenter(self):
        return{
            "Sub Name": self.sub_name ,
            "salary": self.salary


        }   


Center_1=girdi(1234 ,'Rohit' , "girdi" , 34500 , 45)

print(Center_1.basic_info())
print(Center_1.info())
print(Center_1.subcenter())
print("And the name is Gangs of wassepur")


#multiple inheritance
class Supervisor:
    def __init__(self,Name , Age , Location):
        self.Name=Name
        self.Age=Age
        self.Location=Location
    def info(self):
        return f"Hi , i am {self.Name} "    

class Manager:
    def __init__(self,Name , Age , Salary):
        self.Name=Name
        self.Age=Age
        self.Salary=Salary
    def sal(self):
        return f"My Salary Is {self.Salary}"

class Worker(Supervisor , Manager):
    def __init__(self, Name, Age, Location,Salary):
        Supervisor.__init__(self, Name, Age, Location)
        Manager.__init__(self, Name, Age, Salary)
        pass


W1=Worker("Rohit" , 22 , "Girdi" , 78600)
print(W1.info())
print(W1.sal())

#hierarchical inheritance and hybrid inheritance cab be made using above concepts

#A Vast Question on inheritance for backend development 

class Loginrequiredmixin:
    def __init__(self,User , **kwargs):
        super().__init__(**kwargs)
        self.User=User
    def dispatch(self):
        if not self.User:
            return "Login Required"
        return super().dispatch()

class permissionmixin:
    def __init__(self,permission , **kwargs):
        super().__init__(**kwargs)
        self.permission = permission

    def dispatch(self):
        if self.permission !='Admin':
            return "Permission Require"
        return super().dispatch()


class BaseView:
    def __init__(self, **kwargs):
        pass

    def dispatch(self):
        return "✅ Welcome to Dashboard"


class DashboardView(Loginrequiredmixin, permissionmixin, BaseView):
    def __init__(self, User=None, permission=None):
        super().__init__(User=User, permission=permission)    


view=DashboardView(User="Rohit" , permission='Admin')
print(view.dispatch())       

       
        
