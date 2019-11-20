import os, sys
from PIL import Image
import zipfile
import io

appleWatch = {
    "AppIcon.appiconset": {
        "notificationCenter38mm@2x": 48,
        "notificationCenter40mm@3x": 55,
        "notificationCenter42mm@3x": 55,

        "companionSettings44mm@2x": 58,
        "companionSettings44mm@3x": 87,

        "homeScreen38mm@2x": 80,
        "homeScreen40mm@2x": 88,
        "homeScreen42mm@2x": 88,
        "homeScreen44mm@2x": 100,

        "shortLook38mm@2x": 172,
        "shortLook40mm@2x": 216,
        "shortLook42mm@2x": 196,
        "shortLook44mm@2x": 216,

        "appStore@1x": 1024
    },
    "Circular.imageset": {
        "circular38mm@2x": 32,
        "circular40mm@2x": 36,
        "circular42mm@2x": 36,
        "circular44mm@2x": 40
    },
    "Extra Large.imageset": {
        "extraLarge38mm@2x": 182,
        "extraLarge40mm@2x": 203,
        "extraLarge42mm@2x": 203,
        "extraLarge44mm@2x": 224 
    }
}

def createImage(image, zipFile, folder, name, width):
    resized = im.resize((width, width))
    buf = io.BytesIO()
    resized.save(buf, format="PNG")
    zipFile.writestr("{}/{}.png".format(folder, name), buf.getvalue())

if __name__ == '__main__':
    inFile = sys.argv[1]
    im = Image.open(inFile)
    zf = zipfile.ZipFile('Apple Watch Complication Images.zip', 'w')
    for folder, entries in appleWatch.items():
        for name, width, in entries.items():
            createImage(im, zf, folder, name, width)
    zf.close()
    im.close()