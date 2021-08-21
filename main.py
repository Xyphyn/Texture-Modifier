import time
import zipfile
import glob
import os
import blur
import shutil
import grayscale
import randomcolor
import pixelswap
import fold
import foldsideways
import upsidedown
import swaptextures
import swapaudio
import rgbmax
import blackscale
import invert

if os.path.exists('./textures'):
    a = input('./textures already exists. Do you want to remove it? [y/n] ')
    if a.lower() == 'y':
        shutil.rmtree('./textures')
        print('removed.')
    elif a.lower() == 'n':
        print("Not removing.")

print("Welcome to Xylight's texture modifier!")
path = input("Please enter the path to a minecraft texture pack (.zip): ")
if path == "n":
    pass
else:
    print("Working...")

    with zipfile.ZipFile(path,"r") as zip_ref:
        zip_ref.extractall("./textures")

    print("Done. File was extracted to ./textures")
time.sleep(.5)
a = input("\nWhat effect do you want to add to this texturepack? [blur/grayscale/randomcolor/pixelswap/fold/foldsideways/upsidedown/swaptextures/swapaudio/blackscale/rgbmax/invert/cancel] ")

if a.lower() == "blur":
    print("Working...")
    blur.convert()
elif a.lower() == "grayscale":
    print("Working...")
    grayscale.convert()
elif a.lower() == "randomcolor":
    print("Warning: randomcolor is pretty slow, as it loops through every single pixel inside of every image.")
    randomcolor.convert()
elif a.lower() == "pixelswap":
    print("pixelswap is pretty slow.")
    time.sleep(.5)
    print('working...')
    pixelswap.convert()
elif a.lower() == "fold":
    print("Same with pixelswap, pretty slow.")
    time.sleep(.5)
    print('working')
    fold.convert()
elif a.lower() == "upsidedown":
    upsidedown.convert()
elif a.lower() == "foldsideways":
    print("Working...")
    foldsideways.convert()
elif a.lower() == "swaptextures":
    print("Working...")
    swaptextures.convert()
elif a.lower() == "swapaudio":
    print("Working...")
    swapaudio.convert()
elif a.lower() == "rgbmax":
    rgbmax.convert()
elif a.lower() == "blackscale":
    blackscale.convert()
elif a.lower() == "invert":
    invert.convert()
else:
    print("Ok, won't add any filters.")
    exit()


a = input('finished! Would you like to put it back as a zip? (Will overwrite current zip) [y/n] ')
if a.lower() == "y":
    print("Working... zipping folder/files...")
    zipObj = zipfile.ZipFile('pack.zip', 'w')

    os.chdir('./textures')

    for root, dirs, files in os.walk("./"):
        for file in files:
            fileToZip = os.path.join(root, file)
            zipObj.write(fileToZip)

    zipObj.close()
