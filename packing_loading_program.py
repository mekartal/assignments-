item_amount = int(input("Enter the number of items to be sent :"))
package_weight = 0
sent_packages = 0
total_sent_weight = 0
unused_capacity = 20 # Initialize it to the max package weight
max_unused_package = 0
max_unused_capacity = 0

for item in range(item_amount):
    item_weight = int(input(f"Enter the weight of package {item+1}: "))

    if item_weight < 1 or item_weight > 10:
        print("item must weight be between 1Kg to 10Kg")
        break

    if item_weight == 0:
        break

    if package_weight + item_weight > 20 : 
        sent_packages += 1
        unused_capacity = 20 - package_weight
        total_sent_weight += package_weight
        
        if unused_capacity > max_unused_capacity:
            max_unused_package = sent_packages
            max_unused_capacity = unused_capacity

        package_weight = item_weight
        unused_capacity = 20 - package_weight
    else:
        package_weight += item_weight
        unused_capacity = 20 - package_weight

sent_packages +=1 
total_sent_weight += package_weight

if 20 - package_weight > max_unused_capacity:
    max_unused_package = sent_packages
    max_unused_capacity = 20 - package_weight

print("\nPackage Summary:")
print("Number of packages sent:", sent_packages)
print("Total weight of packages sent:", total_sent_weight)
print("Total 'unused' capacity:", sent_packages * 20 - total_sent_weight)
print("Package with the most 'unused' capacity:", max_unused_package)
print("Amount of 'unused' capacity in that package:", max_unused_capacity)