# Strings are immutable which means that you cannot change them by running functions on them

name = "Harry"
#       01234 .......Indexing

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)

character1 = name[1]  # start from index 1 and get only one character
print(character1)


#******************************** Slicing
print(name[0:3])

print(name[-4: -1]) # just replace it my corrosponding positive No.
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

print(name[::-1]) # it reversed the string value

# ****************************String Funtions 
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.count('r'))
print(name.find('a')) # gives Index

print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))


# How string and variables works together
name = input("Enter your name: ")
print(f"Good Afternoon, {name} ") 
