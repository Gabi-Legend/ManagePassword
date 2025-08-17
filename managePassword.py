appPassword = "1234"
secretWord = "maya"

appPasswordVerify = input("What is the app pasword? : ")
secretWordVerify = input("What is the secret word? : ")

def startApp():
    print("Welcome to your password manager python app!")
    mode = input("What would you like to do, add password or see a existing password? press q to quit : ").lower()
    if mode == "q":
        print("Goodbye!")
    elif mode == "add":
        accountName = input("Enter the name of the account : ")
        accountPassword = input("Enter the password of the account : ")

        with open('password.txt', 'a') as f:
            f.write(accountName + " | " + accountPassword + '\n') 

def tryAgainFunction():
    appPasswordVerify = input("What is the app pasword? : ")
    secretWordVerify = input("What is the secret word? : ")
    if appPasswordVerify == appPassword and secretWordVerify == secretWord:
        startApp()
    else:
        print("Try again later")

if appPasswordVerify == appPassword and secretWordVerify == secretWord:
    startApp()

else:
    tryAgainQuestion = input("Do you want to try again?(Y/N) : ").lower()
    if tryAgainQuestion == "y":
        tryAgainFunction()
    else:
        print("GoodBye!")