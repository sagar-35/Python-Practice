secret_password = "Cyber2025"

while True: #this is for infinite loop
    guess = input("Enter Password: ")

    if guess == secret_password:
        print("Acess Granted!")
        break
    else:
        print("Wrong Password! Try Again.")
