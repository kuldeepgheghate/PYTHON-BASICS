#................. If else.....................  

a = int(input("Enter ur Age:"))

if(a>18):  #...................this is syntax (intentation is matters  )
    print("Ur Adult")
      
else:
    print("ur chotu")
    
    
# ..................If elif else ladder.............................

b = int(input("Enter ur Age:"))   

if(b>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(b<0):
    print("You are entering an invalid negative age")

elif(b==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")


print("End of Program")


# ..................Multiple if statements........................

a = int(input("Enter your age: "))

# If statement no: 1  ........................># ( IF akala ho sakata hai but else & elif akala nhi ho sakata  )
if(a%2 == 0):
    print("a is even")
# End of If statement no: 1

# If statement no: 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")  

else:
    print("You are below the age of consent")
# End of If statement no: 2

print("End of Program")


        
    
                                     
    
    