# Restaurant Menu Ordering System

This is a simple Python console application that simulates a restaurant menu ordering system. Users can view a menu, place orders, and receive a total bill at the end of their session.

## Features
- Displays a menu with items and prices
- Allows users to place orders by typing the item name
- Handles invalid menu selections gracefully
- Supports multiple orders in a single session
- Calculates and displays the total bill

## How to Run
1. Make sure you have Python installed (version 3.x).
2. Open a terminal or command prompt.
3. Navigate to the project directory:
   ```
   cd path/to/restaurant_menu
   ```
4. Run the program:
   ```
   python first.py
   ```

## Example Usage
```
Welcome to our restaurant!
Menu:
pizza: ₹110
burger: ₹150
normalpasta: ₹80
specialpasta: ₹150
coffee: ₹80
greentea: ₹100
nuggets: ₹120

Please place your order, what do you want sir: pizza
pizza added to your order. Current total: ₹110
Do you want to order something more, sir? (Yes/No): yes
... (repeat ordering) ...
Your total bill is ₹230.
Thank you for your patronage, sir!
```

## Customization
You can add or remove menu items by editing the `menu` dictionary in `first.py`.

## License
This project is for educational purposes.
