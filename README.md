PARKING LOT

Description: An Console based app to handle incoming, exiting, grouping of cars in a linear parking lot with fixed slots

External packages used is null.

The code is completely written in a modular way which is easily customisable

The code follows the rules and style guide under PEP-8 and flake8 linter rules

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

Running the app:

To run the app, just open the main.py file on a console like Command Prompt

Instructions and commands used by the program are as follows:

    1.  To create a parking lot, "create_parking_lot <size of lot>"
        example : create_parking_lot 7

        Note: Following commands will not work if there is no parking lot, so always create a parking lot first

    2.  To park a vehicle, "park <registration number in format> <color>"
        example : park KA-01-HH-1234 red

    3.  To check status of the parking lot "status"

    4.  To remove a car from a slot, "leave <slot number>"
        example : leave 4

    5.  To get cars of a given color, "registration_numbers_for_cars_with_colour <color>"
        example : registration_numbers_for_cars_with_colour red

    6.  To get slot number of cars with given color, "slot_numbers_for_cars_with_colour <color>"
        example : slot_numbers_for_cars_with_colour black

    7.  To search slot number of a car on registration number, "slot_number_for_registration_number <registration number>"
        example : slot_number_for_registration_number MH-04-AY-1111

    8. To add extra slots to parking lot, "addslots <number of slots to add>"
        example : addslots 4

    9.  To end the program, "exit"

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
Note:

    In READ COMMANDS FROM A FILE MODE, please make sure the file containing commands has the following conditions satisfied

        CURRENLTY THE APP SUPPORTS ONLY .txt files

        a) It has to be in the same directory as main.py file
        b) Please do write an "exit" command at the end of the file to exit the execution and avoid crashing of your application
        c) Make sure you write the file name correctly while typing when prompted, extension of the file included.
            example : command.txt

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

Extra features:

    1. User can increase the size of the parking lot after creating the parking lot
    2. This has a special check for format of registration numbers provided by user. If the reg no is not in given format, the program throws an error
    3. Program is pretty self explanatory, User can read insturction on the program anytime
