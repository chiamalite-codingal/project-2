Email = int(input("Do you want to open an email account? 1.Yes  2.No"))
age = int(input("Enter your age: "))
if Email==1:
    print("Allowed to create an account")
else:
    if age<=20:
        print("Allowed to create an account")
    else:
        print("Not allowed to create an account")        