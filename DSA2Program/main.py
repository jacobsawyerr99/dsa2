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

interface.prompt()

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

#function to load truck 1 based on parameters
def loadTruck1():
    list1 = []
    # deliver packages that need to be together
    print("Loading packages that need to be delivered together with 13,15, and 19...")
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
            if ("Must be delivered with" in str(packageID).strip()) or (i == 13) or (i == 15) or (i == 19) or (i == 40):
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
# output
print (t1.packages)

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
# output
print (t2.packages)
    
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
# call interface to load truck 3
interface.loadingTruckInterface(3)
#call loadTruck3 Method
t3.packages = loadTruck3()
# output
print (t3.packages)
sleep(1)
package9 = package.updatedPackage(hash_table_init.lookup(9))


# handler for addresses. called within interface.py
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
    
# handler for distances. called within interface.py
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

def deliver(truck, startAddress, departTime):
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
        # get index of minimum value. This will match with index in package list
        minDistIndex = distanceList.index(min(distanceList))

        # nextPackage will be looked up in hash based on index of value in truck.packages
        nextPackage = hash_table_init.lookup(truck.packages[minDistIndex])
        # we then assign the nextPackage variable to the address of the next package. this will be sent to the recursion of the function
        nextPackage = nextPackage.address
        # delete values from truck.packages and distancelist so we no longer have to deal with those values
        del truck.packages[minDistIndex]
        del distanceList[minDistIndex]
        # add distance travled for each minimum distance
        truck.distanceTraveled = truck.distanceTraveled + minDist
        # webinars suggested tracking this time this way (with dateTime)
        truck.departTime += datetime.timedelta(hours = minDist / 18)
        print (truck.departTime)
        # recursion
        deliver(truck, nextPackage, truck.departTime)
    # if there is only 1 package left in truck.packages
    else:
        # notify reader we are going back to hub
        print("Returning to hub...")
        # add distance from last location back to hub
        truck.distanceTraveled = truck.distanceTraveled + findDistance(address_lookup((hash_table_init.lookup(truck.packages[0])).address), address_lookup("4001 South 700 East"))
        truck.departTime += datetime.timedelta(hours = findDistance(address_lookup((hash_table_init.lookup(truck.packages[0])).address), address_lookup("4001 South 700 East")) /18 )
    

    # used to add up mileage for each truck
    # print(truck.packages[minDistIndex]) --> gets element from index based on distance
    # returns statement to get the minDist (this will change)


# next we need to complete steps for truck 1 then add in time functinality. After that,
# do truck 2 and 3 with their special requirements.
# modify interface to be able to display package at any given time.
def t1Deliver():
    undelivered1 = t1.packages.copy()
    t1.departTime = datetime.timedelta(hours = 8)
    deliver(t1, t1.startingAddress, t1.departTime)
    print(t1.distanceTraveled)
    print(t1.departTime)
    print("t1 finished")
    t1.packages = undelivered1

def t2Deliver():
    undelivered2 = t2.packages.copy()
    t2.departTime = datetime.timedelta(hours = 9)
    deliver(t2, t2.startingAddress, t2.departTime)
    print(t2.distanceTraveled)
    print(t2.departTime)
    print("t2 finished")
    t2.packages = undelivered2

def t3Deliver():
    undelivered = t3.packages.copy()
    print("truck 1 has returned to hub. delivering truck 3 right now.")
    t3.departTime = datetime.timedelta(hours = 10, minutes= 30)
    deliver(t3, t3.startingAddress, t3.departTime)
    print(t3.distanceTraveled)
    print(t3.departTime)
    t3.packages = undelivered