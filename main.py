import time
import zipfile
import glob
import os
import blur
import shutil
import grayscale

if os.path.exists('./textures'):
    a = input('./textures already exists. Do you want to remove it? [y/n] ')
    if a.lower() == 'y' or 'yes':
        shutil.rmtree('./textures')
        print('removed.')
    else:
        print("Not removing.")
        exit()

print("Welcome to Xylight's texture modifier!")
path = input("Please enter the path to a minecraft texture pack (.zip): ")
print("Working...")

with zipfile.ZipFile(path,"r") as zip_ref:
    zip_ref.extractall("./textures")

print("Done. File was extracted to ./textures")
time.sleep(.5)
a = input("\nWhat effect do you want to add to this texturepack? [blur/grayscale/cancel] ")

if a.lower() == "blur":
    print("Working...")
    blur.convert()
elif a.lower() == "grayscale":
    print("Working... (hopefully)")
    grayscale.convert()
else:
    print("Ok, won't add any filters.")
    exit()


a = input('finished! Would you like to put it back as a zip? (Will not overwrite old file, will make a new one) [y/n] ')
if a.lower() == "y":
    print("Working... zipping folder/files...")
    zipObj = zipfile.ZipFile('pack.zip', 'w')

    os.chdir('./textures')

    for root, dirs, files in os.walk("./"):
        for file in files:
            fileToZip = os.path.join(root, file)
            zipObj.write(fileToZip)

    zipObj.close()
