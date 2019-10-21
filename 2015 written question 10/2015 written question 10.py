def DrawByLine():
    correctInput = False
    while correctInput == False:
        try:
            numberRange = int(input("Please enter the number range: "))
            correctInput = True
        except Exception as e:
            print(f"An error occured, please try again.\n{e}")
    char = "*"
    space = " "


    for i in range(numberRange):
        output = None
        if i < 2: #If I is less then 2
            stars = i + 1
            for x in range(stars):
                if not output:
                    output = char
                else:
                    output = output + char
        elif i >= 2 and i < (numberRange - 1): #If I is more than/equal to 2 but less than the max number
            output = char
            for x in range((i - 1)):
                output = output + space
            output = output + char
        elif i >= 2 and i == (numberRange - 1): #If I is more than 2 and equals the numberinputted
            stars = i + 1
            for x in range(stars):
                if not output:
                    output = char
                else:
                    output = output + char
        print(output)

def DrawAtOnce():
    correctInput = False
    while correctInput == False:
        try:
            numberRange = int(input("Please enter the number range: ")) 
            correctInput = True
        except Exception as e:
            print(f"An error occured, please try again.\n{e}")
    char = "*"
    space = " "
    output = None


    for i in range(numberRange):
        if i < 2: #If I is less then 2
            stars = i + 1
            for x in range(stars):
                if not output:
                    output = char
                else:
                    output = output + char
            output = output + "\n"
        elif i >= 2 and i < (numberRange - 1): #If I is more than/equal to 2 but less than the max number
            output = output + char
            for x in range((i - 1)):
                output = output + space
            output = output + char
            output = output + "\n"
        elif i >= 2 and i == (numberRange - 1): #If I is more than 2 and equals the numberinputted
            stars = i + 1
            for x in range(stars):
                if not output:
                    output = char
                else:
                    output = output + char
            output = output + "\n"
    print(output)

while True:
    correctInput = False
    while correctInput == False:
        try:
            type = str(input("Please choice a drawing method. \nEither per line or all at once. \nFailure to choice will result in the default action being taken: "))
            correctInput = True
        except Exception as e:
            print(f"An error occured, please try again.\n{e}")
    if "line" in type.lower():
        DrawByLine()
    else:
        DrawAtOnce()
