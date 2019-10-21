import time
import sys

def GetNumber():
    fraudCount = 0
    correctInput = False
    while correctInput == False:
        if fraudCount == 10:
            print("You haven't supplied a number. I am giving you the number 5")
            return 5
        try:
            number = int(input("Please enter a number between 1 & 9: "))
            if number >= 1 and number <= 9:
                correctInput = True
                return number
            else:
                fraudCount += 1
        except Exception as e:
            print(f"An error occured, please try again.\n{e}")

number = GetNumber()
print(f"Thanks for giving me the number {number}")
