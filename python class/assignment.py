# Assignment 

# 1. data = "1:A, 2:B, 3:C, 4:D, 5:E"
# Print out only the digits in the data above
# Expected output: 12345

# answer
data = "1:A, 2:B, 3:C, 4:D, 5:E"
print(data[0::5])

# 2. student_score = [1,2,3,[4,5,[6,7]]]
# in the student_score above, change 7 to 8
#answer
student_score = [1, 2, 3, [4, 5, [6, 7]]]
student_score[3][2][1] = 8
print(student_score)


# 3. words = "I am here"
# print out the word in reverse to read "here am I"
#answer
words = "I am here"

words = words.split()
words.reverse()

print(" ".join(words))

# 4. num = '123456789'
#  Print out the following from num 98765432
#answer
num = '123456789'
print(num[-1:-9:-1])

# 5. Mention 5 Benefits of DevOps
#devop helps to make the process of software delivery fast
#it helps to solve the problem of miscommications between devloper and operations
# it helps to reduce human man errors which through all the ways of software production
#it helps to solve the challages of friction and roadlocks that might delay in sofware delivery process
#it stregthen collaboration between developers and operations



# 6. You have joined SwiftCart as a junior DevOps engineer.
# The company currently uses these technologies:
# tools = ["Git", "Linux", "Docker", "Jenkins"]
# Prints the number of tools.
#answers
tools =  ["Git", "Linux", "Docker", "Jenkins"]
print(len(tools))

# 7. Adds "Kubernetes".
# Adds "AWS".
# answer
tools.append("Kubernetes")
tools.append("AWS")
print(tools)

# 8. Removes "Linux".
# answer
tools.pop(1)
print(tools)


# 9. Changes "Jenkins" to "GitHub Actions".
# answer
tools[2] = "GitHub Actions"
print(tools)


# 10. Print out Git and Jenkins
# 10 
print(tools[0:3:2])
num = "123456789"
print(num[-2:-9:-1])

data = "1:A, 2:B, 3:C, 4:D, 5:E"
print(data[0::5])

name = "dara"
print(name.replace("a","o"))
word = "God is good"
# print(" ".join(word.split()[ : : -1]))
sentence = "I love Python"
print(sentence.replace("Python", "Devops"))
print(name.upper().replace("A", "O"))
words = "  python  "
print(words.split())
print(word.split()[::-1])
print(" ".join(word.split()[::-1]))
print(name + name)
print(name * 3) 
employee = [
    {"name": "neche", "gender": "male"},
    {"name": "mary", "gender": "female"},
]
print(employee[1]["gender"])
print(employee[1]["name"])
print(employee[0]["gender"])
print(employee[0]["name"])

location = { 
    "street": "4 soji adepegba", "code":{
        "zip": 10001, 
        "course": ["devops","software"]
    }
}

print(location["code"]["course"][0])
print(location["code"]["zip"])
print(location["street"])
print(location["code"]["course"][1][-1])
score = [1,2,3,[4,5,[6,7]]]
score[3][2][1] = 8
print(score)

record ={'k1':[{'nest_key':['this is deep',['tech365']]}]}
print(record['k1'][0]['nest_key'][1][0])
# arithmetic operators
print(5 + 3)
print(5 - 3)
print(5 / 3)
print(5 % 3)
print(5 // 3)
print(5 * 3)
print(5 ** 3)

# comparison operator >,<,<=,>=,==
print(5 > 3)
print(5 < 3)
print(5 >= 3)
print(5 <= 3)
print(5 == 3)
print(5 != 3)

# # logical operator and, or, not
# print(5 > 3) and (2 > 3)
# print(5 > 3) or  (5 > 3)
# print(not(3 > 7))
# # assignment operator +=, -=, *=, /=
# x = 5
# y = 2
# x += y
# print(x)
# x -= y
# print(x)
# x *= y
# print(x)
# x /= y
# print(x)

A = {1,2,3}
B = {3,4,5}

age = 20
if age >= 18:
    print("you can vote")
else:
    print("not eligible")  

num = 0
if num > 0:
    print("positive") 
elif num < 0:
    print("negative") 
elif num == 0:
    print('zero')
else:
    print("whoareyou")    

x = 1
while x <= 3:
    print(x)
    x += 1