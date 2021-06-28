from package import Package
from distance import get_shortest_path
import distance

packages_list = Package().hash_table
truck1_packages = []
truck2_packages = []
truck3_packages = []
truck1_depart_time = ['8:00:00']
truck2_depart_time = ['9:06:00']
truck3_depart_time = ['11:00:00']

for i in range(1, 41):
    if packages_list.get(i) is not None:
        if 'EOD' not in packages_list.get(i)[5]:
            if 'Must' in packages_list.get(i)[8] or 'None' in packages_list.get(i)[8]:
                packages_list.get(i)[9] = truck1_depart_time[0]
                truck1_packages.append(packages_list.get(i))
        if 'Can only be' in packages_list.get(i)[8] or 'Delayed' in packages_list.get(i)[8]:
            packages_list.get(i)[9] = truck2_depart_time[0]
            truck2_packages.append(packages_list.get(i))
        if packages_list.get(i) not in truck1_packages and packages_list.get(i) not in truck2_packages:
            if len(truck2_packages) < len(truck3_packages):
                packages_list.get(i)[9] = truck2_depart_time[0]
                truck2_packages.append(packages_list.get(i))
            else:
                packages_list.get(i)[9] = truck3_depart_time[0]
                truck3_packages.append(packages_list.get(i))

truck1_distances = []
truck2_distances = []
truck3_distances = []

counter = 0
# O(n^2), links truck list with list of addresses
for j in truck1_packages:
    for k in distance.get_address():
        if j[1] == k[2]:
            truck1_distances.append(int(k[0]))
            truck1_packages[counter][1] = k[0]
    counter += 1

counter = 0
# O(n^2), links truck list with list of addresses
for j in truck2_packages:
    for k in distance.get_address():
        if j[1] == k[2]:
            truck2_distances.append(int(k[0]))
            truck2_packages[counter][1] = k[0]
    counter += 1

counter = 0
# O(n^2), links truck list with list of addresses
for j in truck3_packages:
    for k in distance.get_address():
        if j[1] == k[2]:
            truck3_distances.append(k[0])
            truck3_packages[counter][1] = k[0]
    counter += 1

get_shortest_path(truck1_distances, 1, 0)
get_shortest_path(truck2_distances, 2, 0)
get_shortest_path(truck3_distances, 3, 0)


# O(1)
def get_all_packages():
    return packages_list


# O(1)
def get_truck1_packages():
    return truck1_packages


# O(1)
def get_truck2_packages():
    return truck2_packages


# O(1)
def get_truck3_packages():
    return truck3_packages
