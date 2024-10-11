def investment(number_of_years, amount_of_investment):
    interest = 0
    for i in range(number_of_years):
        interest = amount_of_investment * 0.1
        amount_of_investment += interest
        print(f"""
            Year {i+1}
            Amount: {amount_of_investment:,.2f}
            Interest: {interest}
        """)


while True:
    try:
        number_of_years = int(input("Enter number of years or enter 0 to exit: "))
        if number_of_years == 0:
            print("Exiting program")
            break
        amount_of_investment = float(input("Enter amount to invest or enter 0 to exit: "))
        if amount_of_investment == 0:
            print("Exiting program")
            break
        if number_of_years < 0:
            print("Number of years must be more than 1!")
        elif amount_of_investment < 0:
            print("Amount to invest must be more than 1!")
        investment(number_of_years, amount_of_investment)
    except Exception as e:
        print(f"Invalid input! enter a number!\nRead more: {e}")
