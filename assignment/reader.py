import csv
import os
import sys

files_in_our_folder = os.listdir()
file_name = input("Please provide the file name: ")

if file_name in files_in_our_folder:
    file_name_csv = "dst.csv"  
    all_products = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            all_products.append(row)

    user_command = input("Please provide a command (read / change and save / quit): ")
    if user_command == "read":
        for row in all_products:
            print(row)

    elif user_command == "change and save":
        change_command_column = int(input("Please provide a column for change: "))
        change_command_row = int(input("Please provide a row for change: "))

        if 1 <= change_command_column <= len(all_products[0]) and 1 <= change_command_row <= len(all_products):
            new_value = input("Provide the new value: ")
            all_products[change_command_row - 1][change_command_column - 1] = new_value

            with open(file_name_csv, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(all_products)

            print("Changes saved successfully.")
        else:
            print("Invalid row or column index. Change and save failed.")

    elif user_command == "quit":
        sys.exit(0)

    else:
        print("Invalid command")

else:
    print("The file does not exist. Files:", os.listdir())