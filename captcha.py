# For help: https://github.com/koviubi56/python-captcha/wiki
import time
import tkinter as tk
import random


def math(maxnum):
    """A math question

    Args:
        maxnum (int): The maximum addend

    Returns:
        bool: The captcha succesfullity
    """
    mathFirst = random.randrange(1, maxnum)
    mathSecond = random.randrange(1, maxnum)
    mathAdd = random.choice(["+", " plus "])
    mathWhat = random.choice(
        ["neabFmf9oly3tMn4tE9Ggw==", "hsBLyYY+7qD6ZDpbvQs+Lw=="])
    try:
        if mathWhat == "neabFmf9oly3tMn4tE9Ggw==":
            mathUser = int(input("What is " + str(mathFirst) +
                                 mathAdd + str(mathSecond) + ">"))
        elif mathWhat == "hsBLyYY+7qD6ZDpbvQs+Lw==":
            mathUser = int(
                input(str(mathFirst) + " " + mathAdd + " " + str(mathSecond) + " is>"))
        else:
            return False
    except ValueError:
        print("[ERROR]")
        print("ValueError")
        print("You needed to write an (int) number!")
        input("Press enter to continue!")
        input("We will send False to the program, so we say \"The captcha was didn't completed successfully.\" Press enter to confirm!")
        return False
    return mathUser == mathFirst + mathSecond


def text():
    """Gives you a number, and you need to copy it

    Returns:
        bool: The captcha succesfullity
    """
    textText = str(random.randrange(
        1, 999)*random.randrange(1, 999) + 11)
    textUser = input("Write " + str(textText) + ">")
    return textText == textUser


def animal():
    """Gives you an animal and its color, and you need to name its name or color

    Returns:
        bool: The captcha succesfullity
    """
    animals = ["Elephat", "Tiger", "Snake", "CRAB", "BIRD", "spider", "Cow", "sheep", "COW", "Dog",
               "CAT", "BEE", "PIG", "owl", "monkey", "T-Rex", "Giraffe", "Goat", "FOX", "bear", "PENGUIN", "Mouse"]
    colors = ["RED", "Orange", "yellow", "Chartreuse", "green",
              "Spring", "cyan", "azure", "BLUE", "Violet", "magenta", "Rose"]
    animalAnimal = random.choice(animals)
    animalColor = random.choice(colors)
    animalName = random.choice(
        ["k6r+A87Rzp3mJKDDnjhpzQ==", "o6zbD1J+cb+omtrcULg8hw==", "OsA+1cKz/ko14A9xvyHmbHCZVYq6qqZZFndU29YvUIM="])
    if animalName == "k6r+A87Rzp3mJKDDnjhpzQ==":
        animalUser = input("If the " + animalAnimal + " is " +
                           animalColor + ", what color is it (case-sensitive)>")
    elif animalName == "o6zbD1J+cb+omtrcULg8hw==":
        animalUser = input("If the " + animalAnimal + " is " +
                           animalColor + ", what animal is it (case-sensitive)>")
    elif animalName == "OsA+1cKz/ko14A9xvyHmbHCZVYq6qqZZFndU29YvUIM=":
        animalUser = input("The " + animalColor + " " +
                           animalAnimal + " is what color>")
    else:
        return False

    if animalName == "k6r+A87Rzp3mJKDDnjhpzQ==" or animalAnimal == "OsA+1cKz/ko14A9xvyHmbHCZVYq6qqZZFndU29YvUIM=":
        return animalUser == animalColor
    elif animalName == "o6zbD1J+cb+omtrcULg8hw==":
        return animalUser == animalAnimal
    return False


def lastword():
    """Gives you a list, and you need to write the first/second/third thing from the list

    Returns:
        bool: The captcha succesfullity
    """
    animals = ["Elephat", "Tiger", "Snake", "CRAB", "BIRD", "spider", "Cow", "sheep", "COW", "Dog",
               "CAT", "BEE", "PIG", "owl", "monkey", "T-Rex", "Giraffe", "Goat", "FOX", "bear", "Penguin", "mouse"]
    colors = ["RED", "Orange", "yellow", "Chartreuse", "green",
              "Spring", "cyan", "azure", "BLUE", "Violet", "magenta", "Rose"]
    words = ["MILK", "orange", "Tree", "WINDOW", "table", "pencil",
             "Water", "Glue", "BOOK", "paper", "Power", "COLOR", "sky", "Airport", "SLEEP", "Light", "DAY", "Week", "Month", "YEAR"]
    mix = animals + colors + words
    lastwords = [random.choice(mix), random.choice(
        mix), random.choice(mix)]
    lastwordQ = random.choice(["list", "series"])
    lastwordWhat = random.choice(
        ["06zNSgCAITUEurlPewn5tw==", "5OAYoY++S8oFDXL15oDlmw==", "mwf+NAMaRDt/WGB3k75rPQ=="])
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
    return False


def digit():
    """Gives you a number, and you need to write its *th digit

    Returns:
        bool: The captcha succesfullity
    """
    digitDigit = random.randrange(4, 10)
    digitNumber = random.randrange(1000000000, 10000000000)
    digitWhat = random.choice(
        ["I4sZv95d/efwlH55KJZavQ==", "mXYMEkTnMfK9nqShwT8x+A==", "OjX3nWXUCaECPyuemv4EAg=="])
    digitList = [int(digitInAnsware) for digitInAnsware in str(digitNumber)]
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
    return digitUser == digitList[digitDigit - 1]


def biggest():
    """Gives you two numbers, and you need to write the biggest

    Returns:
        bool: The captcha succesfullity
    """
    biggestFirst = ""
    biggestSecond = ""
    biggestWhat = random.choice(["iu8GCXhuhyTPT+3uV6NSsQ==", "4nJw2yjPdCUTKIDyLwFcmQ==",
                                 "gwUaDNtI2qNmB1RAVlTrDh7wU8XPR/kQi42NSzH3Uug=", "mRYXBTkJnSiHUzuwzEwK5SAUEKkzBHZ330JiyIAQXZA="])
    biggestQWord = random.choice(["largest", "biggest", "highest"])
    while biggestFirst == biggestSecond:
        biggestFirst = int(random.randrange(1, 100))
        biggestSecond = int(random.randrange(1, 100))
    try:
        if biggestWhat == "iu8GCXhuhyTPT+3uV6NSsQ==":
            biggestUser = int(input(str(biggestFirst) + " or " +
                                    str(biggestSecond) + ": which of these is the " + biggestQWord + ">"))
        elif biggestWhat == "4nJw2yjPdCUTKIDyLwFcmQ==":
            biggestUser = int(input("Enter the " + biggestQWord + " number of " +
                                    str(biggestFirst) + " and " + str(biggestSecond) + ">"))
        elif biggestWhat == "gwUaDNtI2qNmB1RAVlTrDh7wU8XPR/kQi42NSzH3Uug=":
            biggestUser = int(
                input(str(biggestFirst) + ", or " + str(biggestSecond) + ": the " + biggestQWord + " is>"))
        elif biggestWhat == "mRYXBTkJnSiHUzuwzEwK5SAUEKkzBHZ330JiyIAQXZA=":
            int(input(str(biggestFirst) + ", or " +
                      str(biggestSecond) + ": the " + biggestQWord + " is>"))
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
        return biggestFirst > biggestSecond
    elif biggestUser == biggestSecond:
        return biggestFirst < biggestSecond
    return False


def smallest():
    """Gives you two numbers, and you need to write the smallest

    Returns:
        bool: The captcha succesfullity
    """
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
        return smallestFirst < smallestSecond
    elif smallestUser == smallestSecond:
        return smallestFirst > smallestSecond
    return False


def name():
    """Gives you a person, and you need to write his name

    Returns:
        bool: The captcha succesfullity
    """
    nameName = random.choice(
        ["John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Liam", "Noah", "Logan", "Benjamin", "Mason", "Elijah", "Oliver"])
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


def color():
    """Gives a color, and you need to write it (black/white)

    Returns:
        bool: The captcha succesfullity
    """
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
    return (
        colorUser == "WHITE"
        and color == "wx9XfbNO+vuRHo837XToBg=="
        or colorUser == "black"
        and color == "YY0C75qWSpXAbWlNRpXm1A=="
    )


def day():
    """Gives you a day, and you need to write it

    Returns:
        bool: The captcha succesfullity
    """
    dayQWhat = random.choice(
        ["X+f59jNsreM/h1LyGpM6abkZIaQP47wasfjfuChxCrHwiYgi4uVFVUpjphSFI33s"])
    dayDWhat = random.choice(
        ["Monday", "Tuesday", "WEDNESDAY", "Thursday", "Friday", "saturday", "sunday"])
    if dayQWhat == "X+f59jNsreM/h1LyGpM6abkZIaQP47wasfjfuChxCrHwiYgi4uVFVUpjphSFI33s":
        dayUser = input("If tomorrow is " + dayDWhat +
                        ", what day is today(case-sensitive)>")
        return dayUser == dayDWhat
    return False


def all(mathmaxnum):
    return bool(
        math(mathmaxnum)
        and text()
        and animal()
        and lastword()
        and digit()
        and biggest()
        and smallest()
        and name()
        and color()
        and day()
    )

# Made with <3
# * A lot of things were stealed from textcaptcha.com!


if __name__ == '__main__':
    all(10)
