MAX_VALUE = 26
def getMode():
    while True:
        print("Encrypt, Decrypt, or Attack?")
        mode = input().lower()
        if mode in 'encrypt decrypt attack'.split():
            return mode
        else:
            print("Invalid Input")
def getText():
    print("Entert text, please.")
    return input()
def getKey():
    key = 0
    while True:
        print("Enter key")
        key = int(input())
        if key > 26:
            key = key % MAX_VALUE
        return key
def execute(mode, text, key):
    if mode[0] == 'd':
        key = -key
    transText = ''
    for symbol in text:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num +=26
            transText += chr(num)
        else:
            transText +=symbol
    return transText

mode = getMode()
text = getText()
if mode[0] == 'a':
    key = 0
    for key in range(0,26):
        print(execute(mode, text, key))
else:
    key = getKey()
    print(execute(mode, text, key))