
inventory = []
account = 0
list = []
product_quantity_sale =0
review = []

print("Available commands : balance - add or subtract , purchase , sale , list, warehouse , review ,account ")

while True : 
    command = input ("Please enter a command:")

    if command == "quit" :
        print ( "Quitting program")
        break
        

    elif command == "balance" :
        command_for_balance = input("Add money or subtract money from the account:")
        if command_for_balance == "add" :
             balance_add = float (input ("How much money do you want add to your account ?:"))
             account = balance_add + account
             print ("Money is added")
             review.append(f"{balance_add} is added to  the account ")
            
        elif command_for_balance == "subtract" :
            balance_subtract = float(input ("how much money do you want subtract from your account ?"))
            balance = balance - balance_subtract
            print ("Money is subtracted")
            review.append(f"{balance_add}is subtracted from thw account")
    
    elif command == "purchase":
        product_name_purchase = input ("What is the product ?:")
        product_price_purchase = float(input("How much does a product ?:"))
        product_quantity_purchase = int (input ("How many product ?:"))
        account = account - (product_quantity_purchase*product_price_purchase)
    
        if account <0:
            account= account + (product_quantity_purchase*product_price_purchase)
            print ("Account balance is not enough for this purchase")

        else:
            
            list += product_name_purchase , product_quantity_purchase , product_price_purchase
            print ("Account balance and list have been updated")
            review.append(f"{product_name_purchase,product_price_purchase,product_quantity_purchase} is added to the list")
    
        
    elif command == "sale" :
        product_name_sale = input ("what is the product ?")
        product_price_sale = float (input ("How much does a product ?"))
        product_quantity_sale = int(input ("How many product : "))
        if product_name_sale not in list :
            print ("This product is not in the warehouse")
        elif product_quantity_purchase < product_quantity_sale:
            print("there are not enough products to sell for this sale")
        else:
            product_quantity_purchase=product_quantity_purchase - product_quantity_sale
        
            account= account + (product_price_purchase*product_quantity_purchase)
            list = product_name_purchase , product_quantity_purchase ,product_price_purchase
            review.append(f"{product_quantity_sale ,product_name_sale} sold from inventory")
            print ("The sale process is completed")
            

    elif command == "warehouse":
        warehouse_product_detail = input ("Enter the name of the products for details:")
        if warehouse_product_detail in list:
            print("Product :" , product_name_purchase)
            print("Quantity:" , product_quantity_purchase)
                  
        else:
            print("Product not found in the warehouse.")

    elif command == "list":
        print("Total inventory in the warehouse :", list), 
    
    elif command == "account":
        print (("Your balance is:") ,account )

    elif command == "review":
        print("History of operations:",review)


        

    


            

    
        




