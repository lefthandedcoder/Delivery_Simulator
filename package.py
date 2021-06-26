import csv
from hash_table import HashMap
from enum import Enum
import datetime


class Status(Enum):
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


class Package:
    hash_table = HashMap()

    def __init__(self):
        with open('./csv_files/packages.csv') as packages:
            read_file = csv.reader(packages, delimiter=',')

            for row in read_file:
                id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip = row[4]
                weight = row[5]
                deadline = row[6]
                status = 1
                note = row[7]
                departure_time = '08:00'
                delivered_time = '01:00'
                Package.hash_table.add(id, [address, city, state, zip, weight, deadline, status, note, departure_time, delivered_time])
