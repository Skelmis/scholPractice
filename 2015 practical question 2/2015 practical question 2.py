inputOne = "10:9.8"#placeholder values
inputTwo = "5:4.3"

def SplitInput(input):#splits the input into the relevant format hour - minute - seconds
    splitInputOne = input.split(":")
    splitInputOneCarry = splitInputOne[1].split(".")

    finishedFirstInput = [f'{splitInputOne[0]}',f'{splitInputOneCarry[0]}',f'{splitInputOneCarry[1]}']
    return finishedFirstInput

print(SplitInput(inputTwo))
