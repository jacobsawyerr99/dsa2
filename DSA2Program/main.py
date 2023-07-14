# Created by Jacob Sawyer
# Student ID: 010397170

# imports
import csv
from hash import hashFunc
from package import packageObject
from truck import truckObject
import interface

# init prompt from interface.py. This generates all output text
interface.prompt()

# handler for packages. Loads into hash table in hash.py
def loadPkgInHash(hash_table_init):
    # actual csv reader to grab data from packageFile.csv
    with open ("packageFile.csv") as packageFileImport:
        packageList = csv.reader(packageFileImport)
        packageList = list(packageList)
        # assigns all 8 columns within csv to attributes of package object.
        # for loop creates indexed list and then package object is created in package.py
        for package in packageList:
            id = package[0]
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadlineTime = package[5]
            kgs = package[6]
            notes = package[7]
            # my csv generated multiple empty lists. this is a check to make sure only
            # lists that have an id are converted to a package
            if (package[0] != ''):
                pakgeObj = packageObject(int(id), address, city, state, zip, deadlineTime, kgs, notes)
                hash_table_init.insert(int(id), pakgeObj)
# init and load hashmap with package info with hashmap in hash.py              
hash_table_init = hashFunc()
loadPkgInHash(hash_table_init)

# print(hash_table_init.lookup(15)) --> test for hashmap

# load packages into trucks here
# we effectively have two trucks since we only have two drivers
truck1 = truckObject()
truck2 = truckObject()
truck3 = truckObject()












