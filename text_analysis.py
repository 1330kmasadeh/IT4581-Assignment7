# text_analysis.py

import os

def text_analysis(filename):

    if os.path.exists(filename):

        file = open(filename, "r")

        text = file.read()

        words = text.split()
        lines = text.split("\n")

        print("Word count:", len(words))
        print("Line count:", len(lines))

        file.close()

    else:
        print("File not accessible")


filename = input("Enter file name: ")

text_analysis(filename)
