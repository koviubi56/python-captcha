# This work by Koviubi56 is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/
# For help: https://github.com/koviubi56/python-captcha/wiki
import random
import tkinter as tk
import time


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
    if mathUser == mathFirst + mathSecond:
        return True
    else:
        return False


def text():
    textText = str(random.randrange(
        1, 999)*random.randrange(1, 999) + 11)
    textUser = input("Write " + str(textText) + ">")
    if textText == textUser:
        return True
    else:
        return False


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
        if animalUser == animalColor:
            return True
        else:
            return False
    else:
        animalUser = input("If the " + animalAnimal + " is " +
                           animalColor + ", what animal is it (case-sensitive)>")
        if animalUser == animalAnimal:
            return True
        else:
            return False


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
        if lastwordUser == lastwords[1]:
            return True
        else:
            return False
    elif lastwordWhat == "5OAYoY++S8oFDXL15oDlmw==":
        lastwordUser = input(
            "Write the third word from this " + lastwordQ + ": " + str(lastwords) + " (case-sensitive)>")
        if lastwordUser == lastwords[2]:
            return True
        else:
            return False
    elif lastwordWhat == "mwf+NAMaRDt/WGB3k75rPQ==":
        lastwordUser = input(
            "Write the first word from this " + lastwordQ + ": " + str(lastwords) + " (case-sensitive)>")
        if lastwordUser == lastwords[0]:
            return True
        else:
            return False
    else:
        return False


def digit():
    digitDigit = random.randrange(4, 10)
    digitNumber = random.randrange(1000000000, 10000000000)
    digitWhat = random.choice(
        ["I4sZv95d/efwlH55KJZavQ==", "mXYMEkTnMfK9nqShwT8x+A==", "OjX3nWXUCaECPyuemv4EAg=="])
    digitList = []
    for digitInAnsware in str(digitNumber):
        digitList.append(int(digitInAnsware))
    digitInAnsware = ""
    try:
        if digitWhat == "mXYMEkTnMfK9nqShwT8x+A==":
            digitUser = int(input("In the number " + str(digitNumber) +
                                  ", what is the " + str(digitDigit) + "th digit>"))
        elif digitWhat == "I4sZv95d/efwlH55KJZavQ==":
            digitUser = int(input("Which digit is " + str(digitDigit) +
                                  "th in the number " + str(digitNumber) + ">"))
        elif digitWhat == "OjX3nWXUCaECPyuemv4EAg==":
            digitUser = int(
                input("What is the " + str(digitDigit) + "th digit in " + str(digitNumber) + ">"))
        else:
            return False
    except ValueError:
        print("[ERROR]")
        print("ValueError")
        print("You needed to write an (int) number!")
        input("Press enter to continue!")
        input("We will send False to the program, so we say \"The captcha was didn't completed successfully.\" Press enter to confirm!")
        return False
    if digitUser == digitList[digitDigit - 1]:
        return True
    else:
        return False


def biggest():
    biggestFirst = ""
    biggestSecond = ""
    biggestWhat = random.choice(
        ["iu8GCXhuhyTPT+3uV6NSsQ==", "4nJw2yjPdCUTKIDyLwFcmQ=="])
    biggestQWord = random.choice(["largest", "biggest", "highest"])
    while biggestFirst == biggestSecond:
        biggestFirst = int(random.randrange(1, 100))
        biggestSecond = int(random.randrange(1, 100))
    try:
        if biggestWhat == "iu8GCXhuhyTPT+3uV6NSsQ==":
            biggestUser = int(input(str(biggestFirst) + " or " +
                                    str(biggestSecond) + ": which of these is the " + biggestQWord + ">"))
        elif biggestWhat == "4nJw2yjPdCUTKIDyLwFcmQ==":
            biggestUser = int(input("Enter the biggest number of " +
                                    str(biggestFirst) + " and " + str(biggestSecond) + ">"))
        else:
            return False
    except ValueError:
        print("[ERROR]")
        print("ValueError")
        print("You needed to write an (int) number!")
        input("Press enter to continue!")
        input("We will send False to the program, so we say \"The captcha was didn't completed successfully.\" Press enter to confirm!")
        return False
    if biggestUser == biggestFirst:
        if biggestFirst > biggestSecond:
            return True
        else:
            return False
    elif biggestUser == biggestSecond:
        if biggestFirst < biggestSecond:
            return True
        else:
            return False
    else:
        return False


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
    if smallestUser == smallestFirst:
        if smallestFirst < smallestSecond:
            return True
        else:
            return False
    elif smallestUser == smallestSecond:
        if smallestFirst > smallestSecond:
            return True
        else:
            return False
    else:
        return False


def name():
    nameName = random.choice(
        ["John", "Robert", "Michael", "William", "David", "Richard", "Joseph"])
    nameWhat = random.choice(
        ["Mooh4VjoO5NeGJud1blxzg==", "Q0DYWXOPka9F83IIP1pSyg=="])
    if nameWhat == "Mooh4VjoO5NeGJud1blxzg==":
        nameUser = input("What is " + nameName + "'s name>")
    elif nameWhat == "Q0DYWXOPka9F83IIP1pSyg==":
        nameUser = input("If a person is called " +
                         nameName + ", what is their name>")
    else:
        return False
    if nameUser == nameName:
        return True
    else:
        return False


def color():
    print("You get a color, and you need to name it!")
    print("Please wait...")
    time.sleep(5)
    print("If you see it, close the window!")
    color = random.choice(
        ["wx9XfbNO+vuRHo837XToBg==", "YY0C75qWSpXAbWlNRpXm1A=="])
    HEIGHT = 500
    WIDTH = 500

    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    if color == "YY0C75qWSpXAbWlNRpXm1A==":
        frame = tk.Frame(root, bg='black')
    elif color == "wx9XfbNO+vuRHo837XToBg==":
        frame = tk.Frame(root, bg='white')

    frame.place(relwidth=1, relheight=1)

    root.mainloop()
    colorUser = input("WHITE or black (case-sensitive)>")
    if colorUser == "WHITE" and color == "wx9XfbNO+vuRHo837XToBg==":
        return True
    elif colorUser == "black" and color == "YY0C75qWSpXAbWlNRpXm1A==":
        return True
    else:
        return False


def day():
    dayQWhat = random.choice(
        ["X+f59jNsreM/h1LyGpM6abkZIaQP47wasfjfuChxCrHwiYgi4uVFVUpjphSFI33s"])
    dayDWhat = random.choice(
        ["Monday", "Tuesday", "WEDNESDAY", "Thursday", "Friday", "saturday", "sunday"])
    if dayQWhat == "X+f59jNsreM/h1LyGpM6abkZIaQP47wasfjfuChxCrHwiYgi4uVFVUpjphSFI33s":
        dayUser = input("If tomorrow is " + dayDWhat +
                        ", what day is today(case-sensitive)>")
        if dayUser == dayDWhat:
            return True
        else:
            return False
    else:
        return False


def all(mathmaxnum):
    if captcha.math(mathmaxnum) == True:
        if captcha.text() == True:
            if captcha.animal() == True:
                if captcha.lastword() == True:
                    if captcha.digit() == True:
                        if captcha.biggest() == True:
                            if captcha.smallest() == True:
                                if captcha.name() == True:
                                    if captcha.color() == True:
                                        if captcha.day() == True:
                                            return True
    return False


def all2(mathmaxnum):
    if math(mathmaxnum) == True:
        if text() == True:
            if animal() == True:
                if lastword() == True:
                    if digit() == True:
                        if biggest() == True:
                            if smallest() == True:
                                if name() == True:
                                    if color() == True:
                                        if day() == True:
                                            return True
    return False
# Made with <3
