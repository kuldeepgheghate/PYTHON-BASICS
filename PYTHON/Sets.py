
# A set is a Immutable ( we can't change it )

e = set() # creat empty set, Dont use s = {} as it will create an empty dictionary

s = {1, 5, 32, 54,5, 5, 5, "Kuldeep","Kuldeep"} 
print(s) # sets can't print duplicate values

# Methods of set 

print(s, type(s)) # print type
s.add(566) # add at last 
s.remove(1) # sets don't have index we have to directly use values from it


s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2)) 

# Q 2
# write 18 as number and string in set
s = set()
s.add(18)
s.add("18")
print(s)

 # .......... Interview ask Q
t = set()
t.add(20)
t.add(20.0)
t.add('20') # length of s after these operations?

print(len(t)) # hear we have 3 different values but the length will be 2 because in python
# we can't have duplicate values in set even if they are different data types


# Q 10
#...... Can we update the value of list which is inside the Set ( No we can't update the list in the set ) 
# 1. we can't add List in the set 
k = {20, 30, 10, "kuldeep", [1,2]}
print(k) 