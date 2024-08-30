def calculate_total_amount(collection_rate):
	base_pay = 5000
	total_amount_per_parcel = None
	
	if collection_rate < 50:
		total_amount_per_parcel = (160 * collection_rate) + base pay
		print("N{total_amount_per_parcel} is your payment for {collection_rate} successful delivery")
	elif collection_rate >= 50 and collection_rate <= 59:
		total_amount_per_parcel = (200 * collection_rate) + base_pay
		print("N{total_amount_per_parcel} is your payment for {collection_rate} successful delivery")
	elif collection_rate >= 60 and collection_rate <= 69:
		total_amount_per_parcel = (250 * collection_rate) + base_pay
		print("N{total_amount_per_parcel} is your payment for {collection_rate} successful delivery")
	elif collection_rate >= 70:
		total_amount_per_parcel = (500 * collection_rate) + base_pay
		print("N{total_amount_per_parcel} is your payment for {collection_rate} successful delivery")


while True:
	collection_rate_input = int(input("Enter the number of guests: "))
	
	if collection_rate_input != 0:
		calculate_total_amount(collection_rate_input)
	else:
		print("Exiting program...")
		break