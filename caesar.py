import re

# Create caesar cipher method
def caesar(n, stringly):
    last = ""
    try:
        n = int(n)
        temp = len(stringly)
        re.sub('[^A-Za-z]', '', stringly)
        if len(stringly) < temp:
            print("Some non-alphabetic characters were removed during conversion")
        stringly.casefold()
        for i in stringly:
            a = (ord(i) % 96 + n) % 26 + 96
            last += chr(a)
    except ValueError:
        print("Rot must be int")
    return last

print(caesar(input("Enter rotation: "), input("Enter word: ")))

