def convert_to_list(enter_lucky_number):
    result = []
    entered_numbers = enter_lucky_number.split(",") if "," in enter_lucky_number else enter_lucky_number.split(" ")
    if len(entered_numbers) < 3 or len(entered_numbers) > 3:
        return "Error! you are only permitted to enter 3 numbers differentiated with either space or comma."
    for num in entered_numbers:
        result.append(int(num))
    return result


def run_lucky_draw(converted_list):
    lucky_numbers = [0, 0, 7]

    if lucky_numbers == converted_list:
        return "You won $5000 three out of the numbers are correct and in order!"
    else:
        count = 0
        for number in lucky_numbers:
            if number in converted_list:
                count += 1
        if count == 1:
            return"You won! $2000 one out of the lucky draw was correct!"
        elif count == 2:
            return"You Won! $3000 two out of the lucky draw was correct!"
        elif count == 3:
            return"You Won! $4000 three out of the lucky draw was correct! but not in the same order"


enter_lucky_number = input("Enter your lucky numbers it should be in this format 0, 0, 0: ")
converted_list = convert_to_list(enter_lucky_number)
print(run_lucky_draw(converted_list))