# This work by Koviubi56 is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/
# For help: https://github.com/koviubi56/python-captcha/wiki
import random


def math(maxnum):
    mathFirst = random.randrange(1, maxnum)
    mathSecond = random.randrange(1, maxnum)
    mathAdd = random.choice(["+", " add ", " plus "])
    try:
        mathUser = int(input("What is " + str(mathFirst) +
                             mathAdd + str(mathSecond) + ">"))
    except ValueError:
        print("[ERROR]")
        print("ValueError")
        print("You needed to write an (int) number!")
        input("Press enter to continue!")
        input("We will send False to the program, so we say \"The captcha was didn't completed successfully.\" Press enter to confirm!")
        return False
    return mathUser == mathFirst + mathSecond


def text():
    textText = str(random.randrange(
        1, 999)*random.randrange(1, 999) + 11)
    textUser = input("Write " + str(textText) + ">")
    return textText == textUser


def animal():
    animals = ["Elephat", "Tiger", "Snake", "CRAB", "BIRD", "spider", "Cow", "sheep", "COW",
               "Dog", "CAT", "BEE", "PIG", "owl", "monkey", "T-Rex", "Giraffe", "Goat", "FOX", "bear"]
    colors = ["RED", "Orange", "yellow", "Chartreuse", "green",
              "Spring", "cyan", "azure", "BLUE", "Violet", "magenta", "Rose"]
    animalAnimal = random.choice(animals)
    animalColor = random.choice(colors)
    animalName = random.choice(
        ["k6r+A87Rzp3mJKDDnjhpzQ==", "o6zbD1J+cb+omtrcULg8hw=="])
    if animalName == "o6zbD1J+cb+omtrcULg8hw==":
        animalUser = input("If the " + animalAnimal + " is " +
                           animalColor + ", what color is it (case-sensitive)>")
        return animalUser == animalColor
    else:
        animalUser = input("If the " + animalAnimal + " is " +
                           animalColor + ", what animal is it (case-sensitive)>")
        return animalUser == animalAnimal


def lastword():
    animals = ["Elephat", "Tiger", "Snake", "CRAB", "BIRD", "spider", "Cow", "sheep", "COW",
               "Dog", "CAT", "BEE", "PIG", "owl", "monkey", "T-Rex", "Giraffe", "Goat", "FOX", "bear"]
    colors = ["RED", "Orange", "yellow", "Chartreuse", "green",
              "Spring", "cyan", "azure", "BLUE", "Violet", "magenta", "Rose"]
    mix = animals + colors
    lastwords = [random.choice(mix), random.choice(
        mix), random.choice(mix)]
    lastwordQ = random.choice(["list", "series"])
    lastwordWhat = random.choice(["06zNSgCAITUEurlPewn5tw==",
                                  "5OAYoY++S8oFDXL15oDlmw==", "mwf+NAMaRDt/WGB3k75rPQ=="])
    if lastwordWhat == "06zNSgCAITUEurlPewn5tw==":
        lastwordUser = input(
            "Write the second word from this " + lastwordQ + ": " + str(lastwords) + " (case-sensitive)>")
        return lastwordUser == lastwords[1]
    elif lastwordWhat == "5OAYoY++S8oFDXL15oDlmw==":
        lastwordUser = input(
            "Write the third word from this " + lastwordQ + ": " + str(lastwords) + " (case-sensitive)>")
        return lastwordUser == lastwords[2]
    elif lastwordWhat == "mwf+NAMaRDt/WGB3k75rPQ==":
        lastwordUser = input(
            "Write the first word from this " + lastwordQ + ": " + str(lastwords) + " (case-sensitive)>")
        return lastwordUser == lastwords[0]
    else:
        return False


def digit():
    digitDigit = random.randrange(4, 10)
    digitNumber = random.randrange(1000000000, 10000000000)
    digitWhat = random.choice(
        ["I4sZv95d/efwlH55KJZavQ==", "mXYMEkTnMfK9nqShwT8x+A=="])
    digitList = [int(digitInAnsware) for digitInAnsware in str(digitNumber)]
    digitInAnsware = ""
    try:
        if digitWhat == "mXYMEkTnMfK9nqShwT8x+A==":
            digitUser = int(input("In the number " + str(digitNumber) +
                                  ", what is the " + str(digitDigit) + "th digit>"))
        elif digitWhat == "I4sZv95d/efwlH55KJZavQ==":
            digitUser = int(input("Which digit is " + str(digitDigit) +
                                  "th in the number " + str(digitNumber) + ">"))
    except ValueError:
        print("[ERROR]")
        print("ValueError")
        print("You needed to write an (int) number!")
        input("Press enter to continue!")
        input("We will send False to the program, so we say \"The captcha was didn't completed successfully.\" Press enter to confirm!")
        return False
    return digitUser == digitList[digitDigit - 1]


def biggest():
    biggestFirst = ""
    biggestSecond = ""
    biggestWhat = random.choice(
        ["0cnc8J4Ksbz1pEikjWs1aA==", "DaInXmBOU3b7FMkAOIX61A==", "taE5qLWOMH5XlUqWZdI+8Q=="])
    while biggestFirst == biggestSecond:
        biggestFirst = int(random.randrange(1, 100))
        biggestSecond = int(random.randrange(1, 100))
    try:
        if biggestWhat == "DaInXmBOU3b7FMkAOIX61A==":
            biggestUser = int(input(str(biggestFirst) + " or " +
                                    str(biggestSecond) + ": which of these is the largest>"))
        elif biggestWhat == "0cnc8J4Ksbz1pEikjWs1aA==":
            biggestUser = int(input(str(biggestFirst) + " or " +
                                    str(biggestSecond) + ": which of these is the biggest>"))
        elif biggestWhat == "taE5qLWOMH5XlUqWZdI+8Q==":
            biggestUser = int(input(str(biggestFirst) + " or " +
                                    str(biggestSecond) + ": which of these is the highest>"))
        else:
            return False
    except ValueError:
        print("[ERROR]")
        print("ValueError")
        print("You needed to write an (int) number!")
        input("Press enter to continue!")
        input("We will send False to the program, so we say \"The captcha was didn't completed successfully.\" Press enter to confirm!")
        return False
    return (
        biggestUser == biggestFirst
        and biggestFirst > biggestSecond
        or biggestUser != biggestFirst
        and biggestUser == biggestSecond
        and biggestFirst < biggestSecond
    )


def smallest():
    smallestFirst = ""
    smallestSecond = ""
    smallestWhat = random.choice(
        ["0cnc8J4Ksbz1pEikjWs1aA==", "DaInXmBOU3b7FMkAOIX61A==", "taE5qLWOMH5XlUqWZdI+8Q=="])
    while smallestFirst == smallestSecond:
        smallestFirst = int(random.randrange(1, 100))
        smallestSecond = int(random.randrange(1, 100))
    try:
        if smallestWhat == "DaInXmBOU3b7FMkAOIX61A==":
            smallestUser = int(input(str(smallestFirst) + " or " +
                                     str(smallestSecond) + ": which of these is the tiniest>"))
        elif smallestWhat == "0cnc8J4Ksbz1pEikjWs1aA==":
            smallestUser = int(input(str(smallestFirst) + " or " +
                                     str(smallestSecond) + ": which of these is the smallest>"))
        elif smallestWhat == "taE5qLWOMH5XlUqWZdI+8Q==":
            smallestUser = int(input(str(smallestFirst) + " or " +
                                     str(smallestSecond) + ": which of these is the lowest>"))
        else:
            return False
    except ValueError:
        print("[ERROR]")
        print("ValueError")
        print("You needed to write an (int) number!")
        input("Press enter to continue!")
        input("We will send False to the program, so we say \"The captcha was didn't completed successfully.\" Press enter to confirm!")
        return False
    return (
        smallestUser == smallestFirst
        and smallestFirst < smallestSecond
        or smallestUser != smallestFirst
        and smallestUser == smallestSecond
        and smallestFirst > smallestSecond
    )


def name():
    nameName = random.choice(["John", "Robert", "Michael", "William",
                              "David", "Richard", "Joseph"])
    nameWhat = random.choice(
        ["Mooh4VjoO5NeGJud1blxzg==", "Q0DYWXOPka9F83IIP1pSyg=="])
    if nameWhat == "Mooh4VjoO5NeGJud1blxzg==":
        nameUser = input("What is " + nameName + "'s name>")
    elif nameWhat == "Q0DYWXOPka9F83IIP1pSyg==":
        nameUser = input("If a person is called " +
                         nameName + ", what is their name>")
    else:
        return False
    return nameUser == nameName


def all(mathmaxnum):
    return (
        captcha.math(mathmaxnum) == True
        and captcha.text() == True
        and captcha.animal() == True
        and captcha.lastword() == True
        and captcha.digit() == True
        and captcha.biggest() == True
        and captcha.smallest() == True
        and captcha.name() == True
    )

# Made with <3
