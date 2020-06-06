from AccountDao import AccountDao

if __name__ == '__main__':
    
    dbIterator = AccountDao()

    while True:
        print("Enter NEW to create a new account")
        print("Enter LOG to log in an existing account")
        print("Enter QUIT to exit the process")

        req = input()

        if req == "NEW":

            username = input("Insert your new username\n")
            password = input("Insert your new password\n")
            
            if dbIterator.findAccount(username) == None:
                dbIterator.addAccount(username, password)
            else:
                print("Username already present. Please try again.")

        elif req == "LOG":

            username = input("Insert your username\n")
            password = input("Insert your password\n")

            queried_account = dbIterator.findAccount(username)

            if queried_account == None:
                print("Username not present. Please create a new Account first.")
            else:
                if dbIterator.verifyAccount(queried_account['password'], password):
                    print("You have successfully logged in!!!!!!")
                else:
                    print("Invalid Password")
             
        elif req == "QUIT":
            break
        else:
            print("No actions available")
