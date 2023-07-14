from dataclasses import dataclass

# For the data classes, I used a python module "dataclass" to do so. There is nothing in the rubric preventing so, and only mentions to not use dicts to build hashmap
# data class has all of the necessary components for this project, so both the truck and package objects were created with that in mind.


@dataclass
class packageObject:
    ID: int
    address: str
    city: str
    state: str
    zipcode: str
    Deadline_time: str
    weight: int
    status: str