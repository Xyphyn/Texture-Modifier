import os

def convert():
    cwd = os.getcwd()
    for root, dirs, files in os.walk("./textures"):

        for file in files:
            if file.endswith(".ogg"):
                