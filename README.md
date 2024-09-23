# coffee_machine

**Coffee Machine Project -**
**Overview:**
The Coffee Machine is a Python project that simulates a coffee vending machine. It allows users to order coffee drinks like espresso, latte, or cappuccino by providing enough change (quarters, dimes, nickels, and pennies). The machine checks if there are enough resources (milk, water, and coffee) and if the user has inserted enough money before making the drink.

**Features:**
**Drinks Available:**

Espresso
Latte
Cappuccino
**Resources Management:**

Tracks available amounts of water, milk, and coffee.
Deducts resources based on the drink ordered.
**Money Handling:****

Users insert change in quarters, dimes, nickels, and pennies.
The machine calculates the total money inserted and returns change if necessary.
If the money is insufficient, the order is cancelled, and the money is refunded.

**Status Report:**

The machine can print a report of its available resources and money collected.
****How it Works:**
Logo Display:

A coffee machine ASCII art is displayed when the program starts.
**User Input:**

The user is prompted to choose one of three coffee drinks (espresso, latte, cappuccino), or they can type report to see the machine's resource status.
Report:

**If the user types report, the machine prints:**
Remaining milk (ml)
Remaining water (ml)
Remaining coffee (g)
Total money collected ($)
**Order Processing:**

After choosing a drink, the user is asked to input how many quarters, dimes, nickels, and pennies they insert.
The machine checks:
If enough resources are available to make the drink.
If the inserted money is sufficient.
If all conditions are met, the machine makes the drink, updates its resources, and provides the change (if any).

Code Example:

# Sample to order a latte
user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
if user_input == "latte":
    latte()
Dependencies:
This project requires no external libraries. It is a simple console-based application running entirely on standard Python.

**Customization:**
You can modify each drink's ingredients and quantities by editing the MENU dictionary.
The initial resource quantities can be adjusted in the resources dictionary.

P**ossible Extensions:**
Add more drink types with different recipes.
Allow users to restock the machine with water, milk, or coffee.
Implement a user-friendly graphical interface using a GUI library like Tkinter.
Add the option for different currencies or pricing models.

**Enjoy your coffee! ☕**







Error Handling:

If resources are insufficient (milk, water, or coffee), the machine cancels the order and informs the user.
If the user doesn't insert enough money, the machine refunds the inserted money.
Usage:
Clone or download the repository to your local machine.
Ensure Python is installed on your system.
Run the coffee_machine.py file.
Choose from the available options to order a coffee or check the machine's status.
