from dataclasses import dataclass
from dataclasses import fields
from time import sleep
import hash
import colors

# For the data classes, I used a python module "dataclass" to do so. There is nothing in the rubric preventing so, and only mentions to not use dicts to build hashmap
# data class has all of the necessary components for this project, so both the truck and package objects were created with that in mind.

#### Big O = O(1)

@dataclass
class packageObject:
    ID: int() # package ID
    address: str # package address
    city: str  # package city
    state: str # package state
    zipcode: str # package zipcode
    Deadline_time: str #package deadline
    weight: int # package weight
    status: str() # package status
    deliveredTime = 0
    departureTime = 0
    
#### big O = O(1)
def GetStatus(self): # returns note/status of package
    return self.status

#### Big O = O(1)
def GetAddress(self): # returns address of package
    return self.address
    
#### Big = O(1)
# package #9 has wrong address. this method will be called to update it.
def updatedPackage(self):
    # prints the output that the address is being updates
    print(colors.CREDBORDER + "\nAlert!!!: " + colors.CEND + "We have received updated address for package 9. New Address is: 410 S State St., Salt Lake City, UT 84111\n")
    # self (package 9) new address
    self.address = "410 S State St."
    # self package zipcode update
    self.zipcode = "84111"
    #sleep so its easier to read
    sleep(1)
    print("Address Updated! Good to go.")