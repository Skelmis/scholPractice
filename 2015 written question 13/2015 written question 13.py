def Reverse(s): 
    return s[::-1] 
  
def IsPalindrome(s): 
    rev = Reverse(s) 
    if s == rev: 
        return True
    return False

while True:
    correctInput = False
    while correctInput == False:
        try:
            string = str(input("Please enter the sentance to check for a palindrome: ").lower())
            correctInput = True
        except Exception as e:
            print(f"An error occured, please try again.\n{e}")

    answer = IsPalindrome(string)
    if answer == True:
        print("Yes your input is a palindrome!")
    else:
        print("Im sorry, that is not a palindrome")
