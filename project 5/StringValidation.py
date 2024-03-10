
class ValidateString:
   
    def validateNumericInput(userInput): #this function is designed to be certain that any given value from an input command can be turned into an int value.
        validString = 0 # a value of zero means the input cannot be turned into an int string. a value of one means it can. we start at zero, and alter it if the loop finishes.
        uniqueIntegerList = [] #an empty list. the method fills the rest with string versions of all unique digits in the decimal system
        index = 0 # an index value utilized in the while loop below
        for integer in range(10):
            uniqueIntegerList.append(str(integer)) #creates a list containing integers from 0-9 to check the user's numeric inputs.

        while index < len(userInput): #this loop checks if there are any values that are not string variants of a given int number.
            if userInput[index] in uniqueIntegerList:
                index += 1
            else: # ends the loop and determines that the string cannot be translated
                break
        else: #if the while loop finishes naturally, the value is updated.
            validString += 1
        return validString #gives a truth value so that the code knows that the string is valid.

    def validateYes(userInput): #checks the string to see if the user is inputting yes or any variant of it.
        yesList = ["Y", "y", "E","e", "S", "s"] #a list of the different capitalizations is made to catch the possibility.
        validCount = 0 #a variable to check how many characters from the input are in the validlist
        yesResponse = 0 #the value determining if the user is inputting yes.
        for character in userInput: #this loop checks all characters of the input, and sees if the characters given are in the list.
            if character in yesList:
                validCount += 1
            else:
                validCount = validCount
        if validCount == len(userInput): #finalizes that the user meant to say yes by comparing the validated characters to the length of the input string
            yesResponse += 1
        else:
            yesResponse += 0
        return yesResponse #gives the valie to any assigned variable, telling whether or not the input was yes or not.

    def validateNo(userInput): #Identical to validate yes, the only difference is that it's designed around the user saying no.
        noList = ["N", "n", "O", "o"]
        validCount = 0
        noResponse = 0
        for character in userInput:
            if character in noList:
                validCount += 1
            else:
                validCount = validCount
        if validCount == len(userInput):
            noResponse += 1
        else:
            noResponse += 0
        return noResponse
