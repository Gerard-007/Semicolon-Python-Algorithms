balance = 0

while True:
	option = int(input("""
	Enter 1 to deposit
	Enter 2 to withdraw
	Enter 3 to check balance
	Enter 0 to exit
	>> """))
	
	if option == 0:
		break
	match option:
		case 1:
			deposit = float(input("Enter an amount to deposit: "))
			if deposit > 0:
				balance += deposit
				print(f"{deposit} deposited successfully.")
			else:
				print(f"{deposit} cannot be less than or equals zero.")
		case 2:	
			withdraw = float(input("Enter an amount to withdraw: "))
			if balance > withdraw:
				balance -= withdraw
				print(f"{withdraw} witdrawal was successful.")
			else:
				print(f"Insufficient balance.")
		case 3:
			print(f"Your current balance is N{balance}")

