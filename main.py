from User import User
from hash import verify_password

users = []
author = None

def create_new_user():
    print("------------- Creating New User -------------")
    name = input("Enter Your Name: ")
    password = input("Enter A Password: ")
    new_user = User(name, password)
    users.append(new_user)
    print("------------- User Created Successfully -------------")

def operation():
    while True:
        print("########################-:- User Penal -:-########################")
        print("Enter 1. Check Savings Account")
        print("Enter 2. Check current Account")
        print("Enter 3. Create a Savings Account[Interest Rate: 3.5%]")
        print("Enter 4. Create a Current Account")
        print("Enter 5. Deposit Money in Savings Account")
        print("Enter 6. Deposit Money in Current Account")
        print("Enter 7. Withdraw Money from Savings Account")
        print("Enter 8. Withdraw Money from Current Account")
        print("Enter 9. To Go Back")
        op = int(input("Enter choice "))

        if op == 1:
            if not author.savings_Account == None:
                print("::::::::::::::::-- User Savings Accounts Details --::::::::::::::::")
                print(f"Account Number: {author.savings_Account.account_number}")
                print(f"Account Holder: {author.savings_Account.account_holder}")
                print(f"Balance       : {author.savings_Account.balance}")
                print("::::::::::::::::--=================================--::::::::::::::::")
            else:
                print(f"::::::::::::::::-- No Savings Account Found for the User --::::::::::::::::")
        elif op == 2:
            if not author.current_Account == None:
                print("::::::::::::::::-- User Savings Accounts Details --::::::::::::::::")
                print(f"Account Number : {author.current_Account.account_number}")
                print(f"Account Holder : {author.current_Account.account_holder}")
                print(f"Overdraft Limit: {author.current_Account.overdraft_limit}")
                print(f"Balance        : {author.current_Account.balance}")
                print("::::::::::::::::--=====================--::::::::::::::::")
            else:
                print(f"::::::::::::::::-- No Current Account Found for the User --::::::::::::::::")
        elif op == 3:
            result = author.create_savings_acc()
            if result:
                print(f"Savings Account Created for user: {author.name}")
            else:
                print(f"Cannot Create Savings Account for user: {author.name}")
        elif op == 4:
            result = author.create_current_acc()
            if result:
                print(f"Current Account Created for user: {author.name}")
            else:
                print(f"Cannot Create Current Account for user: {author.name}")
        elif op == 5:
            if not author.savings_Account:
                print(f"Savings Account not found for user: {author.name}")
                continue
            amt = int(input("Enter amount to be deposited: "))
            result = author.savings_Account.deposit(amt)
            if result:
                print(f"Amount {amt} Deposited Successfully.")
            else:
                print(f"Something went wrong. Try again later.")
        elif op == 6:
            if not author.current_Account:
                print(f"Current Account not found for user: {author.name}")
                continue
            amt = int(input("Enter amount to be deposited: "))
            result = author.current_Account.deposit(amt)
            if result:
                print(f"Amount {amt} Deposited Successfully.")
            else:
                print(f"Something went wrong. Try again later.")
        elif op == 7:
            if not author.savings_Account:
                print(f"Savings Account not found for user: {author.name}")
                continue
            amt = int(input("Enter amount to be credited: "))
            result = author.savings_Account.withdraw(amt)
            if result:
                print(f"Amount {amt} credited from user: {author.name} account type: Savings successfully")
            else:
                print("Something went wrong. Try again later.")
        elif op == 8:
            if not author.current_Account:
                print(f"Current Account not found for user: {author.name}")
                continue
            amt = int(input("Enter amount to be credited: "))
            result = author.current_Account.withdraw(amt)
            if result:
                print(f"Amount {amt} credited from user: {author.name} account type: Current successfully")
        elif op == 9:
            break
        else:
            print("Enter a valid choice");
    
def login_user():
    print("------------- Login -------------")
    global author
    name = input("Enter Your Name: ")
    password = input("Enter A Password: ")
    for user in users:
        if user.name == name:
            result = verify_password(password, user.password)
            if result:
                author = user
            else:
                print("Wrong Credentials")
                print("------------- Login Failed -------------")
                return False
    if author == None: 
        print("User not found")
        print("------------- Login Failed -------------")
        return False
    return True
                
while True:
    print("########################-:- Welcome to Bank Account Management System-:- ########################")
    print("1. Register an User")
    print("2. Login an User")
    print("3. List of User")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        create_new_user()
        
    elif choice == 2:
        result = login_user()
        if result:
            operation()
            author = None

    elif choice == 3:
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ User List +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        for user in users:
            print("===============================================================")
            print(f"Name: {user.name}")
            if not user.savings_Account == None:
                print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-| Savings Account Details |-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
                print(f"Account Number: {user.savings_Account.account_number}")
                print(f"Account Holder: {user.savings_Account.account_holder}")
                print('***********************************************************************************')
            if not user.current_Account == None:
                print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-| Current Account Details |-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
                print(f"Account Number: {user.current_Account.account_number}")
                print(f"Account Holder: {user.current_Account.account_holder}")
                print('***********************************************************************************')
                
            print("===============================================================")
    
    elif choice == 4:
        print("Thank for using Bank Account Management System")
        break
    
    else: 
        print("Enter a valid option")
        