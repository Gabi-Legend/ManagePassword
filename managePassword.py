appPassword = "1234"
secretWord = "maya"

appPasswordVerify = input("What is the app pasword? : ")
secretWordVerify = input("What is the secret word? : ")

def tryAgainFunction():
    appPasswordVerify = input("What is the app pasword? : ")
    secretWordVerify = input("What is the secret word? : ")
    if appPasswordVerify == "1234" and secretWordVerify == "maya":
        pass
    else:
        print("Try again later")

if appPasswordVerify == "1234" and secretWordVerify == "maya":
    pass

else:
    tryAgainQuestion = input("Do you want to try again?(Y/N) : ").lower()
    if tryAgainQuestion == "y":
        tryAgainFunction()
    else:
        print("GoodBye!")