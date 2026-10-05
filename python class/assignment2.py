# Assignment 2

# 1. record = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['python']]}]}]}
# print out python from the record above
record = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['python']]}]}]}
print(record['k1'][2]['k2'][1]['tough'][2][0])

# 2. data = [
#   {
#     "id": 1,
#     "name": "Leanne Graham",
#     "username": "Bret",
#     "email": "Sincere@april.biz",
#     "address": {
#       "street": "Kulas Light",
#       "suite": "Apt. 556",
#       "city": "Gwenborough",
#       "zipcode": "92998-3874",
#       "geo": {
#         "lat": "-37.3159",
#         "lng": "81.1496"
#       }
#     }
#   }
# ]
# print put 81.1496 from the data above

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

print(data[0]["address"]["geo"]["lng"])

# 3. create a program that takes a score and shows the grade based on the score
# eg.
# 90 - 100 ("Grade A")
# # 70 - 89 ("Grade B")
# # 50 - 69 ("Grade c")
# # 30 - 49 ("Grade D")
# # 0 - 29 ("Grade F")

# score = float(input("Enter your score:"))

# if score >= 90 and score <= 100:
#     print("Grade A")
# elif score >= 70 and score <= 90:
#     print("Grade B")
# elif score >= 50 and score <= 70:
#     print("Grade C")
# elif score >= 30 and score <= 50:
#     print("Grade D")
# elif score >= 0 and score <= 30:
#      print("Grade F")
# else:
#      print("invalid score")   

# 4. record = "this is the time to attend python training"
# bring out the words that start from 't'
record = "this is the time to attend python training"

words = record.split()
for word in words:
    if word.startswith('t'):
     print(word)

# 5. words = 'Python is not hard. Do you agree'
# Print every word in this sentence above that has an even number of letters

words = 'Python is not hard. Do you agree'

for word in words.split():
    if len(word) % 2 == 0:
        print(word)

students = [
    {"name": "wale", "grade": 10},
    {"name": "mary", "grade": 15},
    {"name": "obi", "grade": 19},
    {"name": "chi", "grade": 9}
]
for i in students:
    if i["grade"] > 10:
        print(i["name"])

# import calculator
# calculator.add_it(2,4)
from calculator import *
div_it(12,4)
sub_it(42, 34)
add_it(2, 4)
#  module
# import os
# # os.mkdir("tech365")
# os.chdir("tech365")
# print(os.getcwd())
# os.mkdir("tech365")
#  working with files
# myfile = open("Bede.txt", "w")
# myfile.write( " i will studey and understand devOps in jesus name")
# myfile.close()
myfile = open("Bede.txt", "r")
# myfile.write( "\n learning with tech365")
# # myfile.close()
print(myfile.read())