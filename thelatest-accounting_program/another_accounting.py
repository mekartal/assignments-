from ast import literal_eval

def load_inventory(file_name):
    try:
        with open(file_name, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("File does not exist! Creating a new file.")
        return {}

def save_inventory(file_name, inventory, account):
    data = {
        'inventory': inventory,
        'account': account
    }
    with open(file_name, 'w') as file:
        file.write(str(data))

file_name = input("Please provide a name of a file (including extension, e.g., txt): ")
inventory_data = load_inventory(file_name)

inventory = inventory_data.get('inventory', {})
account = inventory_data.get('account', 0)
review = []

print("Available commands: balance - add or subtract, purchase, sale, inventory, warehouse, review, account, quit")

while True:
    command = input("Please enter a command: ")

    if command == "quit":
        print("Quitting program")
        save_inventory(file_name, inventory, account)
        break
    
    elif command == "balance":
        command_for_balance = input("Add money or subtract money from the account: ")

        if command_for_balance == "add":
            balance_add = float(input("How much money do you want to add to your account?: "))
            account += balance_add
            print("Money is added")
            review.append(f"{balance_add} is added to the account")

        elif command_for_balance == "subtract":
            balance_subtract = float(input("How much money do you want to subtract from your account?: "))
            account -= balance_subtract
            print("Money is subtracted")
            review.append(f"{balance_subtract} is subtracted from the account")

    elif command == "purchase":
        product_name_purchase = input("What is the product?: ")
        product_price_purchase = float(input("How much does the product cost?: "))
        product_quantity_purchase = int(input("How many products do you want to purchase?: "))
        total_cost = product_price_purchase * product_quantity_purchase

        if account >= total_cost:
            account -= total_cost
            if product_name_purchase in inventory:
                inventory[product_name_purchase] += product_quantity_purchase
            else:
                inventory[product_name_purchase] = product_quantity_purchase
            print("Account balance and inventory have been updated")
            review.append(f"{product_quantity_purchase} {product_name_purchase}(s) purchased")
            save_inventory(file_name, inventory)  # Save inventory after purchase
        else:
            print("Account balance is not enough for this purchase")

    elif command == "sale":
        product_name_sale = input("What is the product you want to sell?: ")
        product_price_sale = float(input("How much does the product cost?: "))
        product_quantity_sale = int(input("How many products do you want to sell?: "))

        if product_name_sale in inventory:
            if inventory[product_name_sale] >= product_quantity_sale:
                account += product_price_sale * product_quantity_sale
                inventory[product_name_sale] -= product_quantity_sale
                review.append(f"{product_quantity_sale} {product_name_sale}(s) sold from inventory")
                print("The sale process is completed")
                save_inventory(file_name, inventory)  # Save inventory after sale
            else:
                print("Not enough quantity available in the inventory.")
        else:
            print("Product not found in the warehouse.")

    elif command == "warehouse":
        warehouse_product_detail = input("Enter the name of the product for details: ")

        if warehouse_product_detail in inventory:
            print("Product:", warehouse_product_detail)
            print("Quantity:", inventory[warehouse_product_detail])
        else:
            print("Product not found in the warehouse.")

    elif command == "inventory":
        print("Total inventory in the warehouse:")

        for product, quantity in inventory.items():
            print("Product:", product)
            print("Quantity:", quantity)
            print("--------")

    elif command == "account":
        print("Your balance is:", account)

    elif command == "review":
        print("History of operations:")

        for operation in review:
            print(operation)
            print("--------")