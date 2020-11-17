import pathlib
import datetime
import os

# welcome screen

print("\n\nWELCOME TO OUR PARKING LOT \n\n")
print("(If you want to see the commands to use the lot then type 'instructions' and press ENTER)\n\n")  # noqa
print("We charge based on seconds, 1 Rs for 2 seconds is our current price")
print("Please choose a mode\n")

# here we choose interactive mode or file read mode


def choosemode():
    global mode
    print("Press 1 and ENTER if you want to go with INTERACTIVE MODE")

    print("Press 2 and ENTER if you want to READ INPUT FROM A FILE")
    modeinput = input()

    if modeinput == "" or modeinput == " ":
        print("Please choose a correct mode")
        choosemode()
    elif modeinput == "instructions":
        abpath = str(pathlib.Path(__file__).parent.absolute())
        filepath = abpath.replace("\\", "/") + "/"+"instructions.txt"
        file = open(filepath, "r")
        for line in file:
            print(line)
        print()
        choosemode()
    else:
        if modeinput[0] == "1":
            mode = 1

        elif modeinput[0] == "2":
            mode = 2
        else:
            print("Please choose a correct mode")
            choosemode()


# This variable stays true until user types exit on the console
programIsRunning = True
lotexists = False
programOn = True
mode = 0
# Our class for car


class Car:

    def __init__(self, regNo, color):
        self.regNo = regNo
        self.color = color
        self.parkedtime = ""


# our class for parking lot

class ParkingLot:
    def __init__(self, size=6):
        self.lot = [0]*size  # creates and array with given size, default is 6

    # our dictionary to sort and store the color of cars and their reg no
        self.colorbasedsort = {}

    # function for parking the car
    def park(self, car):
        for i in range(len(self.lot)):
            if self.lot[i] == 0:
                self.lot[i] = car
                self.sortoncolor(car)
                print("Alloted slot number :", i+1)
                car.parkedtime = datetime.datetime.now()
                return
        else:
            print("Parking Lot is full, No space to park")
            print("You can add extra slots to the lot, see instructions for details")  # noqa

    # function for sorting the cars based on their colors
    def sortoncolor(self, car):
        if car.color in self.colorbasedsort.keys():
            self.colorbasedsort[car.color].append(car.regNo)
        else:
            self.colorbasedsort[car.color] = [car.regNo]

    # function for viewing the lot
    def viewLot(self):
        for i in range(len(self.lot)):
            if self.lot[i] != 0:
                print(self.lot[i].regNo, end=" ")
            else:
                print("empty", end=" ")
        print()

        print(self.colorbasedsort)

    # function for taking out a car from a slot
    def takeout(self, slot):
        if slot > len(self.lot) or slot < 1:
            print("Please Enter a valid slot number, Slot Number out of range")
            return
        if self.lot[slot-1] != 0:
            currentcar = self.lot[slot-1]
            currentime = datetime.datetime.now()
            timestayed = self.timepassed(currentcar.parkedtime, currentime)
            cost = timestayed.seconds//2
            self.lot[slot-1] = 0
            self.colorbasedsort[currentcar.color].remove(currentcar.regNo)
            print("You have been charged", "Rs.", cost)
            print("Slot no", slot, "is now free")
        else:
            print("Slot is already empty, there is no car at this spot")

    def timepassed(self, parked, leaving):
        second_elapsed = leaving - parked

        return second_elapsed

    # function for searching slot number of a car based on its reg no

    def searchonregno(self, regno):
        for i in range(len(self.lot)):
            if self.lot[i] != 0:
                if self.lot[i].regNo == regno:
                    print("Car found at slot number :  "+str(i+1))
                    return
                else:
                    continue
            else:
                continue
        print("Car not found")

    # function for searching slot of a car based on their color
    def slotoncolor(self, color):
        regnoarray = []
        if color in self.colorbasedsort:
            currentcolor = self.colorbasedsort[color]
            for j in currentcolor:
                for i in range(len(self.lot)):
                    if self.lot[i] != 0:
                        if self.lot[i].regNo == j:
                            if i+1 not in regnoarray:
                                regnoarray.append(i+1)
                        else:
                            continue
                else:
                    continue
        if len(regnoarray) == 0:
            print("No cars found with the color ",
                  color, "at the given moment")
        else:
            print("Cars with color", color.upper(), "are at slots: ", end=" ")
            for num in regnoarray:
                print(num, end=", ")
            print()

    # function that prints the reg no of cars based on their color
    def regnooncolor(self, color):
        if color in self.colorbasedsort and \
                len(self.colorbasedsort[color]) > 0:
            print("The cars with color ", color.upper(), "are as follows")
            for i in self.colorbasedsort[color]:
                print(i, end=" ,")
        else:
            print("No cars found with this color")
        print()

    # function that prints the current status of parkinglot
    def status(self):
        for i in range(len(self.lot)):
            if self.lot[i] != 0:
                print("SLOT NO.", i+1, "has a",
                      self.lot[i].color.upper(),
                      "car with REG NO.", self.lot[i].regNo)
            else:
                print("SLOT NO.", i+1, "is empty")

    # check the format of registration number

    def checkregno(self, regno):
        arr = regno.split("-")
        checkstring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        checknum = "1234567890"
        if len(arr) != 4:
            return False
        else:
            if len(arr[0]) == 2:

                for char in arr[0]:
                    if char not in checkstring:
                        return False
            else:
                return False
            if len(arr[1]) == 2:

                for char in arr[1]:
                    if char not in checknum:
                        return False
            else:
                return False

            if len(arr[2]) <= 2:
                for char in arr[2]:
                    if char not in checkstring:
                        return False
            else:
                return False

            if len(arr[3]) <= 4:
                for char in arr[3]:
                    if char not in checknum:
                        return False
            else:
                return False
        return True

    # adds extra slots
    def addslot(self, size):
        for _ in range(size):
            self.lot.append(0)


# function that takes user input string and split \
# and return the array of commands
def takeInput():

    return input("$$ ENTER YOUR COMMAND --->> ").split(" ")


parkinglot = None


def main(mode):
    if mode == 1:
        command = takeInput()
        inputcommand(command)
    if mode == 2:
        def getfilename():
            given = input("Enter the file name: ")
            if given == "" or given == " ":
                print("Please Enter a file name to continue: ")
                return getfilename()
            else:
                return given

        filename = getfilename()
        abpath = str(pathlib.Path(__file__).parent.absolute())
        filepath = abpath.replace("\\", "/") + "/"+filename
        if os.path.exists(filepath):

            file = open(filepath, "r")
            if file:

                for line in file:

                    command = line.rstrip()
                    commandsplit = command.split(" ")
                    inputcommand(commandsplit)
            else:
                print("File not found")
                choosemode()
        else:
            print("\nThe File name you entered does not exist, please retry\n")
            choosemode()


def inputcommand(command):
    # declaring the parking lot variable used globally
    global parkinglot

    # Prompts user to enter some command if the user leaves the console empty
    if command[0] == "":
        print()
        print("Please enter some command, View Instructions to check the commands that are supported\n")  # noqa

    # this runs if user inputs for creating a parking lot
    elif command[0] == "create_parking_lot":
        print()
        # checks if there exists a parking lot already,\
        #  if yes then will prompt user to not go ahead
        if parkinglot is not None:
            print(
                "There already exists a parking lot, doing this will erase all data on current lot\nPlease exit this program and restart to create a new one")  # noqa
            print()
        # checking if the size field is empty
        else:
            # checks if the user has entered all the parameters
            if len(command) < 2 or command[1] == "":
                print("You have not entered a size for our parking lot, If you hit enter a default lot with size 6 will be created\n OR type the size you want and hit enter to create a lot with desried size\n")  # noqa
                print("Waiting for your Response")
                response = input()
                # if user doesnt enter any size,\
                #  a default lot with size 6 is created
                if response == "" or response == " ":
                    parkinglot = ParkingLot()
                    print("Paking Lot with size 6 has been created\n ")
                # if user enters a size the lot is created
                elif response.isdecimal():
                    parkinglot = ParkingLot(int(response))
                    print("Paking Lot with size",
                          response, "has been created\n ")

                else:
                    print(
                        "Seems like you have not entered a correct format of size, Please use whole integers as size. TRY AGAIN\n")  # noqa
            # if user enters all fields correctly then lot is created
            elif command[1].isdecimal():
                parkinglot = ParkingLot(int(command[1]))

                print("Paking Lot with size", command[1], "has been created\n")
            # if user still enters wrong commands then\
            #  he will be prompted to try again
            else:
                print(
                    "Looks like you have entered wrong format for size of parking lot, please enter a whole integer and try again")  # noqa
        print()

    # command to park the car
    elif command[0] == "park":
        print()
        # checks if a parking lot exists or not
        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other operation without creating a parking lot\n")  # noqa
        else:
            # checks if command has all arguments
            if len(command) < 3:
                print(
                    "Park Command requires you to put Registration number and color of the car,\n Please Enter them and TRY AGAIN")  # noqa

            else:
                if command[2] == "":
                    print(
                        "Not entered a color for you car, Please enter a color and TRY AGAIN")  # noqa
                else:
                    if parkinglot.checkregno(command[1]):
                        car = Car(command[1], command[2].lower())
                        parkinglot.park(car)
                    else:
                        print("The format of registration number is wrong, please try again")  # noqa
        print()

    # command to leave or empty a slot
    elif command[0] == "leave":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other operation without creating a parking lot\n")  # noqa
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Leave command takes a slot number, Please enter slot number and try again")  # noqa
            else:
                if command[1].isdecimal():
                    parkinglot.takeout(int(command[1]))
                else:
                    print("The slot number should be an integer, Please Try again")  # noqa

        print()

    # prints a status of the lot
    elif command[0] == "status":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other operation without creating a parking lot\n")  # noqa
        else:
            parkinglot.status()

        print()

    # prints reg no of cars with given color
    elif command[0] == "registration_numbers_for_cars_with_colour":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other operation without creating a parking lot\n")  # noqa
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Please enter a color to search for,Enter the color and try again\n")  # noqa
            else:
                parkinglot.regnooncolor(command[1].lower())
        print()

    # prints slots of cars with given color
    elif command[0] == "slot_numbers_for_cars_with_colour":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other operation without creating a parking lot\n")  # noqa
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Please enter a color to search for, Enter the color and try again\n")  # noqa
            else:
                parkinglot.slotoncolor(command[1].lower())
        print()

    # prints slot of cars on registration number
    elif command[0] == "slot_number_for_registration_number":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other operation without creating a parking lot\n")  # noqa
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Please enter a registration number to search for, Enter the number and try again\n")  # noqa
            else:
                parkinglot.searchonregno(command[1])
        print()

    # exits the program

    elif command[0] == "exit":
        global programOn
        print()
        print("Thank You For using our parking Lot ")
        programOn = False
        print()

    # adds extra slots to the parking lot

    elif command[0] == "addslots":
        print()
        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other operation without creating a parking lot\n")  # noqa
        else:
            if len(command) < 2 or command[1] == "" or command[1] == " ":
                print("Add slots takes integer number of slots to be added, Please enter the command correctly and try again")  # noqa
            else:
                if command[1].isdecimal():
                    parkinglot.addslot(int(command[1]))
                    print("Successfully added", command[1], "slots")
                else:
                    print("Add slots takes integer number of slots to be added, Please enter the command correctly and try again")  # noqa
        print()

    # prints instructions on console
    elif command[0] == "instructions":
        print()
        abpath = str(pathlib.Path(__file__).parent.absolute())
        filepath = abpath.replace("\\", "/") + "/"+"instructions.txt"
        file = open(filepath, "r")
        for line in file:
            print(line)
        print()

    # if user enters some unknown command
    else:
        print()
        print("The command you entered is not found , please enter the commands in our program\n Read instructions to see the commands present")  # noqa


if __name__ == "__main__":
    choosemode()
    while programOn is True:

        main(mode)
