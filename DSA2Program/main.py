# Created by Jacob Sawyer
# Student ID: 010397170

# imports here
import csv
from hash import hashFunc
from package import packageObject
from truck import truckObject
import package
from dataclasses import fields
from time import sleep
import interface
import datetime

# Overall time complexity = O(n^2)
# Class time complexity = O(n^2)

interface.prompt()

# entire flow of program followes recommended steps given by Professor Lusby's study guide

#### Big O = O(n)
# handler for packages. Loads into hash table in hash.py. using 2 copies to be able to effectively load trucks
def loadPkgInHash(hash_table_init, hash_table_init2):
    # actual csv reader to grab data from packageFile.csv
    with open ("packageFile.csv") as packageFileImport:
        packageList = list(csv.reader(packageFileImport))
        # assigns all 8 columns within csv to attributes of package object.
        # for loop creates indexed list and then package object is created in package.py
        for package in packageList:
            # my csv generated multiple empty lists. this is a check to make sure only
            # lists that have an id are converted to a package
            if (package[0] != ''):
                pakgeObj = packageObject(int(package[0]), 
                                         package[1], 
                                         package[2], 
                                         package[3], 
                                         package[4], 
                                         package[5], 
                                         package[6], 
                                         package[7])
                hash_table_init.insert(int(package[0]), pakgeObj)
                # created dupe hashtable to assist in loading trucks
                hash_table_init2.insert(int(package[0]), pakgeObj)
                # print (pakgeObj) --> test to make sure all packages populate
# init and load hashmap with package info with hashmap in hash.py              
hash_table_init = hashFunc()
# created a dupe hash table to assist in loading trucks
hash_table_init2 = hashFunc()
# calls to load both copies of hashtable. second one will be empty after trucks are loaded.
loadPkgInHash(hash_table_init, hash_table_init2)

# print(hash_table_init.lookup(15)) --> test

# load packages into trucks here
# we effectively have two trucks since we only have two drivers.
t1 = truckObject()
t2 = truckObject()
t3 = truckObject()

#### Big O = O(n)
#function to load truck 1 based on parameters
def loadTruck1():
    list1 = []
    # deliver packages that need to be together
    print("Loading packages that need to be delivered together with 13,15, and 19. Also loading packages with early deadlines...")
    sleep(1)
    # loop through all packages (pass 1)adding all packages that need to be delivered with 13,15,19.
    for i in range (1, 41):
        #lookup up package based on ID
        packageID = hash_table_init2.lookup(i)
        # if theres no id (meaning already loaded, then skip
        if packageID != None:
            # get status of package (the note about needing to be loaded with others)
            packageID = package.GetStatus(packageID)
            # check to see if its any package that meets criteria
            if ("Must be delivered with" in str(packageID).strip()) or (i == 13) or (i == 15) or (i == 19) or (i == 40) or (i == 1) or (i == 31) or (i ==30) or (i ==2) or (i == 37)or (i == 29):
                # add to to-load list
                list1.append(i)
                # removed from hashtable since loaded
                hash_table_init2.remove(i)
                # if we reach max size then return list
                if len(list1) == 16:
                    print("16 package limit reached. Delivering now.")
                    return list1 
    # deliver packages with same address as the packages above            
    print("Adding packages with same address")
    # loop through all packages, adding the packages that meet the "same address" criteria
    for i in range (1, 41):
        # lookup based on package ID
        packageID = hash_table_init2.lookup(i)
        # if theres no ID (already loaded), then skip
        if packageID != None:
            # get address of all packages
            packageID = package.GetAddress(packageID)
            # if the address matches
            if (str(packageID).strip() == "2010 W 500 S" or str(packageID).strip() == "4300 S 1300 E" or str(packageID).strip() == "4580 S 2300 E" or str(packageID).strip() == "177 W Price Ave" or str(packageID).strip() == "3595 Main St"):
                # add to to load list for truck 1
                list1.append(i)
                # remove from hashmap since being loaded
                hash_table_init2.remove(i)
                # if we hit limit, finish loading
                if len(list1) == 16:
                    print("16 package limit reached. Delivering now.")
                    return list1 
    return list1
# call interface to load truck 1
interface.loadingTruckInterface(1)
# call loadTruck1 method
t1.packages = loadTruck1()
# output of package list
print (t1.packages)


#### Big O= O(n)
# function to load truck 2 based on parameters
def loadTruck2():
    # first iterate through all notes requiring to be on truck 2
    list1 = []
     # deliver packages that need to be on truck 2. this truck will also wait behind because of the news some packages are late.
    print("Loading packages that need to be on truck 2. Waiting on late packages as well...")
    # loop through remaining packages
    for i in range (1, 41):
        # lookup based on ID
        packageID = hash_table_init2.lookup(i)
        # if the package is not listed, move on since its already loaded
        if packageID != None:
            # get status/ note that package needs to be on specific truck
            packageID = package.GetStatus(packageID)
            # if note signifies package needs to be on truck 2
            if str(packageID).strip() == "Can only be on truck 2":
                # add to truck 2
                list1.append(i)
                # remove same package from hashmap since its being loaded
                hash_table_init2.remove(i)
                # if we hit truck limit then pause loading
                if len(list1) == 16:
                    print("16 package limit reached. Delivering now.")
                    return list1 
    print("Loading Delayed Packages...")
    # loop through remaining packages
    for i in range (1, 41):
        # lookup based on ID
        packageID = hash_table_init2.lookup(i)
        # if the package is not listed, move on since its already loaded
        if packageID != None:
            # get status/ note that package needs to be on specific truck
            packageID = package.GetStatus(packageID)
            # if note signifies package needs to be on truck 2
            if (str(packageID).strip() == "Delayed on flight---will not arrive to depot until 9:05 am"):
                # add to truck 2
                list1.append(i)
                # remove same package from hashmap since its being loaded
                hash_table_init2.remove(i)
                # if we hit truck limit then pause loading
                if len(list1) == 16:
                    print("16 package limit reached. Delivering now.")
                    return list1 
    print("Loading Packages with same address...")
    # loop through remaining packages
    for i in range (1, 41):
        # lookup based on ID
        packageID = hash_table_init2.lookup(i)
        # if the package is not listed, move on since its already loaded
        if packageID != None:
            # get status/ note that package needs to be on specific truck
            packageID = package.GetAddress(packageID)
            # if note signifies package needs to be on truck 2
            if (str(packageID).strip() == (str(packageID).strip() == "380 W 2880 S")  or (str(packageID).strip() == "2530 S 500 E" or (str(packageID).strip() == "410 S State St")) or (str(packageID).strip() =="1330 2100 S")):
                # add to truck 2
                list1.append(i)
                # remove same package from hashmap since its being loaded
                hash_table_init2.remove(i)
                # if we hit truck limit then pause loading
                if len(list1) == 16:
                    print("16 package limit reached. Delivering now.")
                    return list1 
    return list1
# call interface to load truck 2
interface.loadingTruckInterface(2)
#call loadTruck2 Method
t2.packages = loadTruck2()
# output of package list
print (t2.packages)
    

#### Big O = O(n)
# truck 3 can not leave the hub until truck 1 returns. There is only 2 drivers.
def loadTruck3():
    list1 = []
    # loads packages not on truck 1 or 2
    print("Loading remainder of packages...")
    # loop through remaining packages
    for i in range (1, 41):
        # lookup based on ID
        packageID = hash_table_init2.lookup(i)
        # if the package is not listed, move on since its already loaded
        if packageID != None:
            # add remainder of packages to truck 3
            list1.append(i)
            # remove same package from hashmap since its being loaded
            hash_table_init2.remove(i)
            # if we hit truck limit then pause loading
            if len(list1) == 16:
                print("16 package limit reached.")
                return list1 
    return list1
# call interface to load truck 3
interface.loadingTruckInterface(3)
#call loadTruck3 Method
t3.packages = loadTruck3()
# output of package list
print (t3.packages)
sleep(1)
# update package 9. it has the wrong address
package9 = package.updatedPackage(hash_table_init.lookup(9))


#### Big O = O(n)
# handler for addresses. called within interface.py. function is recommended by professor lusby
def address_lookup(address):
    # csv read for addressFile.csv
    with open ("addressFile.csv") as addressFileImport:
        addressList = list(csv.reader(addressFileImport))
    # per instructions of professor Lusby's email, it is beneficial to create an address lookup
    # capablity. This essentially finds an address and pulls a unique id from address list
    # print (addressList)
    for lists in addressList:
        if address in lists:
            return (addressList.index(lists) + 1)
    

#### Big O = O(n)
# handler for distances. called within interface.py. function is recommended by professor lusby
def findDistance(x, y):
    # csv reader for distanceFile.csv reads into list, distanceList
    with open ("distanceFile.csv") as distanceFileImport:
        distanceList = list(csv.reader(distanceFileImport))
    # this is a typical case where the is a distance listed in excel sheet.
    distance = distanceList[x-1][y-1]
    # this catches the cases where there is a zero or empty section in distances list
    # basically, reverses coordinates to search. For example, if I use loadDistance(2,3), I would return '', whicf is invalid.
    # With the reversal of coordinates, this would be 9.2. And since python indexes at zero, i subtract one to keep everything consistent.
    # This provides the correct distance, 7.1
    if "".__eq__(distance):
        distance = distanceList[y-1][x-1]
    # print (float(distance)) --> test
    return float(distance)

# findDistance(5, 4) --> test
# address_lookup("380 W 2880 S") --> test

# deliver method. "truck" is passed below. Signifies which of three trucks is being delivered
# uses the nearest neighbor algorithm to deliver packages. First assigns all distances from start point to list
# it is recursive until there are 0 packages in list.


#### Big O = O(n^2), would be O(n) if we only called it once. but it is called recursively 
def deliver(truck, startAddress): # nearest neighbor algorithm is deliver function
    # empty list to store distances
    distanceList = []
    # look through list of IDs in truck packages 
    for i in truck.packages:
        # find assocaited package
        p = hash_table_init.lookup(i)
        # get starting address (this will be updated with 'next' address after remove og address)
        a1 = address_lookup(startAddress)
        # get next address distances
        a2 = address_lookup(p.address)
        # generate distance between starting addreess (new one each time) and rest of addresses remaining
        distanceList.append(findDistance(a1, a2))
    # if there is more than one item in list of packages (if theres only one then the next location will be the hub)
    if(len(truck.packages) > 1):
        # get min value of our distance list generated in the above for loop
        minDist = min(distanceList)
        # webinars suggested tracking this time this way (with dateTime)
        truck.departTime += datetime.timedelta(hours = minDist / truck.speed)
        # get index of minimum value. This will match with index in package list
        minDistIndex = distanceList.index(min(distanceList))
        # nextPackage will be looked up in hash based on index of value in truck.packages
        nextPackage = hash_table_init.lookup(truck.packages[minDistIndex])
        nextPackage.deliveredTime = truck.departTime
        # we then assign the nextPackage variable to the address of the next package. this will be sent to the recursion of the function
        nextPackage = nextPackage.address
        # delete values from truck.packages and distancelist so we no longer have to deal with those values
        del truck.packages[minDistIndex]
        del distanceList[minDistIndex]
        # add distance travled for each minimum distance
        truck.distanceTraveled = truck.distanceTraveled + minDist
        # recursion
        deliver(truck, nextPackage)
    # if there is only 1 package left in truck.packages
    else:
        # last package:
        truck.distanceTraveled = findDistance(a1, a2) + truck.distanceTraveled
        truck.departTime += datetime.timedelta(hours = (findDistance(a1, a2)) / truck.speed)
        p.deliveredTime = truck.departTime   


        # notify reader we are going back to hub
        # add distance from last location back to hub
    # used to add up mileage for each truck
    # print(truck.packages[minDistIndex]) --> gets element from index based on distance
    # returns statement to get the minDist (this will change)

#### Big O = O(1)
# function to deliver truck 1 and get distance back to hub and final time
def t1Deliver():
    # created dupe list since deliver method clears the t1.packages list
    undelivered1 = t1.packages.copy()
    # truck one will be first truck of day to leave. Driver of this truck will also be driving truck 3 at 10:30
    t1.departTime = datetime.timedelta(hours = 8)
    # calls nearest neighbor deliver function
    deliver(t1, t1.startingAddress)
    # backToHub
    # gets distance from last package location back to hub
    t1.distanceLastPackageToHub = findDistance(address_lookup((hash_table_init.lookup(t1.packages[0])).address), address_lookup("4001 South 700 East"))
    # gets time to go from last package to hub. This is essentially the time the truck returns
    t1.timeLastPackageToHub = t1.departTime + datetime.timedelta(hours = findDistance(address_lookup((hash_table_init.lookup(t1.packages[0])).address), address_lookup("4001 South 700 East")) / t1.speed )
    # repopulate truck list
    t1.packages = undelivered1

#### Big 0 = O(1)
# function to deliver truck 2 and get distance back to hub and final time
def t2Deliver():
    # created dupe list since deliver method clears the t2.packages list
    undelivered2 = t2.packages.copy()
    # truck two will be second truck to leave at 0900
    t2.departTime = datetime.timedelta(hours = 9)
    # calls nearest neighbor deliver function
    deliver(t2, t2.startingAddress)
    # backToHub
    # gets distance from last package location back to hub
    t2.distanceLastPackageToHub = findDistance(address_lookup((hash_table_init.lookup(t2.packages[0])).address), address_lookup("4001 South 700 East"))
    # gets time to go from last package to hub. This is essentially the time the truck returns
    t2.timeLastPackageToHub = t2.departTime + datetime.timedelta(hours = findDistance(address_lookup((hash_table_init.lookup(t2.packages[0])).address), address_lookup("4001 South 700 East")) / t2.speed )
    # repopulate truck list
    t2.packages = undelivered2

#### Big O = O(1)
# function to deliver truck 3 and get distance back to hub and final time
def t3Deliver():
    # created dupe list since deliver method clears the t3.packages list
    undelivered = t3.packages.copy()
    # truck 3 will be the third truck to leave at 10:30. The same driver that drove truck 1 will be driving this truck
    t3.departTime = datetime.timedelta(hours = 10, minutes= 30)
    # calls nearest neighbor deliver function
    deliver(t3, t3.startingAddress)
    # backToHub
    t3.distanceLastPackageToHub = findDistance(address_lookup((hash_table_init.lookup(t3.packages[0])).address), address_lookup("4001 South 700 East"))
    # gets time to go from last package to hub. This is essentially the time the truck returns
    t3.timeLastPackageToHub = t3.departTime + datetime.timedelta(hours = findDistance(address_lookup((hash_table_init.lookup(t3.packages[0])).address), address_lookup("4001 South 700 East")) / t3.speed )
    # repopulate truck list
    t3.packages = undelivered

#calls to run the previous 3 functinos
t1Deliver()
t2Deliver()
t3Deliver()

# calls output function in interface. this will handle rest of program
interface.output(t1, t2, t3, hash_table_init, datetime.timedelta(hours = 8), datetime.timedelta(hours = 9), datetime.timedelta(hours = 10, minutes= 30))
