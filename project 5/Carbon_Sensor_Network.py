"""This program is a simulation for a sensor network to measure Carbon dioxide levels to improve ventilation.
This code was Written By Pranay Mohla.
"""
import StringValidation #importing an additional module I created to help check inputs made by the user. makes this file easier to read by using.
import random #Importing the random module to help us randomly generate our values for sensor position.

val = StringValidation.ValidateString #a shortcut variable I created to type less to refer to the function/module I created for assistance.

def sensorCreation(sensorAmount): #this function creates our sensor objects.
    """This Function creates the sensors requested by the user."""
    sensors = []        
    compatable = val.validateNumericInput(sensorAmount) #sends the input value up to the validateNumericalInput method to see if it can be used.
    while compatable != 1 or int(sensorAmount) <= 0: #checks to see if the string given is valid or is a non-zero number.
        print("Incorrect Entry! Please Try again.")
        sensorAmount = input("PlEnter the number of Sensors deplyoed across sheridan Campus")
        compatable = val.validateNumericInput(sensorAmount)
    else: #if the loop finishes, then a list of all sensors are created. their co-ordinates are added in sensorLocation.
        for sensor in range(int(sensorAmount)):
            sensors.append([])
    return sensors 

def sensorLocation(sensors): #this function assigns our sensors their positions.
    """This function randomly generates the location of every sensor."""
    locations = [] # a list we create to store our location values.
    locationIndex = 0 #a variable to help us keep track of what we're putting INTO each sensor.
    for sensor in range((len(sensors)*2)): #the condition tells us how many numbers we need to create to assign to a 
        coordinate = random.randint(0, 100) + (random.randint(0, 100)/100) #lets us create floats, as there is no random method for floats.
        if coordinate in locations: #checks to see if the generate coordinate value already exists in our locations list. if it does, it is discarded and a new one is created.
            continue
        else: #if the created coordinate is unique from the ones in the list.
            locations.append(coordinate) #add the numbers to the total.
    for sensor in sensors: #this loop looks at every list possible and appends values to it from our "locations" list.
        sensor.append(locations[locationIndex])
        sensor.append(locations[locationIndex + 1])
        locationIndex += 2
    return sensors #returns the created sensors, with their locations assigned.

def dayAmount(sensors): #this function asks the user to give them a number of days, and sends it to the readingAverage function, for every sensor we have.
    """This function receives how many days we are reading for each sensor."""
    sensorID = 0 #the variable helps us format the string displaying which sensor we are working with.
    for sensor in sensors: #the first loop activates, having the code run for every sensor we're created.
        print('')
        print('')  #while largely uneeded, the double prints are to match the formatting requirements for the assignment.
        print("This is for Sensor ", sensorID + 1, " at position ", sensor) #this print shows which sensor we are performing the task for.
        
        dayCount = input("Enter the number of days for the readings: ") #prompts a user for an input
        compatable = val.validateNumericInput(dayCount) #sends the input to the checker and recieves the validation results.
        while compatable != 1 or int(dayCount) <= 0: #runs if the checker returns false, and loops until a valid input is made.
            print("Incorrect Entry! Please try again!")
            dayCount = input("Enter the number of days for the readings: ")
            compatable = val.validateNumericInput(dayCount)
        else: #when the loop finishes, the input is convered to an int and sent to the readingCollection function
            readingCollection(int(dayCount))
        sensorID += 1 #updates the sensorID

def readingCollection(dayCount): #this function collects all given readings into a list, and keeps track of how many days go by.
    """This function collects the days that pass and their readings on the sensor that day."""
    readings = [] #creates an empty list, and empties it when a new sensor is being measured.
    daysPassed = 0 #creates a variable tied to the days that have passed, and resets upon the function being re-ran
    for day in range(dayCount): 
        dayNumber = "Enter the CO2 For Day " + str(day + 1) + ": " #a vairable created to help format the string for the user to keep track of the day number.
        carbonReading = input(dayNumber) #asks user for an input
        compatable = val.validateNumericInput(carbonReading) #sends the input through to the checker to see if it is a valid input.
        while compatable != 1 or int(carbonReading) <= 0: #if the input given is invalid, a new one is requested and then sent to the checker.
            print("Incorrect Entry! Please try again")
            carbonReading = input(dayNumber)
            compatable = val.validateNumericInput(carbonReading)
        else: #when the validation loop finishes/never runs, the daysPassed variable and readings list are updated.
            readings.append(int(carbonReading))
            daysPassed += 1
    readingAverage(readings, daysPassed) #when the for loop finishes, it sends the variables we kept track of into the function to calculate the average.

def readingAverage(readingList, readingDays): #calculates the average PPM for the input CO2 levels, and prints it.
    """this function returns the sum of the carbon levels given and takes the average."""
    readingTotal = 0 #a variable is created to add together all values of the values stored in the list from readingCollection
    for i in readingList: #goes through the list and adds all values to the new variable.
        readingTotal += i
    print("Rounded Average Readings ", (readingTotal / readingDays)) #returns the value in string format, dividing the total sum by the days that passed.

def repeatProgram(): #this function asks for an input of yes or no to repeat the program again, and updates the values determining the loop making the program run.
    """This function determines if the user wants to keep using the program."""
    repeat = input("Do you want to continue: (Y)es or (N)o: ")
    userRepeat = val.validateYes(repeat) #the program sends the input over to the module helper to see if it is a yes
    userEnd = val.validateNo(repeat) #the program sends the input over to the module helper to see if it is a no.
    while (userRepeat !=1) and (userEnd != 1): #if the checkers finds that the statement is neither a yes or a no, it asks for another input, and runs it throught he checkers 
        print("Invalid Entry! Please Try again")
        repeat = input("Do you want to continue: (Y)es or (N)o: ")
        userRepeat = val.validateYes(repeat)
        userEnd = val.validateNo(repeat)
    else: #when the loop ends/never starts, then the program looks at the given truth values is greater, and returns 1 or 0 depending on which is greater.
        if userRepeat > userEnd: #since our truth values are determined as ones and zeroes, this will only run if one is true and the other isnt
            return 1 #1 is what we have chosen to loop the program. a zero will cause it to stop.
        else: #runs if userEnd is greater than userRepeat
            return 0

continueProgram = 1 #keeps the loop below going until the users wants to turn it off.
while continueProgram != 0: #repeats the program until the user does not want it to loop.
    firstInput = input("Enter the number of sensors deployed across Sheridan Campus: ") #begins the program by asking for input.
    sensors = sensorCreation(firstInput) #the input given is run through the creation program, and the sensors are returned with no location
    sensorLocation(sensors) #the sensors, created successfully are run through the code and are assigned locations.
    dayAmount(sensors) #the sensors, fully created, are then run through this function to get each assigned readings.
    continueProgram = repeatProgram() #changes the input in case the user wants to end the program.
else: #if the user ends the program, a string is returned, and the program stops running.
    print("Exiting the Program......")