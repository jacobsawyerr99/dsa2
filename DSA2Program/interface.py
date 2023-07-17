from hash import hashFunc
from package import packageObject
from truck import truckObject
import package
from dataclasses import fields
from time import sleep
import colors
import datetime
# start of program. initalized in main at top
def prompt():
    # prompt for program start
    print(colors.CRED + "\nWelcome to the WGU Truck Routing Program." + colors.CEND)
    sleep(1)
    print(colors.CRED + "This program is a python implementation of the traveling salesman problem." + colors.CEND)
    sleep(1)

# output for notification of truck loading
# tnum = number of truck
def loadingTruckInterface(tnum):
    sleep(1)
    # uses variable called from loading truck method
    print(colors.CPURPLE + "\n\nLoading truck " + str(tnum) + "..." + colors.CEND)
    sleep(1)

# output for total mileage of route
def output(t1, t2, t3, hashTable, t1PackagesDepartTime, t2PackagesDepartTime, t3PackagesDepartTime):
    print("\nThe total mileage for this route is...")
    sleep(2)
    print(colors.CUL + colors.CGREEN + str(t1.distanceTraveled + t1.distanceLastPackageToHub + t2.distanceTraveled + t2.distanceLastPackageToHub + t3.distanceTraveled + t3.distanceLastPackageToHub)+ colors.CEND + "\n") # add truck 1 2 and 3 mileage here.
    x = 0
    while(x != 1 and x != 2 and x != 3 and x != 4): 
        print("What would you like to do?")
        print("1. Print all packages and delivered times?")
        print("2. Get single packages status with a timestamp?")
        print("3. Get all packages status with a time stamp?")
        print("4. Exit Program")
        x = int(input("Enter 1, 2, 3, or 4\n"))


    if (x == 1):
        print("Packages on Truck 1")
        for i in t1.packages:
            p = hashTable.lookup(i)
            print("ID:" + str(p.ID))
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            print("Delivered Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: Delivered\n")
        print("Truck 1 Distance after getting back to Hub: " + str(t1.distanceLastPackageToHub + t1.distanceTraveled))
        print("Time returned to Hub: " + str(t1.timeLastPackageToHub) + "\n\n")
        print("Packages on Truck 2")
        for i in t2.packages:
            p = hashTable.lookup(i)
            print("ID:" + str(p.ID))
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            print("Delivered Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: Delivered\n")
        print("Truck 2 Distance after getting back to Hub: " + str(t2.distanceLastPackageToHub + t2.distanceTraveled))
        print("Time returned to Hub: " + str(t2.timeLastPackageToHub) + "\n")
        print("Packages on Truck 3")
        for i in t3.packages:
            p = hashTable.lookup(i)
            print("ID:" + str(p.ID))
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            print("Delivered Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: Delivered\n")
        print("Truck 3 Distance after getting back to Hub: " + str(t3.distanceLastPackageToHub + t3.distanceTraveled))
        print("Time returned to Hub: " + str(t3.timeLastPackageToHub) + "\n")



    elif (x == 2):
        valid = False 
        while valid == False:
            try:
                time_input = input("What time would you like to search? Please use format: HH:MM:SS\n")
                datetime.time.fromisoformat(time_input)
                valid = True
            except:
                print("Invalid Input Try Again")
                valid = False
        (hrs, mins, secs) = time_input.split(":")
        time_input = datetime.timedelta(hours = int(hrs), minutes = int(mins), seconds = int(secs))
        valid = False 
        while valid == False:
            package_input = int(input("What package would you like to search? Please enter a number 1-41.\n"))
            if (package_input in range(1,41,1)):
                valid = True
            else:
                valid = False
        p = hashTable.lookup(package_input)
        if (package_input in t1.packages):
            p.departureTime = t1PackagesDepartTime
            truckNum = 1
        elif (package_input in t2.packages):
            p.departureTime = t2PackagesDepartTime
            truckNum = 2
        elif (package_input in t3.packages):
            p.departureTime = t3PackagesDepartTime
            truckNum = 3
        if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
            p.status= "En Route"
        elif (p.deliveredTime < time_input):
            p.status = "Delivered"
        else:
            p.status = "At hub waiting to leave"
        print("Package is on truck " + str(truckNum))
        print("ID:" + str(p.ID))
        print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
        if(p.status == 'Delivered'):
            print("Delivery Time: " + str(p.deliveredTime))
        print("Deadline Time: " + str(p.Deadline_time))
        print("Weight: " + str(p.weight))
        print("Status: " + str(p.status) + "\n")



    elif (x == 3):
        valid = False 
        while valid == False:
            try:
                time_input = input("What time would you like to search? Please use format: HH:MM:SS\n")
                datetime.time.fromisoformat(time_input)
                valid = True
            except:
                print("Invalid Input Try Again")
                valid = False
        (hrs, mins, secs) = time_input.split(":")
        time_input = datetime.timedelta(hours = int(hrs), minutes = int(mins), seconds = int(secs))
        print("Truck 1 Package Statuses at " + str(time_input) + "\n")
        for i in t1.packages:
            p = hashTable.lookup(i)
            p.departureTime = t1PackagesDepartTime
            if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
                p.status= "En Route"
            elif (p.deliveredTime < time_input):
                p.status = "Delivered"
            else:
                p.status = "At hub waiting to leave"
            print("ID:" + str(p.ID))
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            if(p.status == 'Delivered'):
                print("Delivery Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: " + str(p.status) + "\n")

        print("Truck 2 Package Statuses at " + str(time_input) + "\n")
        for i in t2.packages:
            p = hashTable.lookup(i)
            p.departureTime = t2PackagesDepartTime
            if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
                p.status= "En Route"
            elif (p.deliveredTime < time_input):
                p.status = "Delivered"
            else:
                p.status = "At hub waiting to leave"
            print("ID:" + str(p.ID))
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            if(p.status == 'Delivered'):
                print("Delivery Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: " + str(p.status) + "\n")

        print("Truck 3 Package Statuses at " + str(time_input) + "\n")
        for i in t3.packages:
            p = hashTable.lookup(i)
            p.departureTime = t3PackagesDepartTime
            if ((p.departureTime <= time_input) and (time_input < p.deliveredTime)):
                p.status= "En Route"
            elif (p.deliveredTime < time_input):
                p.status = "Delivered"
            else:
                p.status = "At hub waiting to leave"
            print("ID:" + str(p.ID))
            print("Address: " + str(p.address) + ", " + str(p.city) + ", " + str(p.state) + ", " + str(p.zipcode))
            if(p.status == 'Delivered'):
                print("Delivery Time: " + str(p.deliveredTime))
            print("Deadline Time: " + str(p.Deadline_time))
            print("Weight: " + str(p.weight))
            print("Status: " + str(p.status) + "\n")
        

    elif (x == 4):
        quit()