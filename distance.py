import csv
from hash_table import HashTable

with open('./csv_files/locations.csv') as addresses:
    read_addresses = csv.reader(addresses, delimiter=',')
    all_addresses = HashTable()
    # O(n) loops through all rows
    # The address_name and address_id will be used for determining optimal routes
    for row in read_addresses:
        key = row[2]
        address_id = row[0]
        address_name = row[1]
        address = row[2]
        value = [address_id, address_name, address]
        all_addresses.add(key, value)

with open('./csv_files/distances.csv') as distances:
    read_distances = csv.reader(distances, delimiter=',')
    all_distances = HashTable()
    # O(n^2) loops through all rows and then loops through all columns in each row
    # key is the starting position, second_key is the destination, and the row[column] value is the distance
    key = -1
    for row in read_distances:
        key += 1
        value = []
        second_key = -1
        for column in range(0, len(row)):
            second_key += 1
            if row[column] != '':
                value.append([second_key, row[column]])
            if row[column] == '':
                break
        all_distances.add(key, value)


def get_all_addresses():
    return all_addresses


def get_all_distances():
    return all_distances