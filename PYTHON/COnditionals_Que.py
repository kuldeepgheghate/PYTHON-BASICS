# Q 1 > Find the greatest among 4 No.

a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a4:", a4)
    
    
    
# Q 2 > weather the student is pass or fail if he have > 40% and atleast should have > 33 in each subject 

marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)   
      
 
 
 # Q 3 > Write a program to delete the spam Comment that are : "Make a lot of money", "buy now" , "subscribe this", "click this"
 
 # We are using ( in ) key word which check weaher it is a substring of main string or not
 
p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"

message = input("Enter your comment: ") # String 

if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)): # .. using in key word
    print("This comment is a spam")

else:
    print("This comment is not a spam")
    
    
    
# Q 5 check weather the names of students is present in the list or not 

l = ["Harry", "Rohan", "Shubham", "Divya"]

name = input("Enter your name: ")

if(name in l):                              # using in key word 
    print("Your name is in the list")
else:
    print("Your name is not in the list")    