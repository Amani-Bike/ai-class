num=float(input("Enter the first number "))
operator=str(input("Enter the operator "))
num2=float(input("Enter the second number "))

def calculator():
    if operator=="+":
        return f"The result of your problem is {num+num2}"
    elif operator=="-":
        return f"The result of your problem is {num-num2}"
    elif operator=="*":
        return f"The result of your problem is {num*num2}"      
    elif operator=="/":
        if num2==0:
            return "Math error...! A number can not be divided by 0"
        else:    
            return f"The result of your problem is {num/num2}"        
    else:
        return "Math error...! Please check your inputs properly"

result=calculator()
print(result)             