# List are Mutable we can change it , but can't do slicing like string

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"] # add any data type in a list

print(friends)
print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])

friends.append("Harry")  # Adding element at the end of the list using append
print(friends)


l1 = [1, 34,62, 2, 6, 11]
 #l1.sort()
 #l1.reverse()
 #l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
 
value = l1.pop(3) # pop function remove 3 index value
print(value)
print(l1)


# Q 1 ....................User input
marks = []
f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)

marks.sort() # sorting them

print(marks)


#Q 2
l = [3, 3, 5, 1]

print(sum(l)) # gives addition