import os
import sys
from PIL import Image
import zipfile
import io

iOS = {
    "AppIcon.appiconset": {
        "notification20pt@2x": 40,
        "notification20pt@3x": 60,

        "settings29pt@2x": 58,
        "settings29pt@3x": 87,

        "spotlight40pt@2x": 80,
        "spotlight40pt@3x": 120,

        "app60pt@2x": 120,
        "app60pt@3x": 180,

        "iPadNotifications20pt@1x": 20,
        "iPadNotifications20pt@2x": 40,

        "iPadSettings29pt@1x": 29,
        "iPadSettings29pt@2x": 58,

        "iPadSpotlight40pt@1x": 40,
        "iPadSpotlight40pt@2x": 80,

        "iPadApp76pt@1x": 76,
        "iPadApp76pt@2x": 152,
        "iPadProApp83pt@2x": 167,

        "AppStore1024pt@1x": 1024,
    }
}

appleWatch = {
    "AppIcon.appiconset": {
        "notificationCenter38mm@2x": 48,
        "notificationCenter40mm@2x": 55,
        "notificationCenter42mm@2x": 55,

        "companionSettings44mm@2x": 58,
        "companionSettings44mm@3x": 87,

        "homeScreen38mm@2x": 80,
        "homeScreen40mm@2x": 88,
        "homeScreen42mm@2x": 88,
        "homeScreen44mm@2x": 100,

        "shortLook38mm@2x": 172,
        "shortLook40mm@2x": 196,
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

def createArchive(im, name, spec):
    zf = zipfile.ZipFile(name, 'w')
    for folder, entries in spec.items():
        for name, width, in entries.items():
            createImage(im, zf, folder, name, width)
    zf.close()

if __name__ == '__main__':
    inFile = sys.argv[1]
    im = Image.open(inFile)
    createArchive(im, 'Apple Watch (and Complication) Assets.zip', appleWatch)
    createArchive(im, 'iOS Assets.zip', iOS)
    im.close()

