def deposit(deposit_amount):
	if deposit_amount > 0:
		return deposit_amount
	return None
	

def withdraw(withdrawal_amount):
	if withdrawal_amount > 0:
		return withdrawal_amount}
	return None


def checkBalance():
	return f"Your current balance is N{balance}"



def main():
	balance = 0.00

	while True:
		option = input("""
		Enter "d" to deposit
		Enter "w" to withdraw
		Enter "b" to check balance
		Enter "n" or "0" to exit
		>> """)

		match option.lower():
			case "0":
				print("Exiting application...")
				break
			case "n":
				print("Exiting application...")
				break
			case "d":
				deposit_amount = float(input("Enter your amount to deposit: "))
				if deposit(deposit_amount) is not None:
					balance += deposit(deposit_amount)
					print(f"Amount N{deposit_amount} deposited successfully.")
			case "w":
				withdrawal_amount = float(input("Enter your amount to withdraw: "))
				if withdraw(withdrawal_amount) is not None and withdraw(withdrawal_amount) < balance:
					balance -= deposit(withdrawal_amount)
					print(f"Amount N{withdrawal_amount} withdrawal was successfully.")
			case "b":
				print(checkBalance())


main()