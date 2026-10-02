# # variables decalartion means to assign a value to a variable
# example of variable

first_name = "bede" 
age = 25
country = 'nigeria'
message = '''welcome to  python class with tech 365 
let get started.'''

a = b = c = 9
x, y, z, = 3, 6, 7,
price = 19.90
score = 40.00

# # output using print in python means to display a value on the screen. example of print

print(first_name)
print('2 + 2')
print(2 + 2)
print(age)
print(b)
print(y)
print(z, z, y, y, x, x, y, z)
print(a + b - c)
print(y + z * x / x )
print(price * score)
print(a + score)
print("i am", age ,"year old")
print("i am " + str(age) + " year old")


# # variable rules and data types
# 1. cant start with a number eg 1name (invalid)
# 2. cannot contain spaces eg first name (invalid) 
# 3. cannot contain speial characters except underscore eg first_name (valid) first-name (invalid)
# 4.  should be descriptive eg first_name (valid) a (invalid)
# 5. case sensitive eg first_name (valid) First_name (invalid)
# 6. dont use reserved words  eg print (invalid) first_name (valid)  
# 7. variable is a container that stores data   eg first_name = "bede" (valid)  first_name = 25 (valid) first_name = 19.90 (valid) first_name = True (valid) first_name = [1,2,3] (valid) first_name = {"name":"bede"} (valid)


# # data type example of data types in python are string, integer, float, boolean, list, tuple, set and dictionary.
# # 1. string data type
# example of string data type is a sequence of characters enclosed in single or double quotes. eg first_name = "bede" (valid) first_name = 'bede' (valid) first_name = '''bede''' (valid) first_name = """bede""" (valid)
# example of string methods are upper(), lower(), capitalize(), title(), count(), endswith(), startswith(), index(), strip(), encode() etc.
# example of string indexing is to access a specific character 
# in a string using its index. eg first_name[0] (valid) first_name[-1] (valid) first_name[0:3] (valid) first_name[-3:] (valid) first_name[::2] (valid) first_name[::-1] (valid)
# example of string slicing is to access a specific range of characters in
#  a string using its index. eg first_name[0:3] (valid) first_name[-3:]
#  (valid) first_name[::2] (valid) first_name[::-1] (valid)
# example of string concatenation is to combine two or more strings 
# using the + operator. eg first_name + " " + last_name (valid) first_name + " " + str(age) (valid) first_name + " " + str(price) (valid) first_name + " " + str(score) (valid)  
# 
# indexing
address = '4 soja adeomeja ikeja' 
print(address[2]) # prints 's'
print(address[-2]) # prints 'a'
print(address[0:4]) # prints '4 soj'
# slicing
print(address[2:6]) # prints 'soja'
print(address[-2:-1]) # prints 'a'
print(address[-8:-10]) # prints 'ikeja'

numbers = "123456789"
print(numbers[1::2]) # prints '2468'
print(numbers[1::3]) # prints '369'  
print(numbers[ -2:-9:-1]) # prints '8765432'
print(numbers[ 7:0:-1]) # prints '8765432'

data = "A:1, B:2, C:3"
print(data[2: :5]) # prints '123'
print(data[-1: : -5]) # prints '321'
print(data[0: :5]) # prints 'A B C'
print(data[-3: : -5]) # prints 'C B A'

# # string methods
print(first_name.upper()) # prints 'BEDE'
print(first_name.lower()) # prints 'bede'
print(first_name.capitalize()) # prints 'Bede'
print(first_name.title()) # prints 'Bede'
print(first_name.count("e")) # prints '2'
print(first_name.lower().count("e")) # prints '2'   
print(first_name.endswith("e")) # prints 'True'
print(first_name.startswith('b')) # prints 'True'
print(len(first_name)) # prints '4'
print(first_name.index('e')) # prints '1'
print(first_name.strip()) # prints 'bede'
print(first_name.encode()) # prints 'b'
print(address.split()) # prints ['4', 'soja', 'adeomeja', 'ikeja']
print(address.replace("soja", "soji")) # prints '4 soji adeomeja ikeja'
print(address.find("soja")) # prints '2'

# list methods
names = ["bede", "neche", "ifeanyi", "john"] # list is a collection of items that are ordered and changeable.
names.append("mary") # adds an item to the end of the list
print(names) # prints ['bede', 'neche', 'ifeanyi', 'john', 'mary']
names.insert(1, "elizabeth") # inserts an item at a specific index
print(names)
names.remove("neche") # removes an item by value
print(names)
names.pop() # removes an item by index (default is last)
names.clear() # removes all items from the list
names.extend(["bede", "neche", "ifeanyi", "john"]) # adds multiple items to the end of the list
names.sort() # sorts the list in ascending order
names.reverse() # reverses the order of the list
names_copy = names.copy() # creates a copy of the list
names_count = names.count("bede") # counts the number of times "bede" appears in the list
names_index = names.index("ifeanyi") # finds the index of "ifeanyi" in the list
names_length = len(names)# finds the length of the list
names.extend(first_name)# adds the characters of the string "first_name" to the end of the list
print(names)
backup = names.copy()# creates a copy of the list
print(backup)

# nestned_list
group = [[1,2,3], [4,5,6], [7,8,9]] # nested list is a list that contains other lists as its elements.

#bring out 5 from the nested list above
print(group[1][1]) # prints '5'

#bring out 9 from the nested list above
print(group[-1][-1]) # prints '9'

# if statement
age = 18    
if age >= 18:
    print("you can vote")
else:
    print("Not eligible")

score = int(input("enter your score:"))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 75 and score < 90:
    print("Grade: B")
elif score >= 60 and score < 75:
    print("Grade: C")
elif score >= 50 and score < 60:
    print("Grade: D")
elif score >= 40 and score < 50:
    print("Grade: E")
elif score >= 0 and score < 40:
    print("Grade: F")
else:
    print("Invalid score")

student_score = [1,2,3,[4,5,[6,7]]]
# in the student_score above, change 7 to 8
student_score [3][2][1] = 8
print(student_score) # prints [1, 2, 3, [4, 5, [6, 8]]]

record = "this is the time to attend python training"
# bring out the words that start from 't'
i = record.split()
for word in i:
    if word.startswith('t'):
        print(word) # prints 'this', 'the', 'time', 'to', 'training'


words = 'Python is not hard. Do you agree'
# Print every word in this sentence above that has an even number of letters

for word in words.split():
    if len(word) % 2 == 0:
        print(word) # prints 'is', 'not', 'Do', 'you'

students = [
    {"name": "wale", "grade": 10},
    {"name": "mary", "grade": 15},
    {"name": "obi", "grade": 19},
    {"name": "chi", "grade": 9}
]
# bring out the names of students that have a grade greater than 10
for i in students:
    if i["grade"] > 10:
        print(i["name"]) # prints 'mary', 'obi'

# function
def greet(name):
    print("Hello, " + name)
greet("Bede") # prints 'Hello, Bede'

def square(x):
    return x * x
value = square(5)
print(value) # prints '25'

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area
print(area_of_circle(3.5)) # prints '78.5'
# function with default parameter
def greet(name, greeting="Hello"):
    print(greeting + ", " + name)
greet("Bede") # prints 'Hello, Bede'
greet("Bede", "Hi") # prints 'Hi, Bede'

import os

import calculator 

print(calculator.add_it(5, 3)) # prints '8'
print(calculator.sub_it(5, 3)) # prints '2'
print(calculator.mul_it(5, 3)) # prints '15'
print(calculator.div_it(5, 3)) # prints '1.6666666666666667'
print(calculator.mod_it(5, 3)) # prints '2'

import os
os.mkdir("tech365")
os.chdir("tech365") 
os.rmdir("tech365")


# #dicitionary data type

# #  indexing dicitionary
student = {"name":"Bede", "age":17, "gender":"male"}
print(student["gender"])
#dicitionary methods
print(student.get("gender"))
print(student.keys())
print(student.values())
print(student.items())
student.pop("gender")
print(student)
student.update({"email":"bede@gmail.com"})
print(student)
student.update({"name":"neche"})
print(student)
student.popitem()
print(student)
student.update({"email":"bede@gmail.com", "state": "lagos"})
print(student)
staff = [
    {"name":"bede", "gender":"male"},
    {"name":"neche", "gender":"female"},
    {"name":"ifeanyi", "gender":"male"}
    ]
print(staff[1]["gender"])
address = {"name": "bede", "age":17, "location":{"state":"lagos","zip":[2345,10001]}
}
print(address["location"]["zip"][1])
record ={'k1':[{'nest_key':['this is deep',['tech365']]}]}
print(record['k1'][0]['nest_key'][1][0])
result = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  }
]
print(result[1]["title"])

# # sets data type
data = {1,1,1,1,2,2,2,3,3,3}
print(data)

x = {1,2,3}
y = {3,4,5}
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(x.symmetric_difference(y))
x.add(8)
print(x)
x.remove(2)
print(x)
x.update([7,9])
print(x)
#tuple- immutable data
months = ("jan", "feb", "mar")
print(months[2])
#number datatype
age = 17
salary = 500.000

# # arithmetic operators
print(5 + 3)
print(5 - 3)
print(5 / 3)
print(5 % 3)
print(5 // 3)
print(5 * 3)
print(5 ** 3)

# # comparison operator >,<,<=,>=,==
print(5 > 3)
print(5 < 3)
print(5 >= 3)
print(5 <= 3)
print(5 == 3)
print(5 != 3)

# # logical operator and, or, not
print(5 > 3) and (2 > 3)
print(5 > 3) or  (5 > 3)
print(not(3 > 7))
# assignment operator +=, -=, *=, /=
x = 5
y = 2
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)

# # control flow
# age = int(input("enter your age:"))
# if age >= 18:
#     print("you can vote")
# else:
#     print("Not eligible")
color = "red"
if color == "red":
    print("red")
elif color == "green":
    print("green")
elif color == "blue":
    print("blue")
else:
    print("invalid color")

# #loops
x = 1
while x <= 5:
    print(x)
    x += 1

#     #for loop
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for i in numbers:
        print(i)
for i in range(1,11):
    print(i)
print(list(range(1,11,2)))
x = 5
if x >= 5:
    if x <= 5:
        print("A")
    else:
        print("B")

elif x == 5:
    print("B")
else:
    print("D")
for i in range(1,5):
    if i % 2 == 0:
        continue
    print(i, end = " ")

data = [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
  }
]
print(data[0]["address"]["geo"]["lat"])


# # Assignment
# # 1. record = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['python']]}]}]}

# # print out python from the record above

# # 2. data = [
# #   {
# #     "id": 1,
# #     "name": "Leanne Graham",
# #     "username": "Bret",
# #     "email": "Sincere@april.biz",
# #     "address": {
# #       "street": "Kulas Light",
# #       "suite": "Apt. 556",
# #       "city": "Gwenborough",
# #       "zipcode": "92998-3874",
# #       "geo": {
# #         "lat": "-37.3159",
# #         "lng": "81.1496"
# #       }
# #     }
# #   }
# # ]

# # print put 81.1496 from the data above

# # 3. create a program that takes a score and shows the grade based on the score

# # eg.

# # 90 - 100 ("Grade A")
# # 70 - 89 ("Grade B")
# # 50 - 69 ("Grade c")
# # 30 - 49 ("Grade D")
# # 0 - 29 ("Grade F")

# # 4. record = "this is the time to attend python training"
# # bring out the words that start from 't'

# # 5. words = 'Python is not hard. Do you agree'
# # Print every word in this sentence above that has an even number of letters

# # function
# def add():
#     print(2 + 2) 
# add()
# # function parameter
# def add(x, y):
#     print(x + y) 
# add(2, 2)
# add(5, 3)
# add(1, 3)
# add(1, 6)
# def welcome(username= "guest"):
#     return "welcome " + username
# print(welcome("wale"))

# import calcula
# calculator.
