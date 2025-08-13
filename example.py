def login(ueser_name, password):
    if ueser_name == "admin" and password == "password":
        return True
    return False

#invoke the function
print(login("admin","password"))
