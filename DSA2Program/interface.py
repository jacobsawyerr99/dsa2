from time import sleep

# color codes from ANSI used to stylize text
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN  = '\33[92m'
CUL = '\033[4m'

# prompt for program
def prompt():
    print(CRED + "\nWelcome to the WGU Truck Routing Program." + CEND)
    sleep(1)

    print(CRED + "This program is a python implementation of the traveling salesman problem." + CEND)
    sleep(1)

    print("\nThe total mileage for this route is...")
    sleep(2)
    print(CUL + CGREEN + 'Test' + CEND + "\n") # add truck 1 2 and 3 mileage here.

    print("What would you like to do?")
    # include method for 
    # a. determining total mileage by all trucks
    # b. package delivery status at a specific time for one or multiple trucks
    # c. exit program