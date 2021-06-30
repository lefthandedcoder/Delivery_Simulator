import csv
import datetime

# Read CSV files
with open('./csv_files/distances.csv') as distances:
    read_distances = list(csv.reader(distances, delimiter=','))
with open('./csv_files/locations.csv') as addresses:
    read_addresses = list(csv.reader(addresses, delimiter=','))


# Get distances O(n)
def get_total_distance(row, column, total):
    distance = read_distances[row][column]
    if distance == '':
        distance = read_distances[column][row]
    total += float(distance)
    return total


# Get distances O(n)
def get_current_distance(row, column):
    distance = read_distances[row][column]
    if distance == '':
        distance = read_distances[column][row]
    return float(distance)


# Get addresses O(n)
def get_address():
    return read_addresses


greedy_truck1_list = []
greedy_truck2_list = []
greedy_truck3_list = []
greedy_truck1_distances = []
greedy_truck2_distances = []
greedy_truck3_distances = []


def get_shortest_path(truck_distances, truck_number, current_location):
    if len(truck_distances) == 0:
        return truck_distances

    lowest_value = 200.0
    location = 0

    # O(n)
    for i in truck_distances:
        value = int(i[1])
        if get_current_distance(current_location, value) <= lowest_value:
            lowest_value = get_current_distance(current_location, value)
            location = value

    # O(n^2)
    for i in truck_distances:
        if get_current_distance(current_location, int(i[1])) == lowest_value:
            if truck_number == 1:
                greedy_truck1_list.append(i)
                greedy_truck1_distances.append(i[1])
                truck_distances.pop(truck_distances.index(i))
                current_location = location
                # O(n)
                get_shortest_path(truck_distances, 1, current_location)
            elif truck_number == 2:
                greedy_truck2_list.append(i)
                greedy_truck2_distances.append(i[1])
                truck_distances.pop(truck_distances.index(i))
                current_location = location
                # O(n)
                get_shortest_path(truck_distances, 2, current_location)
            elif truck_number == 3:
                greedy_truck3_list.append(i)
                greedy_truck3_distances.append(i[1])
                truck_distances.pop(truck_distances.index(i))
                current_location = location
                # O(n)
                get_shortest_path(truck_distances, 3, current_location)


def distance_to_hub(current_location):
    return float(read_distances[int(current_location)][0])


# Insert 0 for the first index of each index list
greedy_truck1_distances.insert(0, '0')
greedy_truck2_distances.insert(0, '0')
greedy_truck3_distances.insert(0, '0')


def get_greedy_truck1_list():
    return greedy_truck1_list


def get_greedy_truck2_list():
    return greedy_truck2_list


def get_greedy_truck3():
    return greedy_truck3_list


def get_greedy_truck1_distances():
    return greedy_truck1_distances


def get_greedy_truck2_distances():
    return greedy_truck2_distances


def get_greedy_truck3_distances():
    return greedy_truck3_distances
