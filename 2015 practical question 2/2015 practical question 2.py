#Goal:
#To create a program that takes two inputs and outputs the time difference

#Ideas:
#Take input as a string, split it based on special characters into an array
#Work on each item individually to calculate differences

import time
import sys

inputOne = "10:45.37"#placeholder values
inputTwo = "12:33.10"

def SplitInput(input):#splits the input into the relevant format hour - minute - seconds
    splitInputOne = input.split(":")
    splitInputOneCarry = splitInputOne[1].split(".")

    finishedFirstInput = [f'{splitInputOne[0]}',f'{splitInputOneCarry[0]}',f'{splitInputOneCarry[1]}']
    return finishedFirstInput

def GetDifference(first, second):#Takes two ints, finds the difference between the second and first
    first = int(first)
    second = int(second)
    difference = second - first
    return difference

def SecondCarry(secondDifference, minuteDifference):
    if secondDifference < 0: #If negative number
        secondDifference += 60 #Add 60 seconds to create a positive
        minuteDifference -= 1 #Remove a minute
    return secondDifference, minuteDifference

def MinuteCarry(minuteDifference, hourDifference):
    if minuteDifference < 0: #If negative number
        minuteDifference += 60 #Add an hour to create a positive
        hourDifference -= 1 #Remove 1 hour of time because its minutes now
    return minuteDifference, hourDifference

while True:
    #Getting user input
    print("Please enter any data in the following format:\nhours:minutes.seconds")
    correctInput = False
    while correctInput == False:
        try:
            inputOne = str(input("Please enter the start time: "))
            correctInput = True
        except Exception as e:
            print(f"An error occured, please try again.\n{e}")

    correctInput = False
    while correctInput == False:
        try:
            inputTwo = str(input("Please enter the finish time: "))
            correctInput = True
        except Exception as e:
            print(f"An error occured, please try again.\n{e}")

    #Getting users input split into the relevant parts
    one = SplitInput(inputOne)
    two = SplitInput(inputTwo)
    if int(one[1]) < 0 or int(one[1]) > 60 or int(one[2]) < 0 or int(one[2]) > 60 or int(two[1]) < 0 or int(two[1]) > 60 or int(two[2]) < 0 or int(two[2]) > 60:
        print("Invalid input detected. Please try again")
        break

    secondDifference = GetDifference(one[2], two[2])
    minuteDifference = GetDifference(one[1], two[1])
    hourDifference = GetDifference(one[0], two[0])

    secondDifference = int(secondDifference)
    minuteDifference = int(minuteDifference)
    hourDifference = int(hourDifference)
    #Checking to see if the person start before they began
    if hourDifference < 0:
        print("It appears you finished before you started")
        time.sleep(5)
        sys.exit()

    #Start figuring out if time needs carrying over
    minuteDifference, hourDifference = MinuteCarry(minuteDifference, hourDifference)
    secondDifference, minuteDifference = SecondCarry(secondDifference, minuteDifference)

    print(f"\nTime Taken was:\n{hourDifference}:{minuteDifference}.{secondDifference}\n")
