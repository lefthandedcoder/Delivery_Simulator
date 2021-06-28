import csv
from hash_table import HashTable
from enum import Enum


class Status(Enum):
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


class Package:
    hash_table = HashTable()

    def __init__(self):
        with open('./csv_files/packages.csv') as packages:
            read_file = csv.reader(packages, delimiter=',')
            # Go through all rows in O(n)
            for row in read_file:
                if 'Wrong' in row[7]:
                    row[1] = "410 S State St."
                    row[4] = "84111"
                    row[7] = "Address updated at 10:20 am"
                key = int(row[0])
                id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip = row[4]
                weight = row[5]
                deadline = row[6]
                status = 1
                note = row[7]
                departure_time = '08:00:00'
                delivered_time = '01:00:00'
                Package.hash_table.add(key, [id,
                                             address,
                                             city,
                                             state,
                                             zip,
                                             weight,
                                             deadline,
                                             status,
                                             note,
                                             departure_time,
                                             delivered_time])
