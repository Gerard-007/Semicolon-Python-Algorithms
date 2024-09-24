def format_number(number, width) -> str:
	num_str = str(number)
	if len(num_str) >= width:
		return num_str
	converted_number = ""
	for n in width - len(num_str):
		converted_number += '0'
	converted_number += num_str

	return str(converted_number)
	
	