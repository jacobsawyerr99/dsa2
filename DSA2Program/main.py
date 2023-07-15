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

interface.prompt()

# handler for packages. Loads into hash table in hash.py
def loadPkgInHash(hash_table_init):
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
                # print (pakgeObj) --> test to make sure all packages populate
# init and load hashmap with package info with hashmap in hash.py              
hash_table_init = hashFunc()
loadPkgInHash(hash_table_init)

# print(hash_table_init.lookup(15)) --> test

# load packages into trucks here
# we effectively have two trucks since we only have two drivers.
t1 = truckObject()
t2 = truckObject()
t3 = truckObject()


def loadTruck1():
    list1 = []
    # deliver packages that need to be together
    print("Loading packages that need to be delivered together with 13,15, and 19...")
    sleep(1)
    # loop through all packages (pass 1)adding all packages that need to be delivered with 13,15,19.
    for i in range (1, 41):
        #lookup up package based on ID
        packageID = hash_table_init.lookup(i)
        # if theres no id (meaning already loaded, then skip
        if packageID != None:
            # get status of package (the note about needing to be loaded with others)
            packageID = package.GetStatus(packageID)
            # check to see if its any package that meets criteria
            if ("Must be delivered with" in str(packageID).strip()) or (i == 13) or (i == 15) or (i == 19):
                # add to to-load list
                list1.append(i)
                # removed from hashtable since loaded
                hash_table_init.remove(i)
                # if we reach max size then return list
                if len(list1) == 16:
                    print("16 package limit reached. Delivering now.")
                    return list1 
    # deliver packages with same address as the packages above            
    print("Adding packages with same address")
    # loop through all packages, adding the packages that meet the "same address" criteria
    for i in range (1, 41):
        # lookup based on package ID
        packageID = hash_table_init.lookup(i)
        # if theres no ID (already loaded), then skip
        if packageID != None:
            # get address of all packages
            packageID = package.GetAddress(packageID)
            # if the address matches
            if (str(packageID).strip() == "2010 W 500 S" or str(packageID).strip() == "4300 S 1300 E" or str(packageID).strip() == "4580 S 2300 E" or str(packageID).strip() == "177 W Price Ave" or str(packageID).strip() == "3595 Main St"):
                # add to to load list for truck 1
                list1.append(i)
                # remove from hashmap since being loaded
                hash_table_init.remove(i)
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


def loadTruck2():
    # first iterate through all notes requiring to be on truck 2
    list1 = []
     # deliver packages that need to be on truck 2. this truck will also wait behind because of the news some packages are late.
    print("Loading packages that need to be on truck 2. Waiting on late packages as well...")
    # loop through remaining packages
    for i in range (1, 41):
        # lookup based on ID
        packageID = hash_table_init.lookup(i)
        # if the package is not listed, move on since its already loaded
        if packageID != None:
            # get status/ note that package needs to be on specific truck
            packageID = package.GetStatus(packageID)
            # if note signifies package needs to be on truck 2
            if str(packageID).strip() == "Can only be on truck 2":
                # add to truck 2
                list1.append(i)
                # remove same package from hashmap since its being loaded
                hash_table_init.remove(i)
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
    

def loadTruck3():
    return 0


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


