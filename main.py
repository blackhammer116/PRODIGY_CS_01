alpha = {0: 'A',1: "B" ,2: "C",3: "D",4: "E",5: "F",6: "G",
         7: "H",8: "I",9: "J", 10: "K",11: "L",12: "M",
         13: "N", 14: "O", 15: "P", 16: "Q",17: "R",
         18: "S",19: "T",20: "U",21: "V",
         22: "W",23: "X",24: "Y",25: "Z"}


def encrypt(text, ShiftValue):
    text = text.replace(" ", "")
    textLetter = list(text)
    cipherTextLetter = []
    for i in textLetter:
        keys = list(alpha.values())
        j = keys.index(i.upper())
        l = (j + ShiftValue) % 26
        cipherTextLetter.append(alpha[l])

    cipherText = "".join(cipherTextLetter)
    print(cipherText)


def decrypt(text, ShiftValue):
    textLetter = list(text)
    normalTextLetter = []
    for i in textLetter:
        keys = list(alpha.values())
        j = keys.index(i.upper())
        l = (j - ShiftValue) % 26
        normalTextLetter.append(alpha[l])
    normalText = "".join(normalTextLetter)
    print(normalText)


if __name__ == "__main__":
    print("*****Welcome to Ceaser Cipher*****")
    while(1):
        print("1. Encrypt")
        print("2. Decrypt")
        choice = int(input("> "))
        if choice == 1:
            print("Enter the text you wish to encrypt")
            text = input("> ")
            ShiftValue = int(input("Your desired shift value: "))
            encrypt(text, ShiftValue)
        elif choice == 2:
            print("Enter the text you wish to decrypt")
            text = input("> ")
            ShiftValue = int(input("Your desired shift value: "))
            decrypt(text, ShiftValue)
        else:
            print("Error please choose betweeen 1 or 2")
