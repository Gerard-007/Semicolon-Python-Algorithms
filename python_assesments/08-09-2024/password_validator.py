def is_valid_password(password) -> bool:
	if len(password) < 10:
		return False
	# characters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "_", "="]
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	# character_count = 0
	number_count = 0
	for p in password:
		# if p in characters:
			# character_count += 1
		if p in numbers:
			 number_count += 1
	return True if number_count >= 3 else False


set_password = is_valid_password("Gerard12345")


if set_password:
	print("Password is valid")
else:
	print("Password is invalid")