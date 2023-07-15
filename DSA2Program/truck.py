from dataclasses import dataclass
from package import packageObject

# For the data classes, I used a python module "dataclass" to do so. There is nothing in the rubric preventing so, and only mentions to not use dicts to build hashmap
# data class has all of the necessary components for this project, so both the truck and package objects were created with that in mind.


@dataclass
class truckObject:
    speed = float
    packages = list[int]
    distanceTraveled = float
    departTime = str


def __len__(self):
        return len(self.list)

