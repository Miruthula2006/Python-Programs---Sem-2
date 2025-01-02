import re
def verify_password(password):
    ex=r'^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?!.([!@#$%^&*()_-+=)]).{8,}$'
    
    if re.match(ex,password):
        print("Password is Strong")
    else:
        print("Password is not Strong")

password=input("Enter the Password: ")
verify_password(password)
