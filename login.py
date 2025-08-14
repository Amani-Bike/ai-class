#login system
usernames = ["Aman","John","Pride","Paul","Tozi","Edson"]
password = ["123","abc","a12","b12","c12","ab1"]
userinput = input("Enter your name:  ")
userinput2 = input("Enter your password:  ")
valid = ""
for i in usernames:
    if userinput in usernames and userinput2 in password:
        valid += f"Welcome {userinput}"
        break   
    valid += f"{userinput} is not recognised or the password is incorect" 
    break
print(valid)
        
        