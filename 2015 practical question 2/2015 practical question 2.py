#Goal:
#To create a program that takes two inputs and outputs the time difference

#Ideas:
#Take input as a string, split it based on special characters into an array
#Work on each item individually to calculate differences

inputOne = "1:10.20"#placeholder values
inputTwo = "5:20.10"

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


#Getting users input split into the relevant parts
one = SplitInput(inputOne)
two = SplitInput(inputTwo)

secondDifference = GetDifference(one[2], two[2])
print(secondDifference)

mintueDifference = GetDifference(one[1], two[1])
print(mintueDifference)

hourDifference = GetDifference(one[0], two[0])
print(hourDifference)
