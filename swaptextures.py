import os
import PIL.Image
import PIL.ImageColor
import random
import math
import shutil
import fnmatch

def convert():
    cwd = os.getcwd()
    for root, dirs, files in os.walk("./textures"):
        
        fileCounter = 0

        for file in files:
            if file.endswith(".png"):
                randomFiles = fnmatch.filter(os.listdir(root), "*.png")
                fileCounter = fileCounter + 1
                randomFile = random.choice(randomFiles)

                if not fileCounter == len(files):
                    while os.path.join(root, randomFile) == os.path.join(root, file):
                        randomFiles2 = randomFiles
                        randomFile = random.choice(randomFiles2)
                        print(os.path.join(root, randomFile) + " " + os.path.join(root, file))
                    img_path = os.path.join(root, file)
                    img_path2 = os.path.join(root, randomFile)

                    print("swapping " + img_path + " with " + img_path2)

                    #get img2's graphic data, then after it's stored copy img1 to img2. after that replace img1 with img2's data

                    shutil.copy(img_path2, os.path.join(cwd, "test.png"))

                    shutil.copy(img_path,img_path2)
                    shutil.copy(os.path.join(cwd, "test.png"), img_path)
                    