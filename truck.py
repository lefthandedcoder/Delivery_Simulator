from package import get_truck1_packages
from package import get_truck2_packages
from package import get_truck3_packages
from distance import get_shortest_path
from distance import get_greedy_truck1_distances
from distance import get_greedy_truck2_distances
from distance import get_greedy_truck3_distances
import distance

truck1_packages = get_truck1_packages()
truck2_packages = get_truck2_packages()
truck3_packages = get_truck3_packages()
truck1_distances = []
truck2_distances = []
truck3_distances = []

counter = 0
# O(n^2), links truck list with list of addresses
for address in truck1_packages:
    for address_number in distance.get_address():
        if address[1] == address_number[2]:
            truck1_distances.append(address_number[0])
            truck1_packages[counter][1] = address_number[0]
    counter += 1

counter = 0
# O(n^2), links truck list with list of addresses
for address in truck2_packages:
    for address_number in distance.get_address():
        if address[1] == address_number[2]:
            truck2_distances.append(address_number[0])
            truck2_packages[counter][1] = address_number[0]
    counter += 1

counter = 0
# O(n^2), links truck list with list of addresses
for address in truck3_packages:
    for address_number in distance.get_address():
        if address[1] == address_number[2]:
            truck3_distances.append(address_number[0])
            truck3_packages[counter][1] = address_number[0]
    counter += 1

get_shortest_path(truck1_packages, 1, 0)
get_shortest_path(truck2_packages, 2, 0)
get_shortest_path(truck3_packages, 3, 0)


def get_truck1_distance():
    temp_distance = 0
    for i in range(len(get_greedy_truck1_distances())):
        try:
            temp_distance = distance.get_total_distance(int(get_greedy_truck1_distances()[i]),
                                                        int(get_greedy_truck1_distances()[i + 1]),
                                                        temp_distance)
        except IndexError:
            pass
    temp_distance += distance.distance_to_hub(
        (int(get_greedy_truck1_distances()[len(get_greedy_truck1_distances()) - 1])))
    return temp_distance


def get_truck2_distance():
    temp_distance = 0
    for i in range(len(get_greedy_truck2_distances())):
        try:
            temp_distance = distance.get_total_distance(int(get_greedy_truck2_distances()[i]),
                                                        int(get_greedy_truck2_distances()[i + 1]),
                                                        temp_distance)
        except IndexError:
            pass
    temp_distance += distance.distance_to_hub(
        (int(get_greedy_truck2_distances()[len(get_greedy_truck2_distances()) - 1])))
    return temp_distance


def get_truck3_distance():
    temp_distance = 0
    for i in range(len(get_greedy_truck3_distances())):
        try:
            temp_distance = distance.get_total_distance(int(get_greedy_truck3_distances()[i]),
                                                        int(get_greedy_truck3_distances()[i + 1]),
                                                        temp_distance)
        except IndexError:
            pass
    temp_distance += distance.distance_to_hub(
        (int(get_greedy_truck3_distances()[len(get_greedy_truck3_distances()) - 1])))
    return temp_distance


def get_distance_all_trucks():
    return float(get_truck1_distance() + get_truck2_distance() + get_truck3_distance())