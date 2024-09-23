"""
- Declare a constant <PRICE> to store the fuel price
- Request a number from user and represent the value as <litres>
- Multiply <PRICE> by <litres> entered by the user and Display
- Convert this to function.
"""

PRICE = 855

def price_per_litre():
	try:
		litres = float(input("How much litres do you wish to buy: "))
		print(f"Total price for {litres:.0f} is N{litres * PRICE}\n\n")
	except Exception as e:
		print(f"Invalid input {e}\n\n")


def price_per_budget():
	try:
		budget = float(input("How much fuels did you budget to buy: "))
		print(f"Total litre for N{budget} is {budget / PRICE:.2f}")
	except Exception as e:
		print(f"Invalid input number/decimal number expected {e}")
	

# Sell fuel in litres to a customer...
price_per_litre()


# Sell fuel price to a customer...
price_per_budget()
