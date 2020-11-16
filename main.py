import pathlib


# welcome screen

print("\n\nWELCOME TO OUR PARKING LOT \n\n")
print("(If you want to see the commands to use the lot \
then type 'instructions' and press ENTER)\n\n")
print("Please choose a mode\n")


def choosemode():
    global mode
    print("Press 1 and ENTER if you want to go with INTERACTIVE MODE")

    print("Press 2 and ENTER if you want to READ INPUT FROM A FILE")
    modeinput = input()
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
    initiated = False

    def __init__(self, regNo, color):
        self.regNo = regNo
        self.color = color
        self.initiated = True


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
                return
        else:
            print("Parking Lot is full, No space to park")

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
            self.lot[slot-1] = 0
            self.colorbasedsort[currentcar.color].remove(currentcar.regNo)
            print("Slot no", slot, "is now free")
        else:
            print("Slot is already empty, there is no car at this spot")

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

    def status(self):
        for i in range(len(self.lot)):
            if self.lot[i] != 0:
                print("SLOT NO.", i+1, "has a",
                      self.lot[i].color.upper(),
                      "car with REG NO.", self.lot[i].regNo)
            else:
                print("SLOT NO.", i+1, "is empty")


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
        filename = input("Enter file name: ")
        abpath = str(pathlib.Path(__file__).parent.absolute())
        filepath = abpath.replace("\\", "/") + "/"+filename
        file = open(filepath, "r")
        if file:

            for line in file:

                command = line.rstrip()
                commandsplit = command.split(" ")
                inputcommand(commandsplit)
        else:
            print("File not found")
            choosemode()


def inputcommand(command):
    # declaring the parking lot variable used globally
    global parkinglot

    # Prompts user to enter some command if the user leaves the console empty
    if command[0] == "":
        print()
        print("Please enter some command, View Instructions to\
check the commands that are supported\n")

    # this runs if user inputs for creating a parking lot
    elif command[0] == "create_parking_lot":
        print()
        # checks if there exists a parking lot already,\
        #  if yes then will prompt user to not go ahead
        if parkinglot is not None:
            print(
                "There already exists a parking lot, doing this will erase all \
data on current lot\nPlease exit this program\
and restart to create a new one")
            print()
        # checking if the size field is empty
        else:
            # checks if the user has entered all the parameters
            if len(command) < 2 or command[1] == "":
                print("You have not entered a size for our parking lot, If \
you hit enter a default lot with size 6 will be created\n \
OR type the size you want and hit enter to \
create a lot with desried size\n")
                print("Waiting for your Response")
                response = input()
                # if user doesnt enter any size,\
                #  a default lot with size 6 is created
                if response == "":
                    parkinglot = ParkingLot()
                    print("Paking Lot with size 6 has been created\n ")
                # if user enters a size the lot is created
                elif type(response) == int:
                    parkinglot = ParkingLot(int(response))
                    print("Paking Lot with size",
                          response, "has been created\n ")

                else:
                    print(
                        "Seems like you have not entered a correct format of size\
, Please use whole integers as size. TRY AGAIN\n")
            # if user enters all fields correctly then lot is created
            elif type(int(command[1])) == int:
                parkinglot = ParkingLot(int(command[1]))

                print("Paking Lot with size", command[1], "has been created\n")
            # if user still enters wrong commands then\
            #  he will be prompted to try again
            else:
                print(
                    "Looks like you have entered wrong format for size of parking \
lot, please enter a whole integer and try again")
        print()

    # command to park the car
    elif command[0] == "park":
        print()
        # checks if a parking lot exists or not
        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any \
other operation without creating a parking lot\n")
        else:
            # checks if command has all arguments
            if len(command) < 3:
                print(
                    "Park Command requires you to put Registration number and \
color of the car,\n Please Enter them and TRY AGAIN")

            else:
                if command[2] == "":
                    print(
                        "Not entered a color for you car, \
Please enter a color and TRY AGAIN")
                else:
                    car = Car(command[1], command[2].lower())
                    parkinglot.park(car)
        print()

    # command to leave or empty a slot
    elif command[0] == "leave":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other\
operation without creating a parking lot\n")
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Leave command takes a slot number, Please\
enter slot number and try again")
            else:
                if type(int(command[1])) == int:
                    parkinglot.takeout(int(command[1]))
                else:
                    print("The slot number should be an \
integer, Please Try again")

        print()

    # prints a status of the lot
    elif command[0] == "status":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other \
operation without creating a parking lot\n")
        else:
            parkinglot.status()

        print()

    # prints reg no of cars with given color
    elif command[0] == "registration_numbers_for_cars_with_colour":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other \
operation without creating a parking lot\n")
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Please enter a color to search for,\
Enter the color and try again\n")
            else:
                parkinglot.regnooncolor(command[1].lower())
        print()

    # prints slots of cars with given color
    elif command[0] == "slot_numbers_for_cars_with_colour":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any \
other operation without creating a parking lot\n")
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Please enter a color to search for, \
Enter the color and try again\n")
            else:
                parkinglot.slotoncolor(command[1].lower())
        print()

    # prints slot of cars on registration number
    elif command[0] == "slot_number_for_registration_number":
        print()

        if parkinglot is None:
            print(
                "There is no Parking Lot, Cannot perform any other \
operation without creating a parking lot\n")
        else:
            if len(command) < 2 or command[1] == "":
                print(
                    "Please enter a color to search for, \
Enter the color and try again\n")
            else:
                parkinglot.searchonregno(command[1])
        print()

    elif command[0] == "exit":
        global programOn
        print()
        print("Thank You For using our parking Lot ")
        programOn = False
        print()

        # if user enters some unknown command
    else:
        print()
        print("The command you entered is not found , please enter \
the commands in our program\n Read \
instructions to see the commands present")


# insturctions for using our program

def instructions():

    print()
    print("FOLLOWING ARE THE COMMANDS OFFERED BY OUR PROGRAM")


if __name__ == "__main__":
    choosemode()
    while programOn is True:

        main(mode)
