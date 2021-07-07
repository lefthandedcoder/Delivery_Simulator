import csv
from hash_table import HashTable

with open('./csv_files/locations.csv') as addresses:
    read_addresses = csv.reader(addresses, delimiter=',')
    # Creates new hash table to store locations
    all_addresses = HashTable()
    # Loops through all rows in locations file and stores values in a hash table, O(n)
    # The address_name and address_id will be used for determining optimal routes, note that the key is a string
    for row in read_addresses:
        key = row[2]
        address_id = row[0]
        address_name = row[1]
        address = row[2]
        value = [address_id, address_name, address]
        all_addresses.add(key, value)

with open('./csv_files/distances.csv') as distances:
    read_distances = csv.reader(distances, delimiter=',')
    # Creates new hash table to store distances as [current_location [destination, distance]]
    all_distances = HashTable()
    # O(n^2) loops through all rows O(n) and then loops through all columns in each row O(n) -> O(n) * O(n)
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
                # Disregards null strings, to address this, the subsequent function tries the current setup,
                # and, if error, flips the current_location and destination
                break
        all_distances.add(key, value)


# Gets the hash table of addresses, O(1)
def get_all_addresses():
    return all_addresses


# Gets the hash table of distances, O(1)
def get_all_distances():
    return all_distances