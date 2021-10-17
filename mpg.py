# Student Name: David Van Vleet
# Course: ISQA 3900 - Web Application Development
# Date: 10/17/2021
# The purpose of this program is to assist with learning the action of reading/writing to
# python files to both store and read input that is provided by the user of the program.
# Within this program, there will be various inputs that will be needed to be provided
# by the user. Upon providing inputs there will be a form of exception handling that will
# be performed to ensure that a float value is provided by the user before continuing the
# program. This will assist in ensuring that the appropriate values are utilized when calculating
# the MPG.
# Note: Multiple values will have the ability to be accepted upon initiation of the program for as
# long as the user selects y or yes. This includes both reading trips from a file and writing new
# values to the trips.csv file.

# Imports
import csv
import numpy as np
import re

# Function that will check the input from the user for the miles_driven variable.
def check_miles_input():
    # Initialize check to True.
    check = True
    # Loop for as long as check is True.
    while check:
        # Initiate try block.
        try:
            # Get input from the user, this value will be a float value.
            miles_driven = float(input("Enter miles driven:\t\t"))
            # Initialize check to False as the input is valid.
            check = False
            # Return the miles_driven value.
            return miles_driven
        # Value exception.
        except ValueError:
            # Inform the user that the value entered is invalid.
            print("Enter numeric values only. Try again.")
# Function that will check the input from the user for the gallons_used variable.
def check_gallons_input():
    # Initialize check to True.
    check = True
    # Loop for as long as check is True.
    while check:
        # Initiate try block.
        try:
            # Get input from the user, this value will be a float value.
            gallons_used = float(input("Enter gallons of gas used:\t"))
            # Initialize check to False as the input is valid.
            check = False
            # Return the gallons_used value.
            return gallons_used
        # Value exception.
        except ValueError:
            # Inform the user that the value entered is invalid.
            print("Enter numeric values only. Try again.")
# display a title
print("The Miles Per Gallon program")
print()
# Initialize check var to True.
check = True
# Set the count var to 0.
count = 0
# Loop for as long as check is True.
while check:
    # Check if the user would like to read trips from a file.
    check_input = input("Would you like to read trips from a file? y/n ")
    # Check if the user input is any variation of y or yes.
    if check_input.lower() == 'yes' or check_input.lower() == 'y' or check_input.upper() == 'yes' or check_input.upper() == 'y':
        # Get the name of the file that the user would like to read.
        file_name = input("Enter the csv filename containing trip data: ")
        # Initiate the try block to open the file.
        try:
            # Open the file specified.
            file = open(file_name)
        # IO exception error.
        except IOError:
            # Inform the user that the file entered is not valid.
            print("Trips not read from file - file not found: ", file_name)
            # Continue the program.
            continue
        # Check to ensure the file extension ends with .csv.
        if file_name.endswith('.csv'):
            # Read the csv file.
            csvreader = csv.reader(file)
            # Initialize the separator.
            separator = ", "
            # Loop through the contents of the csv file.
            for row in csvreader:
                # Increase the count variable by 1.
                count += 1
                # Print the contents to the console.
                print('{}. Miles: {:<15} Gallons of Gas: {:<15} Mpg: {:<15}\t'.format(count, *row))
            # Close the file.
            file.close()
        else:
            # Inform the user that the file was not found.
            print("Trips not read from file - file not found: ", file_name)
    # Check if the user input matches the variations of no or n.
    elif check_input.lower() == 'no' or check_input.lower() == 'n' or check_input.upper() == 'no' or check_input.upper() == 'n':
        # Initialize the second check var to True.
        second_check = True
        # Ask the user if they would like to enter trip data.
        trip_input = input("Would you like to enter trip data? y/n ")
        # Loop for as long as second_check is True.
        while second_check:
            # Check if user input is any variation of yes or y.
            if trip_input.lower() == 'yes' or trip_input.lower() == 'y' or trip_input.upper() == 'yes' or trip_input.upper() == 'y':
                # Initialize the title.
                title = ['Miles', 'Gallons of Gas', 'MPG']
                # Get miles_driven input from the user.
                miles_driven = check_miles_input()
                # Get gallons_used input from the user.
                gallons_used = check_gallons_input()
                # calculate and round miles per gallon
                mpg = miles_driven / gallons_used
                # Round mpg.
                mpg = round(mpg, 2)
                # Initialize the data array.
                data = [miles_driven, gallons_used, mpg]
                # Open the trips.csv file and append the data into the file provided by the user input.
                with open('trips.csv', 'a', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                # display the result
                print("Miles Per Gallon:\t\t" + str(mpg))
                # Initialize the counter variable.
                counter = 0
                # Open the trips.csv file.
                trips_file = open('trips.csv')
                # Read the trips.csv file.
                csvreader = csv.reader(trips_file)
                # Initialize the separator value.
                separator = ", "
                # Loop through the csv rows.
                for row in csvreader:
                    # Increase the counter var by 1.
                    counter += 1
                    # Print the contents to the screen.
                    print('{}. Miles: {:<15} Gallons of Gas: {:<15} Mpg: {:<15}\t'.format(counter, *row))
                # Close the file.
                trips_file.close()
                # Check if the user would like to continue entering values.
                check_continue = input("Would you like to continue? y/n ")
                # Check if the value entered is any variation of yes or y to continue the program.
                if check_continue.lower() == 'yes' or check_continue.lower() == 'y' or check_continue.upper() == 'yes' or check_continue.upper() == 'y':
                    print()
                else:
                    # Inform the user that the values have been saved to trips.csv
                    print("Trips saved to file: trips.csv")
                    # Exit the program.
                    exit()
            else:
                # Inform the user that the program will exit.
                print("The MPG Calculation program will now exit!")
                # Exit the program.
                exit()
    else:
        # Inform the user that the program will exit.
        print("The MPG Calculation program will now exit!")
        # Exit the program.
        exit()
