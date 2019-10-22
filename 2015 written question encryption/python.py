import random

cipher = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(cipher)
print(alphabet)
print(cipher)

#The idea being that alphabet[x] is given the value of keyOne[x]
keyOne = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
pairedArray = []

for i in range(27):
    item = keyOne[i],cipher[i],alphabet[i]
    pairedArray.append(item)

for i in range(27):
    print(f"Index Number: {pairedArray[i][0]}\nLetter Input: {pairedArray[i][1]}\nLetter Output: {pairedArray[i][2]}\n-----")

clearText = "ahaha fuck school"
cipherText = None

#Encrypt the text
for i in range(len(clearText)):
    for x in range(27):
        if clearText[i] == pairedArray[x][1]:
            if not cipherText:
                cipherText = pairedArray[x][2]
            else:
                cipherText = cipherText + pairedArray[x][2]
print(f"Input Text: {clearText}\nEncrypted Text: {cipherText}")


#decrypt the text
decryptedText = None
for i in range(len(clearText)):
    for x in range(27):
        if cipherText[i] == pairedArray[x][2]:
            if not decryptedText:
                decryptedText = pairedArray[x][1]
            else:
                decryptedText = decryptedText + pairedArray[x][1]
print(f"Decrypted Text: {decryptedText}")
