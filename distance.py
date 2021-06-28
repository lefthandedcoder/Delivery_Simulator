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
        distance = read_distances[row][column]
    total += float(distance)
    return total


# Get distances O(n)
def get_current_distance(row, column):
    distance = read_distances[row][column]
    if distance == '':
        distance = read_distances[row][column]
    return float(distance)


# Get addresses O(n)
def get_address():
    return read_addresses


optimized_truck1 = []
optimized_truck2 = []
optimized_truck3 = []


def get_shortest_path(truck_distances, truck_number, current_location):
    if len(truck_distances) == 0:
        return truck_distances

    lowest_value = 30.0
    location = 0

    for i in truck_distances:
        value = int(i[1])
        if get_current_distance(current_location, value) <= lowest_value:
            lowest_value = get_current_distance(current_location, value)
            location = value

    for i in truck_distances:
        if get_current_distance(current_location, int(i[1])) == lowest_value:
            if truck_number == 1:
                optimized_truck1.append(i)
                optimized_truck1_indexes.append(i[1])
                truck_distances.pop(truck_distances.index(i))
                current_location = location
                get_shortest_path(truck_distances, 1, current_location)
            elif truck_number == 2:
                optimized_truck2.append(i)
                optimized_truck2_indexes.append(i[1])
                truck_distances.pop(truck_distances.index(i))
                current_location = location
                get_shortest_path(truck_distances, 2, current_location)
            elif truck_number == 3:
                optimized_truck3.append(i)
                optimized_truck3_indexes.append(i[1])
                truck_distances.pop(truck_distances.index(i))
                current_location = location
                get_shortest_path(truck_distances, 3, current_location)

    # Insert 0 for the first index of each index list
    optimized_truck1_indexes.insert(0, '0')
    optimized_truck2_indexes.insert(0, '0')
    optimized_truck3_indexes.insert(0, '0')
