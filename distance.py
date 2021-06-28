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

