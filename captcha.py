# This work by Koviubi56 is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/
# To use it:
# import captcha.py
# captcha.math()
# captcha.text()
# captcha.animal()
# captcha.lastword()
# For help: [GITHUB WIKI URL]
# TL;DR: CC BY-NC-SA 4.0 & For help: [GITHUB WIKI URL]
import random


class captcha:
    def math(maxnum):
        mathFirst = random.randrange(1, maxnum)
        mathSecond = random.randrange(1, maxnum)
        mathUser = int(input("What is " + str(mathFirst) +
                             "+" + str(mathSecond) + ">"))
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
        lastwordWhat = random.choice(["06zNSgCAITUEurlPewn5tw==",
                                      "5OAYoY++S8oFDXL15oDlmw==", "mwf+NAMaRDt/WGB3k75rPQ=="])
        if lastwordWhat == "06zNSgCAITUEurlPewn5tw==":
            lastwordUser = input(
                "Write the second word from this list: " + str(lastwords) + ">")
            if lastwordUser == lastwords[1]:
                return True
            else:
                return False
        elif lastwordWhat == "5OAYoY++S8oFDXL15oDlmw==":
            lastwordUser = input(
                "Write the third word from this list: " + str(lastwords) + ">")
            if lastwordUser == lastwords[2]:
                return True
            else:
                return False
        elif lastwordWhat == "mwf+NAMaRDt/WGB3k75rPQ==":
            lastwordUser = input(
                "Write the first word from this list: " + str(lastwords) + ">")
            if lastwordUser == lastwords[0]:
                return True
            else:
                return False
        else:
            return False
