from bank import Bank
from account import Account

# Create a new bank
new_bank = Bank(
    "Dami & Tobi Bank",
)

def create_account():
    name: str = input("Enter your name: ").strip().title()
    phone: str = input("Enter your phone number: ").strip()
    pin: str = input("Enter your pin: ").strip()
    account = new_bank.register_account(name, phone, pin)
    print(f"""
        Account created successfully
        Account name: {account._name}
        Account number: {account.account_number}
        Account phone: {account.phone}
    """)

def deposit_money():
    ...

def withdraw_money():
    ...

def check_balance():
    ...

def main():
    option = input("""
        Enter 1 to add account
        Enter 2 to deposit money
        Enter 3 to withdraw money
        Enter 4 to check balance
        >>
    """)
    match option:
        case "1":
            create_account()
        case "2":
            deposit_money()
        case "3":
            withdraw_money()
        case "4":
            check_balance()
        case _:
            print("Invalid option selected")

if __name__ == "__main__":
    main()