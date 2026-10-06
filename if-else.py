# if False:
#     print("True : if executes")
# else: 
#     print("False : else executes")   


# check given number is 10 or not
 
n=int(input("Enter a Number : "))
if n==10:
    print("True equal to 10")  
else:
    print("False")  


# check whether given number is positive or negative

n=int(input("Enter a Number : "))
if n>10:
    print("positive given number")  
else:
    print("negative given number") 


# chech biggest numbers between two values

n1=int(input("Enter a Number 1 : "))
n2=int(input("Enter a Number 2 : "))
if n1>n2:
    print("n1 is greater than n2")  
else:
    print("n2 is greater than n1") 



# check given number is Even or not

n1=int(input("Enter number : "))       
if n1%2==0:
    print("Even number") 
else:
    print("Not an Even number")    

#check given number is Odd or not

n1=int(input("number 1 : "))       
if n1%2!=0:
    print("Odd number")  
else:
    print("Not Odd number")   


# check given value is vowel or not

string=input("Enter a characer : ")
if string=="a" or string=="e" or string=="i" or string=="o" or string=="u":
    print("vowel")
else:    
    print("not vowel")   


# check given value is alphabet or not

string=input("Enter a characer : ")
if string>="A" and string>="Z" or string>="a" and string>="z":
    print("Alphabet")
else:
    print("not Alphabet")    

# check given number digit or not

n=int(input("Enter a Number : "))  
if n>=0 and n<=9:
    print(n," is a digit")  
else:
    print(n," is not a digit")

# write a program when name=hero and password=hero@123 output will be login successful otherwise invslid credentials 

name=input("Enter name : ")
password=input("Enter password : ")
if name=="Hero" and password=="Hero@123":
    print("login succeess")
else:
    print("invalid login")    