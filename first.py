menu = {
    "pizza": 110,
    "burger": 150,
    "normalpasta": 80,
    "specialpasta": 150,
    "coffee": 80,
    "greentea": 100,
    "nuggets": 120
}

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")
    print()

def take_order():
    while True:
        order = input("Please place your order, what do you want sir: ").lower()
        if order in menu:
            return order
        else:
            print("Sorry, we don't have that item. Please order from the menu.")

def main():
    order_total = 0
    print("Welcome to our restaurant!")
    
    while True:
        display_menu()
        order = take_order()
        order_total += menu[order]
        print(f"{order} added to your order. Current total: ₹{order_total}")
        
        second_order = input("Do you want to order something more, sir? (Yes/No): ").lower()
        if second_order == "no":
            break
        elif second_order != "yes":
            print("Invalid response. Assuming you don't want to order more.")
            break

    print(f"Your total bill is ₹{order_total}.")
    print("Thank you for your patronage, sir!")

# Run the program
main()
