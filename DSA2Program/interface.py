from hash import hashFunc
from package import packageObject
from truck import truckObject
import package
from dataclasses import fields
from time import sleep
import colors
import datetime

#### Class big O  = O(n)


#### big O = O(1)
# start of program. initalized in main at at line 18 in main.py
def prompt():
    # prompt for program start
    print(colors.CRED + "\nWelcome to the WGU Truck Routing Program." + colors.CEND)
    sleep(1)
    print(colors.CRED + "This program is a python implementation of the traveling salesman problem." + colors.CEND)
    sleep(1)

#### big O = O(1)
# output for notification of truck loading
# tnum = number of truck
def loadingTruckInterface(tnum):
    sleep(1)
    # uses variable called from loading truck method
    print(colors.CPURPLE + "\n\nLoading truck " + str(tnum) + "..." + colors.CEND)
    sleep(1)

#### Big o = O(n)
# output for total mileage of route
def output(t1, t2, t3, hashTable, t1PackagesDepartTime, t2PackagesDepartTime, t3PackagesDepartTime):
   # textual output for total mileage
    print(colors.CRED + "\nThe total mileage for this route is..." + colors.CEND)
    # sleep command for easier reading
    sleep(2)
    # prints total distance (truck distance + distance from last package back to hub) for each truck
    print(colors.CUL + colors.CGREEN + str(t1.distanceTraveled + t1.distanceLastPackageToHub + t2.distanceTraveled + t2.distanceLastPackageToHub + t3.distanceTraveled + t3.distanceLastPackageToHub)+ colors.CEND + "\n") # add truck 1 2 and 3 mileage here.
    # flag to indicate which command we will run
    x = 0
    # while x is not 1,2,3,or 4 then repeat the question. This is not looping through data and is being used as input validation so I did not calculate time complexity 
    while(x != 1 and x != 2 and x != 3 and x != 4): 
        # textual output to ask what to do
        print("What would you like to do?")
        print("1. Print all packages and delivered times?")
        print("2. Get single packages status with a timestamp?")
        print("3. Get all packages status with a time stamp?")
        print("4. Exit Program")
        # assigns the input as an int to our flag, x
        x = int(input("Enter 1, 2, 3, or 4\n"))

    # if x is 1, print all packages at end of route runs
    if (x == 1):
        # textual output for truck 1
        print(colors.CRED + "Packages on Truck 1" + colors.CEND)
        # for each package on truck 1, lookup package based on package ID and print the attributes
        for i in t1.packages:
            # lookup function defined in hash.py
            p = hashTable.lookup(i)
            #textual outputs for each package on truck
            print(colors.CPURPLE + "ID:" + str(p.ID) + colors.CEND)
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            print("Delivered Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            # at end of day, all packages are delivered. So the status will only be "delivered"
            print("Status: Delivered\n")
            # print truck 1 total distance
        print("Truck 1 Distance after getting back to Hub: " + str(t1.distanceLastPackageToHub + t1.distanceTraveled))
        # print the time the truck returned to hub. truck 1 needs to be back by 10:30 so the driver can drive truck 3
        print("Time returned to Hub: " + str(t1.timeLastPackageToHub) + "\n\n")
        # textual output for truck 2
        print(colors.CRED + "Packages on Truck 2" + colors.CEND)
        # # for each package on truck 2, lookup package based on package ID and print the attributes
        for i in t2.packages:
            # lookup defined in hash.py
            p = hashTable.lookup(i)
            # textual outputs for each package on truck
            print(colors.CPURPLE + "ID:" + str(p.ID) + colors.CEND)
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            print("Delivered Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: Delivered\n")
            # print total distance after truck returns to hub
        print("Truck 2 Distance after getting back to Hub: " + str(t2.distanceLastPackageToHub + t2.distanceTraveled))
            # print final time after truck returns to hub 
        print("Time returned to Hub: " + str(t2.timeLastPackageToHub) + "\n")
        # textual output for truck 3
        print(colors.CRED + "Packages on Truck 3" + colors.CEND)
        # for each package in truck 3, lookup package based on ID and print
        for i in t3.packages:
            # lookup function defined in hash.py
            p = hashTable.lookup(i)
            # textual output for each package on truck
            print(colors.CPURPLE + "ID:" + str(p.ID) + colors.CEND)
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            print("Delivered Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: Delivered\n")
            # final distance for truck 3
        print("Truck 3 Distance after getting back to Hub: " + str(t3.distanceLastPackageToHub + t3.distanceTraveled))
            # time truck 3 returns to hub
        print("Time returned to Hub: " + str(t3.timeLastPackageToHub) + "\n")



    # if x is 2, allow user to search for a certian package's status at a certain time stamp
    elif (x == 2):
        # valid is a bool we wil use to loop through this while loop until a valid input is given
        valid = False 
        # keep running loop until there is a valid input. this is being used as input validation so I did not calculate time complexity
        while valid == False:
            # try catch to handle the condition of A. proper input and B. improper input
            try:
                #time_input stores the variable of the user input
                time_input = input("What time would you like to search? Please use format: HH:MM:SS\n")
                # we use this to validate the format of the input
                datetime.time.fromisoformat(time_input)
                # if valid, valid is true and the while loop ends
                valid = True
            except:
                # invalid input, restart loop
                print("Invalid Input Try Again")
                valid = False
                # formats time into readable format
        (hrs, mins, secs) = time_input.split(":")
        time_input = datetime.timedelta(hours = int(hrs), minutes = int(mins), seconds = int(secs))
        # same thing as above, using to loop until a valid package is given
        valid = False # did not calculate time complexity since it is only input validation
        while valid == False:
            # package_input is the user input of a package
            package_input = int(input("What package would you like to search? Please enter a number 1-40.\n"))
            # check to see if package ID exists. it will be somewhere between1 and 41
            if (package_input in range(1,41,1)):
                # if exists, then end loop
                valid = True
            else:
                # if not exist, continue looping
                valid = False
                # lookup package based on id given. lookup defined in hash.py
        p = hashTable.lookup(package_input)
        # if in truck 1, depart time = truck 1 depart time
        if (package_input in t1.packages):
            p.departureTime = t1PackagesDepartTime
            truckNum = 1
        # if in truck 2, depart time = truck 2 depart time
        elif (package_input in t2.packages):
            p.departureTime = t2PackagesDepartTime
            truckNum = 2
        # if in truck 3, depart time = truck 3 depart time
        elif (package_input in t3.packages):
            p.departureTime = t3PackagesDepartTime
            truckNum = 3
        # if time input is after depart time but before delivered time, it is on route
        if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
            p.status= "En Route"
        # if time input is after delivered time, it is delivered
        elif (p.deliveredTime < time_input):
            p.status = "Delivered"
        # else (before depart time) it is at hub stil
        else:
            p.status = "At hub waiting to leave"
        # tell us what truck the package is on
        print(colors.CRED + "Package is on truck " + str(truckNum) + colors.CEND)
        # textual output for package
        print("Package " + str(p.ID) +  " status at " + str(time_input) + ":\n")
        print(colors.CPURPLE + "ID:" + str(p.ID) + colors.CEND)
        print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
        # only print delivered time if already delivered
        if(p.status == 'Delivered'):
            print("Delivery Time: " + str(p.deliveredTime))
        print("Deadline Time: " + str(p.Deadline_time))
        print("Weight: " + str(p.weight))
        print("Status: " + str(p.status) + "\n")



    # if x is equal to 3, return all packages at a given time
    elif (x == 3):
        # same thing as above, using to loop until a valid package is given
        valid = False 
         # keep running loop until there is a valid input. did not calculate time complexity since it is only input validation
        while valid == False:
            # try catch to handle the condition of A. proper input and B. improper input
            try:
                 #time_input stores the variable of the user input
                time_input = input("What time would you like to search? Please use format: HH:MM:SS\n")
                # we use this to validate the format of the input
                datetime.time.fromisoformat(time_input)
                # if valid, valid is true and the while loop ends
                valid = True
            except:
                # invalid input, restart loop
                print("Invalid Input Try Again")
                valid = False
                # formats time into readable format
        (hrs, mins, secs) = time_input.split(":")
        time_input = datetime.timedelta(hours = int(hrs), minutes = int(mins), seconds = int(secs))
        
        # output for truck 1
        print(colors.CRED + "Truck 1 Package Statuses at " + str(time_input) + colors.CEND + "\n")
        # for each package in truck 1
        for i in t1.packages:
            # lookup package based on id from t1.packages
            p = hashTable.lookup(i)
            # departure time for all packages in truck 1 will be the same as the depart time of truck 1
            p.departureTime = t1PackagesDepartTime
            # if time input is before delivered time but greater or equal to depart time, it is en route
            if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
                p.status= "En Route"
            # if time input is after delivered time, it is delivered
            elif (p.deliveredTime < time_input):
                p.status = "Delivered"
            # else, it is at hub
            else:
                p.status = "At hub waiting to leave"
            #textual output for truck 1
            print(colors.CPURPLE + "ID:" + str(p.ID) + colors.CEND)
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            # only print delivery time if it has been delivered
            if(p.status == 'Delivered'):
                print("Delivery Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: " + str(p.status) + "\n")

        # output for truck 2
        print(colors.CRED + "Truck 2 Package Statuses at " + str(time_input) + colors.CEND + "\n")
        # for each package in truck 2
        for i in t2.packages:
            # lookup package based on id from t2.packages
            p = hashTable.lookup(i)
            # depart time for all packages in truck 2 will be the same as depart time of truck 2
            p.departureTime = t2PackagesDepartTime
            # if time input is before delivered time but after or equal to depart time, it is on route
            if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
                p.status= "En Route"
            # if time input is after delivered time, it is delivered
            elif (p.deliveredTime < time_input):
                p.status = "Delivered"
            else:
            # else, it is at hub
                p.status = "At hub waiting to leave"
            # textual output for truck 2
            print(colors.CPURPLE + "ID:" + str(p.ID) + colors.CEND)
            # only print delivery time if it has been delivered
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            if(p.status == 'Delivered'):
                print("Delivery Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: " + str(p.status) + "\n")

        # output for truck 3
        print(colors.CRED + "Truck 3 Package Statuses at " + str(time_input) + colors.CEND + "\n")
        # for each package in truck 3
        for i in t3.packages:
            # look up packages based on id from truck 3 package list
            p = hashTable.lookup(i)
            # for all trucks in truck 3, depart time is equal to truck 3 depart time
            p.departureTime = t3PackagesDepartTime
            # if time input is before deliverd but after or qual to depart time
            if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
                p.status= "En Route"
                # if time input is after delivered time, it is delivered
            elif (p.deliveredTime < time_input):
                p.status = "Delivered"
            else:
                #else, it is at hub
                p.status = "At hub waiting to leave"
            # textual output for pacakges
            print(colors.CPURPLE + "ID:" + str(p.ID) + colors.CEND)
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            # only print delivery time if it has been delivered
            if(p.status == 'Delivered'):
                print("Delivery Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: " + str(p.status) + "\n")
        


    # if x is equal to 4, quit program entirely
    elif (x == 4):
        quit()