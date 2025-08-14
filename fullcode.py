def kilometers_converter():
    kilometers = float(input("Enter kilometers "))
    miles = kilometers*0.621371
    print(f"{kilometers} km = {miles:.2f} miles")

def temp_converter():
    temp_c = float(input("Enter Celcius "))
    temp_f = (temp_c*9/5)+32
    print(f"{temp_c} °C = {temp_f:.2f} °F")

def discount_calculation():
    cost = float(input("Enter the cost ")) 
    if cost > 100:
        final = cost * 0.8
    elif cost >= 50:
        final = cost * 0.9    
    else:
        final = cost   
    print(f"Discounted cost is MK {final:.2f}")    

def main():
    print("Welcom to smart tools")
    print("1. Kilometers to Miles")
    print("2. Temperature Converter (C to F)")
    print("3. Shop Discount Calculator")     

    choice = input("Choose an option (1-3): ")
    if choice == "1":
        kilometers_converter()
    elif choice == "2":
        temp_converter()
    elif choice == "3":
        discount_calculation()
    else:
        print("Invalid choice. Try again.")            
main()