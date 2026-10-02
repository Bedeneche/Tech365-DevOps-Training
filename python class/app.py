print(3+2)
print('Bede')
print("2+2")
# variable is a container that stores data
# example of variable
 
first_name = "Bede" 
age = 18
print(first_name, age)
print("i am", age ,"year old")

# variable rules
# 1. cant start with a number
# 2. cannot contain spaces
# 3. cannot contain speial characters except underscore
# 4.  should be descriptive
# 5. case sensitive 
# 6. dont use reserved words
 # data types

 #1. strings
address = "soji adeomo ikeja close"
print(address)
print(type(address))
print(len(address))
# indexing

print(address[3])
print(address[-1])

# slicing
print(address[-5:])
print(address[:4])
numbers = "123456789"
print(numbers[1:9:2])
print(numbers[1::3])
# string
print(address.upper())
print(address.lower())
print(address.capitalize())
print(address.title())
print(address.count("a"))
print(address.lower().count("e"))
print(address.endswith("e"))
print(address.startswith('s'))
print(address.index('ikeja'))
print(address.strip())
print(address.encode())
