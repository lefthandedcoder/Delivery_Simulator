import csv
from hash_table import HashTable
from enum import Enum


class Status(Enum):
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


with open('./csv_files/packages.csv') as packages:
    read_file = csv.reader(packages, delimiter=',')

    truck1_packages = []
    truck2_packages = []
    truck3_packages = []
    test_packages = []
    truck1_depart_time = ['8:00:00']
    truck2_depart_time = ['9:06:00']
    truck3_depart_time = ['11:01:00']
    all_packages = HashTable()

    # Go through all rows in O(n)
    for row in read_file:
        if 'Wrong' in row[7]:
            row[1] = "410 S State St"
            row[4] = "84111"
            row[7] = "Address updated at 10:20 am"
        key = int(row[0])
        id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        status = 1
        note = row[7]
        departure_time = '08:00:00'
        delivered_time = '01:00:00'
        value = [id, address, city, state, zip, deadline, weight, status, note, departure_time, delivered_time]
        if 'EOD' not in value[5]:
            if 'Must' in value[8] or 'None' in value[8]:
                value[9] = truck1_depart_time[0]
                truck1_packages.append(value)
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            value[9] = truck2_depart_time[0]
            truck2_packages.append(value)
        if value not in truck1_packages and value not in truck2_packages:
            if len(truck2_packages) < len(truck3_packages):
                value[9] = truck2_depart_time[0]
                truck2_packages.append(value)
            else:
                value[9] = truck3_depart_time[0]
                truck3_packages.append(value)

        all_packages.add(key, value)


def get_all_packages():
    return all_packages


def get_truck1_packages():
    return truck1_packages


def get_truck2_packages():
    return truck2_packages


def get_truck3_packages():
    return truck3_packages

