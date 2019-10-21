correctInput = False
while correctInput == False:
    try:
        numberRange = int(input("Please enter the number range: ")) + 1
        correctInput = True
    except Exception as e:
        print(f"An error occured, please try again.\n{e}")
        
totalNumber = 0
for i in range(numberRange):
    print(f"Iteration: {i}")
    currentCalc = i * i
    print(i*i)
    print(f"{totalNumber} : {currentCalc}")
    totalNumber += currentCalc
    print(totalNumber)

print(f"Your end number is {totalNumber}")
