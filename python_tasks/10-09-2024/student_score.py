def student_score(score):
	
	


def main():
	students = 0
	scores = 0
	average = 0

	while True:
		option = input("""Enter score or N/0 to exit program
		>> """)

		match option.lower():
			case "0":
				print("Exiting application...")
				break
			case "n":
				print("Exiting application...")
				break
			case "s":
				score = int(input("Enter student score: "))
				if score <= 0 or score > 100:
					print("Score should be between 1 to 100")
			
