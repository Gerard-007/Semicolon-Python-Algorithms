def calculate_number_of_boxes(guest, slices):
    number_of_boxes = guest // slices

    if guest % slices != 0:
        number_of_boxes += 1
    return number_of_boxes

def display_status(pizza_type, box_sizes, number_of_slices, guests, pizza_price):
    print(f"""
    - Required pizza type: {pizza_type}
    - Number of boxes to buy: {box_sizes}
    - Number of slices: {box_sizes * number_of_slices}
    - Number of slices left over: {(box_sizes * number_of_slices) - guests}
    - Total price: N{pizza_price * box_sizes:.2f}
    """)

def pizza_checkout(guests):
    if guests <= 4:
        pizza_type = "Super Size"
        pizza_price = 2000
        number_of_slices = 4
    elif guests <= 6:
        pizza_type = "Small Money"
        pizza_price = 2400
        number_of_slices = 6
    elif guests <= 8:
        pizza_type = "Big Boys"
        pizza_price = 3000
        number_of_slices = 8
    elif guests <= 12:
        pizza_type = "Odogwu"
        pizza_price = 4200
        number_of_slices = 12
    else:
        print("Guests exceed the limit for available pizza sizes.")
        return

    box_sizes = calculate_number_of_boxes(guests, number_of_slices)
    display_status(pizza_type, box_sizes, number_of_slices, guests, pizza_price)


while True:
    num_of_guests = int(input("Enter the number of guests: "))
    
    if num_of_guests != 0:
        pizza_checkout(num_of_guests)
    else:
        print("Exiting program...")
        break
