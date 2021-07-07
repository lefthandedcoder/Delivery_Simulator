import distance
import package
import datetime


# Creates a class 'truck' with values to be added based on function returns
class Truck:
    def __init__(self):
        self.depart_time = []
        self.status = 'At hub'
        self.package_list = []
        self.route = []
        self.optimized_route = []
        self.current_distance = 0
        self.total_distance = 0
        self.distance_list = []
        self.time = 0  # Will track based on speed and distance and add from departure time
        self.current_location = 0


truck1 = Truck()
truck2 = Truck()
truck3 = Truck()
truck1.depart_time = datetime.timedelta(hours=8, minutes=0, seconds=0)
truck2.depart_time = datetime.timedelta(hours=9, minutes=5, seconds=0)
truck3.depart_time = datetime.timedelta(hours=10, minutes=30, seconds=0)


# Gets Truck 1 with above depart_time added, O(1)
def get_truck1():
    return truck1


# Gets Truck 2 with above depart_time added, O(1)
def get_truck2():
    return truck2


# Gets Truck 3 with above depart_time added, O(1)
def get_truck3():
    return truck3


# Loads trucks, O(n)
def load_trucks():
    # Loops through all packages and sorts into different trucks based on constraints, O(n)
    for item in range(1, (package.get_total_packages() + 1)):
        value = package.get_all_packages().get(int(item))
        if 'EOD' not in value[5]:
            if 'Must' in value[8] or 'None' in value[8]:
                value[9] = truck1.depart_time
                value[12] = 1
                truck1.package_list.append(value)
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            value[9] = truck2.depart_time
            value[12] = 2
            truck2.package_list.append(value)
        if 'Address updated' in value[8]:
            value[9] = truck3.depart_time
            value[12] = 3
            truck3.package_list.append(value)
        if value not in truck1.package_list and value not in truck2.package_list:
            if len(truck2.package_list) < len(truck3.package_list):
                value[9] = truck2.depart_time
                value[12] = 2
                truck2.package_list.append(value)
            else:
                value[9] = truck3.depart_time
                value[12] = 3
                truck3.package_list.append(value)


# Loops through given package list and appends ID values to a route list, O(n)
def get_route(package_list, route):
    for route_packages in package_list:
        route_address = route_packages[1]
        route_address_id = distance.get_all_addresses().get(str(route_address))[0]
        route.append([route_packages[0], route_address_id])


# This is the main algorithm for completing this project. I use a greedy
# algorithm to optimize the given route list to find the shortest path
# that traverses all package destinations for the given package list. I
# use this algorithm because it recursively finds the next best destination
# based on the current location. Once the next best destination is found
# the function fires again with the previous value for the current location
# replaced with the current best destination. The algorithm has a space-time
# complexity of O(n^2) because it has a nested for loop. The first for loop
# finds the shortest distance from the starting location (the hub) to whichever
# destination in the list of packages (the route of package IDs and distances)
# has the lowest distance. Once found, the dummy lowest_distance value is
# replaced with the closest distance, and the location of the closest distance
# becomes the new starting location. The best case scenario is that the first
# distance in the route list is the closest O(1). The worst case scenario is
# that the last distance in the route list is the closest O(n).
#
# The second loop proceeds once the lowest_value is found. This loop repeats
# what happens in the first loop but does so for each subsequent distance until
# the list is optimized and the shortest path is found and the route list is empty.
# Once this happens, the function will exit and an optimized_route list will be ready
# for getting total distance values and total times for the trucks.
#
# This algorithm takes three parameters, the initial list of unsorted distances, the
# list for appending sorted distances, and the starting location (the hub, '0').
#
# This algorithm has a space-time complexity of O(n^2)

def get_shortest_path(route, optimized_route, start):
    if len(route) == 0:
        return route

    lowest_distance = 999.9
    location = 0

    for destination in route:
        next_stop = int(destination[1])
        try:
            temp_distance = distance.get_all_distances().get(start)[next_stop][1]
        except IndexError:
            temp_distance = distance.get_all_distances().get(next_stop)[start][1]
            pass
        if float(temp_distance) <= float(lowest_distance):
            lowest_distance = temp_distance
            location = next_stop

    for destination in route:
        next_stop = int(destination[1])
        try:
            temp_distance = distance.get_all_distances().get(start)[next_stop][1]
        except IndexError:
            temp_distance = distance.get_all_distances().get(next_stop)[start][1]
            pass
        if float(temp_distance) == float(lowest_distance):
            route.remove(destination)
            optimized_route.append(destination)
            current_location = location
            get_shortest_path(route, optimized_route, current_location)


# This function takes the optimized route from the above function and appends a list of package IDs and distances
# at their destinations, O(n)
def get_distance(optimized_route, distance_list):
    last_temp = 0
    new_temp = 0
    # Adds starting position (at hub)
    optimized_route.insert(0, [0, '0'])
    # Adds value for return trip to hub from last delivery destination
    optimized_route.append([0, '0'])
    for index in range(0, len(optimized_route)):
        try:
            start = optimized_route[index][1]
            end = optimized_route[index + 1][1]
            try:
                new_temp += float(distance.get_all_distances().get(int(start))[int(end)][1])
                distance_list.append([optimized_route[index][0], last_temp])
                last_temp = new_temp
            except IndexError:
                new_temp += float(distance.get_all_distances().get(int(end))[int(start)][1])
                distance_list.append([optimized_route[index][0], last_temp])
                last_temp = new_temp
                pass
        except IndexError:
            pass
    distance_list.append([0, last_temp])
    return last_temp


# Gets timedelta values for specific distance/time values or total distance/time, O(1)
def get_time(depart_time, current_distance):
    new_time = current_distance / 18  # minutes per mile
    time_hour_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60)) + ':00'
    (hrs, mins, secs) = time_hour_minutes.split(':')
    add_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
    current_time = depart_time + add_time
    return current_time


# Gets final values for distances and delivery times and updates package values in the package list, O(n^2)
def get_delivered_list(distance_list, depart_time, package_list):
    # Loops through list of package IDs and distances and updates delivery times, O(n)
    for obj in range(0, (len(distance_list) - 1)):
        deliver_time = get_time(depart_time, distance_list[(obj + 1)][1])
        list_id = distance_list[(obj + 1)][0]
        # Loops through packages in package list and as delivered and either on time or delayed
        for item in range(0, len(package_list)):
            package_id = package_list[item][0]
            if list_id == package_id:
                package_list[item][10] = deliver_time
                package_list[item][7] = 'Delivered'
                deadline = package_list[item][5]
                if deadline == 'EOD':
                    deadline = '17:00:00'
                elif deadline == '10:30 AM':
                    deadline = '10:30:00'
                elif deadline == '9:00 AM':
                    deadline = '09:00:00'
                (hrs, mins, secs) = deadline.split(':')
                deadline_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                if deliver_time <= deadline_time:
                    package_list[item][11] = 'On time'
                else:
                    package_list[item][11] = 'Delayed'


def get_status():
    try:
        # Gets a time for reviewing package deliveries, O(1)
        user_time = input('Enter a time (HH:MM:SS) after 8:00:00. \n'
                          'For example, 9 AM is 9:00:00, and 1 PM is 13:00:00. \n'
                          'Time: ')
        (hrs, mins, secs) = user_time.split(':')
        delta_user = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        # Notifies user of known address change if it has occurred before the selected time, O(1)
        swap_time = '10:20:00'
        (hrs, mins, secs) = swap_time.split(':')
        swap_delta = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        if delta_user >= swap_delta:
            print('Address changed for package 9! New address is: ' + package.get_all_packages().get(9)[1] + '\n')
        print('The time is ' + str(delta_user) + '\n')
        truck1_return = get_time(truck1.depart_time, truck1.total_distance)
        truck2_return = get_time(truck2.depart_time, truck2.total_distance)
        truck3_return = get_time(truck3.depart_time, truck3.total_distance)
        user_time_truck1 = delta_user - datetime.timedelta(hours=8, minutes=0, seconds=0)
        convert_distance_truck1 = float(user_time_truck1.total_seconds() / 3600) * 18
        user_time_truck2 = delta_user - datetime.timedelta(hours=9, minutes=5, seconds=0)
        convert_distance_truck2 = float(user_time_truck2.total_seconds() / 3600) * 18
        user_time_truck3 = delta_user - datetime.timedelta(hours=10, minutes=30, seconds=0)
        convert_distance_truck3 = float(user_time_truck3.total_seconds() / 3600) * 18
        # Checks if trucks have completed their deliveries and returned to the hub. If yes, return time and
        # total miles are printed. If not, it prints that the truck has not finished yet.
        if delta_user >= truck1_return:
            print('Truck 1 has finished its route and returned to the hub at ' + str(truck1_return) + '.')
            print('Total distance traveled is ' + str(round(truck1.total_distance)) + ' miles.')
        else:
            print('Truck 1 has not finished its route. Distance traveled is '
                  + str(round(convert_distance_truck1)) + ' miles.')
        if delta_user >= truck2_return:
            print('Truck 2 has finished its route and returned to the hub at ' + str(truck2_return) + '.')
            print('Total distance traveled is ' + str(round(truck2.total_distance)) + ' miles.')
        elif delta_user >= datetime.timedelta(hours=9, minutes=5, seconds=0):
            print('Truck 2 has not finished its route. Distance traveled is '
                  + str(round(convert_distance_truck2)) + ' miles.')
        else:
            print('Truck 2 has not begun its route. Check back later.')
        if delta_user >= truck3_return:
            print('Truck 3 has finished its route and returned to the hub at ' + str(truck3_return) + '.')
            print('Total distance traveled is ' + str(round(truck3.total_distance)) + ' miles.')
        elif delta_user >= datetime.timedelta(hours=10, minutes=30, seconds=0):
            print('Truck 3 has not finished its route. Distance traveled is '
                  + str(round(convert_distance_truck3)) + ' miles.\n')
        else:
            print('Truck 3 has not begun its route. Check back later.\n')
        if delta_user >= truck1_return and delta_user >= truck2_return and delta_user >= truck3_return:
            print('The total distance of all trucks traveled is '
                  + str(round(truck1.total_distance + truck2.total_distance + truck3.total_distance)) + ' miles.\n')
        # Asks user to select either info for a specific package, all packages, a new time, or to exit the program
        get_menu(delta_user)
    except ValueError:
        # If a wrong time format or a string or something other than the requested input is given, this catches
        # the error and exits the program.
        print('Invalid entry! Goodbye!')
        print('The total distance of all trucks traveled is '
              + str(round(truck1.total_distance + truck2.total_distance + truck3.total_distance)) + ' miles.\n')
        exit()


def get_menu(delta_user):
    # See description above
    menu_selection = input('\nSelect from the following: \n'
                           '1: Look Up Package ID \n'
                           '2: Print All Packages \n'
                           '3: Select New Time \n'
                           'Exit: End Program \n'
                           'Enter Option: ')
    if menu_selection == '1':
        # Requests a package ID integer value. If a string or something else is given, it catches the error and exits.
        package_id = int(input('Enter a Package ID: '))
        try:
            # Since the user has given a specific ID number, this function only checks if the ID
            # is in the hash table, O(n)
            if package_id in range(1, (package.get_total_packages() + 1)):
                item = package_id
                # If the ID is in the hash table, this then loops through all 3 package lists to find where
                # the package is. This will then help retrieve delivery info, O(n) + O(n) + O(n)
                for obj in range(0, len(truck1.package_list)):
                    if package.get_all_packages().get(int(item))[0] == truck1.package_list[obj][0]:
                        package.get_all_packages().get(int(item))[9] = truck1.package_list[obj][9]
                        package.get_all_packages().get(int(item))[10] = truck1.package_list[obj][10]
                        package.get_all_packages().get(int(item))[11] = truck1.package_list[obj][11]
                for obj in range(0, len(truck2.package_list)):
                    if package.get_all_packages().get(int(item))[0] == truck2.package_list[obj][0]:
                        package.get_all_packages().get(int(item))[9] = truck2.package_list[obj][9]
                        package.get_all_packages().get(int(item))[10] = truck2.package_list[obj][10]
                        package.get_all_packages().get(int(item))[11] = truck1.package_list[obj][11]
                for obj in range(0, len(truck3.package_list)):
                    if package.get_all_packages().get(int(item))[0] == truck3.package_list[obj][0]:
                        package.get_all_packages().get(int(item))[9] = truck3.package_list[obj][9]
                        package.get_all_packages().get(int(item))[10] = truck3.package_list[obj][10]
                        package.get_all_packages().get(int(item))[11] = truck1.package_list[obj][11]
                depart_time = package.get_all_packages().get(int(item))[9]
                deliver_time = package.get_all_packages().get(int(item))[10]
                # Compares truck departure times against the user's selected time and prints based on results
                # for selected package.
                if depart_time > delta_user:
                    if 'Delayed' in package.get_all_packages().get(int(item))[8]:
                        package.get_all_packages().get(int(item))[7] = 'Package delayed on flight'
                    elif 'Delayed' in package.get_all_packages().get(int(item))[8]:
                        package.get_all_packages().get(int(item))[7] = 'Package delayed on flight'
                    elif 'Address' in package.get_all_packages().get(int(item))[8]:
                        package.get_all_packages().get(int(item))[7] = 'Waiting for new address'
                    else:
                        package.get_all_packages().get(int(item))[7] = 'At hub'

                    print('Package ID: ' + str(package.get_all_packages().get(int(item))[0])
                          + ' Address: ' + str(package.get_all_packages().get(int(item))[1])
                          + ', ' + str(package.get_all_packages().get(int(item))[2]
                                       + ', ' + str(package.get_all_packages().get(int(item))[3]))
                          + ' Zip: ' + str(package.get_all_packages().get(int(item))[4])
                          + ' Weight: ' + str(package.get_all_packages().get(int(item))[6]) + ' kg'
                          + ' Deadline: ' + str(package.get_all_packages().get(int(item))[5])
                          + ' Status: ' + str(package.get_all_packages().get(int(item))[7])
                          + ' Leaving at: ' + str(package.get_all_packages().get(int(item))[9]))
                elif depart_time < delta_user:
                    if deliver_time <= delta_user:
                        package.get_all_packages().get(int(item))[7] = 'Delivered by Truck ' + str(
                            package.get_all_packages().get(int(item))[12])

                        print('Package ID: ' + str(package.get_all_packages().get(int(item))[0])
                              + ' Address: ' + str(package.get_all_packages().get(int(item))[1])
                              + ', ' + str(package.get_all_packages().get(int(item))[2]
                                           + ', ' + str(package.get_all_packages().get(int(item))[3]))
                              + ' Zip: ' + str(package.get_all_packages().get(int(item))[4])
                              + ' Weight: ' + str(package.get_all_packages().get(int(item))[6]) + ' kg'
                              + ' Deadline: ' + str(package.get_all_packages().get(int(item))[5])
                              + ' Status: ' + str(package.get_all_packages().get(int(item))[7])
                              + ' Left at: ' + str(package.get_all_packages().get(int(item))[9])
                              + ' Arrived at: ' + str(package.get_all_packages().get(int(item))[10])
                              + ' On Time?: ' + str(package.get_all_packages().get(int(item))[11]))
                    else:
                        package.get_all_packages().get(int(item))[7] = 'En route on Truck ' + str(
                            package.get_all_packages().get(int(item))[12])

                        print('Package ID: ' + str(package.get_all_packages().get(int(item))[0])
                              + ' Address: ' + str(package.get_all_packages().get(int(item))[1])
                              + ', ' + str(package.get_all_packages().get(int(item))[2]
                                           + ', ' + str(package.get_all_packages().get(int(item))[3]))
                              + ' Zip: ' + str(package.get_all_packages().get(int(item))[4])
                              + ' Weight: ' + str(package.get_all_packages().get(int(item))[6]) + ' kg'
                              + ' Deadline: ' + str(package.get_all_packages().get(int(item))[5])
                              + ' Status: ' + str(package.get_all_packages().get(int(item))[7])
                              + ' Left at: ' + str(package.get_all_packages().get(int(item))[9]))
            else:
                # If the package ID integer is not in the hash table, this result is given.
                print('Package ID not found!')
                print('The total distance of all trucks traveled is '
                      + str(round(truck1.total_distance + truck2.total_distance + truck3.total_distance)) + ' miles.\n')
                exit()
        except ValueError:
            # This catches if an integer is not given and exits the program.
            print('Invalid entry!')
            print('The total distance of all trucks traveled is '
                  + str(round(truck1.total_distance + truck2.total_distance + truck3.total_distance)) + ' miles.\n')
            exit()
        # This asks if the user wants to try a new time and restart the query.
        continue_input = int(input('\nThe time is ' + str(delta_user)
                                   + '. \nContinue? (Type 1 or 2) \n'
                                     '1 : Continue Program \n'
                                     '2 : Exit Program \n'))
        if continue_input == 1:
            # Restarts the function
            get_menu()
        else:
            print('Thank you for using the WGUPS Delivery Simulator. Goodbye!')
            print('The total distance of all trucks traveled is '
                  + str(round(truck1.total_distance + truck2.total_distance + truck3.total_distance)) + ' miles.\n')
            exit()
    if menu_selection == '2':
        try:
            print('The time is ' + str(delta_user) + '.\n')
            # Goes through all packages in the hash table and updates and prints associated data, O(n)
            for item in range(1, (package.get_total_packages() + 1)):
                # Goes through all packages in the three package lists and finds matches and updates values, O(n)
                for obj in range(0, 15):
                    try:
                        if package.get_all_packages().get(int(item))[0] == truck1.package_list[obj][0]:
                            package.get_all_packages().get(int(item))[9] = truck1.package_list[obj][9]
                            package.get_all_packages().get(int(item))[10] = truck1.package_list[obj][10]
                            package.get_all_packages().get(int(item))[11] = truck1.package_list[obj][11]
                    except IndexError:
                        pass
                for obj in range(0, 15):
                    try:
                        if package.get_all_packages().get(int(item))[0] == truck2.package_list[obj][0]:
                            package.get_all_packages().get(int(item))[9] = truck2.package_list[obj][9]
                            package.get_all_packages().get(int(item))[10] = truck2.package_list[obj][10]
                            package.get_all_packages().get(int(item))[11] = truck1.package_list[obj][11]
                    except IndexError:
                        pass
                for obj in range(0, 15):
                    try:
                        if package.get_all_packages().get(int(item))[0] == truck3.package_list[obj][0]:
                            package.get_all_packages().get(int(item))[9] = truck3.package_list[obj][9]
                            package.get_all_packages().get(int(item))[10] = truck3.package_list[obj][10]
                            package.get_all_packages().get(int(item))[11] = truck1.package_list[obj][11]
                    except IndexError:
                        pass
                depart_time = package.get_all_packages().get(int(item))[9]
                deliver_time = package.get_all_packages().get(int(item))[10]
                # Compares results based on user's selected time. Updates and prints based on comparison.
                if depart_time > delta_user:
                    if 'Delayed' in package.get_all_packages().get(int(item))[8]:
                        package.get_all_packages().get(int(item))[7] = 'Package delayed on flight'
                    elif 'Delayed' in package.get_all_packages().get(int(item))[8]:
                        package.get_all_packages().get(int(item))[7] = 'Package delayed on flight'
                    elif 'Address' in package.get_all_packages().get(int(item))[8]:
                        package.get_all_packages().get(int(item))[7] = 'Waiting for new address'
                    else:
                        package.get_all_packages().get(int(item))[7] = 'At hub'

                    print('Package ID: ' + str(package.get_all_packages().get(int(item))[0])
                          + ' Address: ' + str(package.get_all_packages().get(int(item))[1])
                          + ', ' + str(package.get_all_packages().get(int(item))[2]
                                       + ', ' + str(package.get_all_packages().get(int(item))[3]))
                          + ' Zip: ' + str(package.get_all_packages().get(int(item))[4])
                          + ' Weight: ' + str(package.get_all_packages().get(int(item))[6]) + ' kg'
                          + ' Deadline: ' + str(package.get_all_packages().get(int(item))[5])
                          + ' Status: ' + str(package.get_all_packages().get(int(item))[7])
                          + ' Leaving at: ' + str(package.get_all_packages().get(int(item))[9]))
                elif depart_time < delta_user:
                    if deliver_time <= delta_user:
                        package.get_all_packages().get(int(item))[7] = 'Delivered by Truck ' + str(
                            package.get_all_packages().get(int(item))[12])

                        print('Package ID: ' + str(package.get_all_packages().get(int(item))[0])
                              + ' Address: ' + str(package.get_all_packages().get(int(item))[1])
                              + ', ' + str(package.get_all_packages().get(int(item))[2]
                                           + ', ' + str(package.get_all_packages().get(int(item))[3]))
                              + ' Zip: ' + str(package.get_all_packages().get(int(item))[4])
                              + ' Weight: ' + str(package.get_all_packages().get(int(item))[6]) + ' kg'
                              + ' Deadline: ' + str(package.get_all_packages().get(int(item))[5])
                              + ' Status: ' + str(package.get_all_packages().get(int(item))[7])
                              + ' Left at: ' + str(package.get_all_packages().get(int(item))[9])
                              + ' Arrived at: ' + str(package.get_all_packages().get(int(item))[10])
                              + ' On Time?: ' + str(package.get_all_packages().get(int(item))[11]))
                    else:
                        package.get_all_packages().get(int(item))[7] = 'En route on Truck ' + str(
                            package.get_all_packages().get(int(item))[12])

                        print('Package ID: ' + str(package.get_all_packages().get(int(item))[0])
                              + ' Address: ' + str(package.get_all_packages().get(int(item))[1])
                              + ', ' + str(package.get_all_packages().get(int(item))[2]
                                           + ', ' + str(package.get_all_packages().get(int(item))[3]))
                              + ' Zip: ' + str(package.get_all_packages().get(int(item))[4])
                              + ' Weight: ' + str(package.get_all_packages().get(int(item))[6]) + ' kg'
                              + ' Deadline: ' + str(package.get_all_packages().get(int(item))[5])
                              + ' Status: ' + str(package.get_all_packages().get(int(item))[7])
                              + ' Left at: ' + str(package.get_all_packages().get(int(item))[9]))
        except IndexError:
            pass
        continue_input = int(input('\nThe time is ' + str(delta_user)
                                   + '. \nContinue? (Type 1 or 2) \n'
                                   '1 : Continue Program \n'
                                   '2 : Exit Program \n'))
        if continue_input == 1:
            get_menu(delta_user)
        else:
            print('Thank you for using the WGUPS Delivery Simulator. Goodbye!')
            print('The total distance of all trucks traveled is '
                  + str(round(truck1.total_distance + truck2.total_distance + truck3.total_distance)) + ' miles.\n')
            exit()
    if menu_selection == '3':
        # Restarts the function
        get_status()
    if menu_selection == 'Exit':
        # Exits the program
        print('Thank you for using the WGUPS Delivery Simulator. Goodbye!')
        print('The total distance of all trucks traveled is '
              + str(round(truck1.total_distance + truck2.total_distance + truck3.total_distance)) + ' miles.\n')
        exit()
