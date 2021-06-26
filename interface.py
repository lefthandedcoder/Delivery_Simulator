from package import Package

packages = Package().hash_table
j = 0
k = 0
for i in range(1,41):
    if 'EOD' not in packages.get(i)[4]:
        if 'Must' in packages.get(i)[7] or 'None' in packages.get(i)[7]:
            package_id = str(i)
            j += 1
            print('Package ID: ' + package_id)
print('Total packages in Truck 1: ' + str(j))
for i in range(1, 41):
    if 'Can only be' in packages.get(i)[7] or 'Delayed' in packages.get(i)[7]:
        package_id = str(i)
        k += 1
        print('Package ID: ' + package_id)
print('Total packages in Truck 2: ' + str(k))
print('Packages remaining: ' + str(40 - (j + k)))