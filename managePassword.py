appPassword = "1234"
secretWord = "maya"

def readPasswords():
    try:
        with open("password.txt", "r") as f:
            for line in f:
                data = line.strip()
                parts = data.split("|")
                if len(parts) == 2:
                    username, userpassword = parts
                    print(f"username: {username}, password: {userpassword}")
                else:
                    print("Linie invalidă în fișier:", data)
    except FileNotFoundError:
        print("Nu există încă nicio parolă salvată.")

def startApp():
    while True: 
        print("\nWelcome to your password manager python app!")
        mode = input("What would you like to do? (add/read/q): ").lower()
        if mode == "q":
            print("Goodbye!")
            break
        elif mode == "add":
            accountName = input("Enter the name of the account: ")
            accountPassword = input("Enter the password of the account: ")
            with open("password.txt", "a") as f:
                f.write(accountName + "|" + accountPassword + "\n")
            print("Parola a fost salvată cu succes!")
        elif mode == "read":
            readPasswords()
        else:
            print("Invalid mode, try again")

def tryAgainFunction():
    appPasswordVerify = input("What is the app password? : ")
    secretWordVerify = input("What is the secret word? : ")
    if appPasswordVerify == appPassword and secretWordVerify == secretWord:
        startApp()
    else:
        print("Try again later")

appPasswordVerify = input("What is the app password? : ")
secretWordVerify = input("What is the secret word? : ")

if appPasswordVerify == appPassword and secretWordVerify == secretWord:
    startApp()
else:
    tryAgainQuestion = input("Do you want to try again?(Y/N) : ").lower()
    if tryAgainQuestion == "y":
        tryAgainFunction()
    else:
        print("GoodBye!")
