from dataclasses import dataclass
from package import packageObject

# For the data classes, I used a python module "dataclass" to do so. There is nothing in the rubric preventing so, and only mentions to not use dicts to build hashmap
# data class has all of the necessary components for this project, so both the truck and package objects were created with that in mind.


@dataclass
class truckObject:
    speed = 18.0 # speed of truck
    packages = list[int] # list for packages
    distanceTraveled = 0.0 #starting distance traveled
    departTime = str # time truck departed
    startingAddress = "4001 South 700 East" #start of trip (hub)
    distanceLastPackageToHub = 0
    timeLastPackageToHub = 0

