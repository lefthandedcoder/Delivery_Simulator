import truck

print("Truck 1 Total: " + str(len(truck.truck1_packages)))
print("Truck 1 Packages: ")
for item in truck.truck1_packages:
    address = item[1] + ", " + item[2] + ", " + item[3]
    print("Package ID: " + str(item[0]) + " | Delivery Address: " + address + " | Zip Code: " + item[4] + " | Deadline: " + item[5] + " | Departure Time: " + str(item[9]))
print("Truck 2 Total: " + str(len(truck.truck2_packages)))
print("Truck 2 Packages: ")
for item in truck.truck2_packages:
    address = item[1] + ", " + item[2] + ", " + item[3]
    print("Package ID: " + str(item[0]) + " | Delivery Address: " + address + " | Zip Code: " + item[4] + " | Deadline: " + item[5] + " | Departure Time: " + str(item[9]))
print("Truck 3 Total: " + str(len(truck.truck3_packages)))
print("Truck 3 Packages: ")
for item in truck.truck3_packages:
    address = item[1] + ", " + item[2] + ", " + item[3]
    print("Package ID: " + str(item[0]) + " | Delivery Address: " + address + " | Zip Code: " + item[4] + " | Deadline: " + item[5] + " | Departure Time: " + str(item[9]))
