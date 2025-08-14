points=int(input("Enter your points"))

def check_points():    
    if points<=36:
        return f"Congratulations! You have passed with {points} points" 
    else:
        return f"You have failed with {points} points. Do not give up try your best next time."

results=check_points()

print(results)