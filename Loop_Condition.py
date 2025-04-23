secret_password = "cyber2025"

while True:
    guess = input("Enter Password: ")

    if guess == secret_password:
        print("Access Granted!")
        break
    
    else:
        print("Wrong Passwod! Please Try Again.")