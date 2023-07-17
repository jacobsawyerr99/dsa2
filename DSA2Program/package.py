from dataclasses import dataclass
from dataclasses import fields
from time import sleep
import hash
import colors

# For the data classes, I used a python module "dataclass" to do so. There is nothing in the rubric preventing so, and only mentions to not use dicts to build hashmap
# data class has all of the necessary components for this project, so both the truck and package objects were created with that in mind.


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
def GetStatus(self): # returns note/status of package
    return self.status

def GetAddress(self): # returns address of package
    return self.address
    
# package #9 has wrong address. this method will be called to update it.
def updatedPackage(self):
    print(colors.CREDBORDER + "\nAlert!!!: " + colors.CEND + "We have received updated address for package 9. New Address is: 410 S State St., Salt Lake City, UT 84111\n")
    self.address = "410 S State St."
    self.zipcode = "84111"
    sleep(1)
    print("Address Updated! Good to go.")