print("Hi we are revising python")
#functions in python from basic to advance 

#function 1
def greet():
    print("hi Ritik")

greet()    

#function 2
def greett(name):
    print(f"the candidate name is ={name}")

n="Ritik"
greett(n)
greett("Ritesh")


#function 3 with return type
def add(a,b):
    print("in this function we are trying to learn about functions")
    return a+b

a=45
b=67
add(a,b)
a=67
b=90
add(a,b)
# if we need data later we use return not print..

#multiple parameter in functions 
#function 4
def create_user(name , role):
    print("Function Running Successfully")
    return{
        "name": name ,
        "role": role
    }
  
    #print(f"User name is : {name}")
    #print(f"User role is : {role}")

print(create_user("Ravi" , "DEV"))
print(create_user("Ritik" , "Admin"))
print(create_user("Ritika" , "HR"))


#function 5 with default parameter
def create_userr(name, role="user"):
    return {
        "name": name,
        "role": role
    }

print(create_userr("Ritik"))
print(create_userr("Riya", "admin"))



# *args=multiple positional Arguments
#function 6
def num_data(*numbers):
    return numbers


data=num_data(10,56,78.76,98)
print(data)

def take_name(*names):
    return names


name=take_name( 'ravi' , 'ritik' , 'ritika' , 'rohit' , 'rohan')
print(name)

# **kwargs= multiple keyword arguments
#function 7
def take_data(**data):
    return data

data=take_data(Name='Ritik' ,  Age=21 )
data2=take_data( Name='rohit' , Age='21')
data3=take_data(rollno=185)
print(data)
print(data2)
print(data3)



#function 8 : filtering data using functions

users = [
    {"name": "Ritik", "age": 21},
    {"name": "Aman", "age": 17},
    {"name": "Nitin", "age": 21},
    {"name": "sweta jha" , "age": 20},
    {"name": "pintu" , "age": 5} , 
    {"name": "ritesh" , "age": 23}
]

def get_adults(users):
    return [ad for ad in users if ad["age"] >= 18]

#print(get_adults(users))

#function 9 composition 


def adult(age):
    return age >= 18

def filter_user(user):
    return [u for u in user if u['age'] >= 18]

print(filter_user(users))
print(adult(21))

#basic functions end here 

#advance function for backend development purposes
#function 10 : function as parameter
def square(x):
    return x * x
def cube(x):
    return x * x * x
def apply_function(func, value):
    return func(value)
print(apply_function(square, 5))  # Output: 25
print(apply_function(cube, 3))    # Output: 27

#function 11 : nested functions
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

# ========== BACKEND DEVELOPMENT PATTERNS ==========

# Pattern 1: Decorators (used everywhere in backends)

def admin(func):
    def wrap(user):
        if user.get('role')=='admin':
            return func(user)
        return {"Access" : "denied"}
    return wrap
    

@admin
def create_user(user):
    return {"message " : f"{user['name']} created" }

print(create_user({'name':'Ritik' , 'role':'admin'}))
print(create_user({'name':'ravi', 'role':'admin'}))
print(create_user({'name':'ritika', 'role':'student'}))

@admin
def delete_user(user):
    return {"message " : f"{user['name']} deleted" }

print(delete_user({'name':'Ritik' , 'role':'admin'}))
print(delete_user({'name':'ravi', 'role':'admin'}))
print(delete_user({'name':'ritika', 'role':'student'}))


# Pattern 2: Higher Order Functions (callbacks)
def process_data(users , callbacks):
    return [callbacks(u) for u in users]

def get_name(users):
    return users['name']

def get_age(users):
    return users['age']

users=[
    {"name": "Ritik" , "age": 21},
    {"name": "ritika" , "age":22},
    {"name":"riya" , "age":21},
    {"name":"sweta", "age": 20}
]

print(process_data(users , get_name))
print(process_data(users , get_age))



# Pattern 3: Lambda Functions (inline callbacks)
# Common in backend filters
adult_users = list(filter(lambda u: u['age'] >= 18, users))
# print(f"Adults: {adult_users}")

# Pattern 4: Default parameters (API functions)
def create_post(title, content, author, status="draft", tags=None):
    if tags is None:
        tags = []
    return {
        "title": title,
        "content": content,
        "author": author,
        "status": status,
        "tags": tags
    }

post1 = create_post("Learning Python", "Functions are cool", "Ritik")
post2 = create_post("APIs", "REST APIs", "Aman", status="published", tags=["api", "web"])
print(post1)
print(post2)

# Pattern 5: *args and **kwargs together (flexible APIs)
def build_response(*args, **kwargs):
    """Mimics backend API response"""
    return {
        "data": args,
        "meta": kwargs
    }
    
    
response = build_response(
    {"id": 1, "name": "User1"},
    {"id": 2, "name": "User2"},
    status=200,
    message="Success")

print(response)

# Pattern 6: Type hints (modern Python backends)
def authenticate(username: str, password: str) -> dict:
    """Returns token if valid credentials"""
    if username == "admin" and password == "pass123":
        return {"token": "abc123xyz", "success": True}
    return {"token": None, "success": False}
print(authenticate("admin", "pass123"))

# Pattern 7: Data validation in functions
def validate_users(name :str , age:int , email:str) ->dict:
    errors=[]
    if not name or len(name)<2:
        errors.append("Name is invalid")
    if age <18 or age >100:
        errors.append("Age must be under 18 and 100")
    if "@" not in email:
        errors.append("invalid email")   

    if errors:
        return{"Valid": False , "Errors":errors}
    return{
        "Valid": True , "Name":name , "Age":age , "Email":email
    }    


user1=validate_users("Ritik" , 21 , "ritiksharma@gmail.com")
user2=validate_users("ravi" , 21 , "ravi@gmail.com")
user3=validate_users("riya" , 23 , "riya@gmail")
user4=validate_users("Ritika" ,21 , "ritikagmail.com")

print(user1)
print(user2)
print(user3)
print(user4)

# Pattern 8: Closures (important for caching/state)
def create_multiplier(factor):
    """Returns a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_2 = create_multiplier(2)
multiply_by_5 = create_multiplier(5)

print(multiply_by_2(10))  # 20
print(multiply_by_5(10))  # 50

# Pattern 9: Function composition (chaining operations)
def add_tax(price):
    return price * 1.18

def apply_discount(price, discount=0.1):
    return price * (1 - discount)

def final_price(original_price, discount=0.1):
    """Compose functions: first discount, then tax"""
    discounted = apply_discount(original_price, discount)
    return add_tax(discounted)

# price = final_price(1000, 0.2)
# print(f"Final price: {price}")

# Pattern 10: Map, Filter, Reduce (functional programming)
from functools import reduce

# Map: Transform data
doubled_ages = list(map(lambda u: u['age'] * 2, users))
# print(f"Doubled ages: {doubled_ages}")

# Filter: Select data
seniors = list(filter(lambda u: u['age'] > 20, users))
# print(f"Users older than 20: {seniors}")

# Reduce: Aggregate data
total_age = reduce(lambda acc, u: acc + u['age'], users, 0)
# print(f"Total age: {total_age}")

# ========== BACKEND API EXAMPLE ==========

# Real-world example: User service functions
class UserService:
    def __init__(self, users_list):
        self.users = users_list
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        for i, user in enumerate(self.users):
            if i == user_id:
                return user
        return None
    
    def get_adults(self):
        """Get all adults"""
        return list(filter(lambda u: u['age'] >= 18, self.users))
    
    def get_users_by_age(self, min_age):
        """Get users older than min_age"""
        return list(filter(lambda u: u['age'] >= min_age, self.users))
    
    def create_user(self, name, age):
        """Create and return new user"""
        return {"name": name, "age": age}
    
    def update_user(self, user_id, **kwargs):
        """Update user with any field"""
        if user_id < len(self.users):
            for key, value in kwargs.items():
                self.users[user_id][key] = value
            return self.users[user_id]
        return None

service = UserService(users)
print("Adults:", service.get_adults())
print("Users 20+:", service.get_users_by_age(20))
new_user = service.create_user("Neha", 19)
print("New user:", new_user)












