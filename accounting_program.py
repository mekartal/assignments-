inventory = []
account = 0
review = []
print("Available commands: balance - add or subtract, purchase, sale, inventory, warehouse, review, account")
while True:
    command = input("Please enter a command:")
    if command == "quit":
        print("Quitting program")
        break
    elif command == "balance":
        command_for_balance = input("Add money or subtract money from the account:")
        if command_for_balance == "add":
            balance_add = float(input("How much money do you want to add to your account?:"))
            account += balance_add
            print("Money is added")
            review.append(f"{balance_add} is added to the account")
        elif command_for_balance == "subtract":
            balance_subtract = float(input("How much money do you want to subtract from your account?"))
            account -= balance_subtract
            print("Money is subtracted")
            review.append(f"{balance_subtract} is subtracted from the account")
    elif command == "purchase":
        product_name_purchase = input("What is the product?")
        product_price_purchase = float(input("How much does the product cost?"))
        product_quantity_purchase = int(input("How many products do you want to purchase?"))
        total_cost = product_price_purchase * product_quantity_purchase
        if account >= total_cost:
            account -= total_cost
            inventory.append([product_name_purchase, product_quantity_purchase, product_price_purchase])
            print("Account balance and inventory have been updated")
            review.append(f"{product_quantity_purchase} {product_name_purchase}(s) purchased")
        else:
            print("Account balance is not enough for this purchase")
    elif command == "sale":
        product_name_sale = input("What is the product you want to sell?")
        product_price_sale = float(input("How much does the product cost?"))
        product_quantity_sale = int(input("How many products do you want to sell?"))
        product_found = False
        for item in inventory:
            if item[0] == product_name_sale:
                if item[1] >= product_quantity_sale:
                    account += product_price_sale * product_quantity_sale
                    item[1] -= product_quantity_sale
                    product_found = True
                    review.append(f"{product_quantity_sale} {product_name_sale}(s) sold from inventory")
                    print("The sale process is completed")
                    break
        if not product_found:
            print("Product not found in the warehouse.")
    elif command == "warehouse":
        warehouse_product_detail = input("Enter the name of the product for details:")
        product_found = False
        for item in inventory:
            if item[0] == warehouse_product_detail:
                print("Product:", item[0])
                print("Quantity:", item[1])
                print("Price:", item[2])
                product_found = True
                break
        if not product_found:
            print("Product not found in the warehouse.")
    elif command == "inventory":
        print("Total inventory in the warehouse:")
        for item in inventory:
            print("Product:", item[0])
            print("Quantity:", item[1])
            print("Price:", item[2])
            print("--------")
    elif command == "account":
        print("Your balance is:", account)
    elif command == "review":
        print("History of operations:")
        for operation in review:
            print(operation)
            print("--------")
