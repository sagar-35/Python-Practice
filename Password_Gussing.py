secret_password = "Cyber2025"

while True: #this is for infinite loop
    guess = input("Enter Password: ") #user_input

    if guess == secret_password: #condition
        print("Access Granted!")
        break
    else:
        print("Wrong Password! Try Again.")
