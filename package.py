import csv
import datetime
from hash_table import HashTable

with open('./csv_files/packages.csv') as packages:
    read_packages = csv.reader(packages, delimiter=',')
    all_packages = HashTable()
    total_packages = 0

    # Go through all rows in O(n)
    for row in read_packages:
        total_packages += 1
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
        status = 'At hub'
        note = row[7]
        departure_time = datetime.timedelta(hours=8, minutes=0, seconds=0)
        delivered_time = datetime.timedelta(hours=17, minutes=0, seconds=0)
        on_time = ''
        value = [id, address, city, state, zip, deadline, weight, status, note, departure_time, delivered_time, on_time]
        all_packages.add(key, value)


def get_total_packages():
    return total_packages


def get_all_packages():
    return all_packages
