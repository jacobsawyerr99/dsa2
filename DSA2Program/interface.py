from hash import hashFunc
from package import packageObject
from truck import truckObject
import package
from dataclasses import fields
from time import sleep
import colors


def prompt():
    # prompt for program start
    print(colors.CRED + "\nWelcome to the WGU Truck Routing Program." + colors.CEND)
    sleep(1)
    print(colors.CRED + "This program is a python implementation of the traveling salesman problem." + colors.CEND)
    sleep(1)

# output for notification of truck loading
def loadingTruckInterface(tnum):
    sleep(1)
    # uses variable called from loading truck method
    print(colors.CPURPLE + "\n\nLoading truck " + str(tnum) + "..." + colors.CEND)
    sleep(1)

# output for total mileage of route
def mileage():
    print("\nThe total mileage for this route is...")
    sleep(2)
    print(colors.CUL + colors.CGREEN + 'Test' + colors.CEND + "\n") # add truck 1 2 and 3 mileage here.
    print("What would you like to do?")
# include method for 
# a. determining total mileage by all trucks
# b. package delivery status at a specific time for one or multiple trucks
# c. exit program