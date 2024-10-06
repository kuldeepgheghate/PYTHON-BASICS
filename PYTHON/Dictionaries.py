#Dictionaries are mutable in Python, which means they can be changed after they are created. 

d = {}    # Empty dictionary ........( Ask in interview )
marks = {
    "Harry": 100,   # harry is key , 100 is value
    "Shubham": 56,
    "Rohan": 23
}


print(marks, type(marks)) # syntax to print the Dict
print(marks["Harry"])

# Methods of DIct

print(marks.items()) # it seperates both keys and values 
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Renuka": 100})
print(marks)

# print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error


# Q 1
words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}

Don = input("Enter the word you want meaning of: ")

print(words[Don]) # don is a variable words is dict 


# Q .... add 4 friends name with their fav language in Dict from user

d = {}  # empty dict


name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)