"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Milan Musil
email: musil.e@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#+------+-------------+
#| user |   password  |
#+------+-------------+
#| bob  |     123     |
#| ann  |   pass123   |
#| mike | password123 |
#| liz  |   pass123   |
#+------+-------------+

login = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

username = input("username: ")
password = input("password: ")

if login[username] == password:
    print("-" * 40)
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
    number = input("Enter a number btw. 1 and 3 to select: ")
    
    #if the variable "number" is not numeric, program termination
    if not number.isnumeric():
        print("username:", username)
        print("password:", password)
        print("invalid character, terminating the program..")
        exit()
    #if variable "number" is not in the range 1-3, terminate program
    elif not int(number) in range(1, 4):
        print("username:", username)
        print("password:", password)
        print("invalid character, terminating the program..")
        exit()
    #if the conditions are met, process the text
    else:
        text = (TEXTS[int(number) - 1].replace("\n","").replace(",","").replace(".","").split(" "))
        countOfWords = 0
        countOfWordsFrstUpp = 0
        countOfWordsUpp = 0
        countOfWordsLow = 0
        countOfNumbers = 0
        sumOfNumbers = 0
        numberChar1 = 0
        numberChar2 = 0
        numberChar3 = 0
        numberChar4 = 0
        numberChar5 = 0
        numberChar6 = 0
        numberChar7 = 0
        numberChar8 = 0
        numberChar9 = 0
        numberChar10 = 0
        numberChar11 = 0
        numberChar12 = 0
        numberChar13 = 0
        numberChar14 = 0
        numberChar15 = 0
        for word in text:
            if not word == '':
                if len(word) == 1:
                    numberChar1 = numberChar1 +1
                if len(word) == 2:
                    numberChar2 = numberChar2 +1
                if len(word) == 3:
                    numberChar3 = numberChar3 +1
                if len(word) == 4:
                    numberChar4 = numberChar4 +1
                if len(word) == 5:
                    numberChar5 = numberChar5 +1
                if len(word) == 6:
                    numberChar6 = numberChar6 +1
                if len(word) == 7:
                    numberChar7 = numberChar7 +1
                if len(word) == 8:
                    numberChar8 = numberChar8 +1
                if len(word) == 9:
                    numberChar9 = numberChar9 +1
                if len(word) == 10:
                    numberChar10 = numberChar10 +1
                if len(word) == 11:
                    numberChar11 = numberChar11 +1
                if len(word) == 12:
                    numberChar12 = numberChar12 +1
                if len(word) == 13:
                    numberChar13 = numberChar13 +1
                if len(word) == 14:
                    numberChar14 = numberChar14 +1
                if len(word) == 15:
                    numberChar15 = numberChar15 +1
                
                countOfWords = countOfWords + 1
                if word.isnumeric():
                    countOfNumbers = countOfNumbers + 1
                    sumOfNumbers = sumOfNumbers + int(word)
                elif word == word.title():
                    countOfWordsFrstUpp = countOfWordsFrstUpp + 1
                elif word == word.upper():
                    countOfWordsUpp = countOfWordsUpp + 1
                elif word == word.lower():
                    countOfWordsLow = countOfWordsLow + 1

        print("-" * 40)
        print("There are", countOfWords, "words in the selected text.")
        print("There are", countOfWordsFrstUpp, "titlecase words.")
        print("There are", countOfWordsUpp, "uppercase words.")
        print("There are", countOfWordsLow, "lowercase words.")
        print("There are", countOfNumbers, "numeric strings.")
        print("The sum of all the numbers", sumOfNumbers)
        print("-" * 40)
        print("LEN|  OCCURENCES  |NR.")
        print("-" * 40)
        print(" 1 |", "*" * numberChar1, numberChar1)
        print(" 2 |", "*" * numberChar2, numberChar2)
        print(" 3 |", "*" * numberChar3, numberChar3)
        print(" 4 |", "*" * numberChar4, numberChar4)
        print(" 5 |", "*" * numberChar5, numberChar5)
        print(" 6 |", "*" * numberChar6, numberChar6)
        print(" 7 |", "*" * numberChar7, numberChar7)
        print(" 8 |", "*" * numberChar8, numberChar8)
        print(" 9 |", "*" * numberChar9, numberChar9)
        print("10 |", "*" * numberChar10, numberChar10)
        print("11 |", "*" * numberChar11, numberChar11)
        print("12 |", "*" * numberChar12, numberChar12)
        print("13 |", "*" * numberChar13, numberChar13)
        print("14 |", "*" * numberChar14, numberChar14)
        print("15 |", "*" * numberChar15, numberChar15)
else:
    print("username:", username)
    print("password:", password)
    print("unregistered user, terminating the program..")
    exit()
    