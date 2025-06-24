"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Milan Musil
email: musil.e@seznam.cz
"""

import re

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

if login.get(username) == password:
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
        #processing input text using first 4 lessons, failed on first project submission
        #text = (TEXTS[int(number) - 1].replace("\n","").replace(",","").replace(".","").split(" "))
        
        #recommended use of regular expressions
        #text = re.sub(r'\.\,\n','', TEXTS[int(number) - 1]).split(' ')
        text = TEXTS[int(number) - 1]
        text = re.sub(r"\s+", " ", text)
        text = text.strip()
        regex = re.compile(r"[^a-zA-Z0-9 ]+")
        textWithoutSpecChar = regex.sub("", text)
        text = re.split(r"\s+", textWithoutSpecChar)

        print("-" * 40)
        
        lenWord = dict()
        countOfWords = 0
        countOfWordsFrstUpp = 0
        countOfWordsUpp = 0
        countOfWordsLow = 0
        countOfNumbers = 0
        sumOfNumbers = 0
        for word in text:
            if len(word) > 0:
                lenWord[len(word)] = lenWord.get(len(word),0) + 1 
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

        print("There are", countOfWords, "words in the selected text.")
        print("There are", countOfWordsFrstUpp, "titlecase words.")
        print("There are", countOfWordsUpp, "uppercase words.")
        print("There are", countOfWordsLow, "lowercase words.")
        print("There are", countOfNumbers, "numeric strings.")
        print("The sum of all the numbers", sumOfNumbers)
        
        print("-" * 40)
        print("LEN|  OCCURENCES  |NR.")
        print("-" * 40)
        
        for numberOfChar in range(1,countOfWords+1):
            valueNumberOfChar = lenWord.get(numberOfChar, 0)
            if numberOfChar < 10:
                print("", numberOfChar, "|", "*" * valueNumberOfChar, valueNumberOfChar)
            else:
                print(numberOfChar, "|", "*" * valueNumberOfChar, valueNumberOfChar)
            if lenWord.get(numberOfChar) != None:
                lenWord.pop(numberOfChar)
            if len(lenWord) == 0:
                break
        
else:
    print("username:", username)
    print("password:", password)
    print("unregistered user, terminating the program..")
    exit()
    