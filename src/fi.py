# FI.PY by Alexander Abraham,
# a.k.a. "The Black Unicorn", a.k.a. "Angeldust Duke".
# Licensed under the MT license.

import os
import sys
import PIL
import argparse
from sys import exit
from os import chdir
from PIL import Image
from os import makedirs
from argparse import ArgumentParser
def dataPool():
    """
    Returns a [dict] with all relevant data.
    """
    pool = {
    '57':'apple-icon-57x57.png',
    '60':'apple-icon-60x60.png',
    '72':'apple-icon-72x72.png',
    '76':'apple-icon-76x76.png',
    '114':'apple-icon-114x114.png',
    '120':'apple-icon-120x120.png',
    '144':'apple-icon-144x144.png',
    '152':'apple-icon-152x152.png',
    '180':'apple-icon-180x180.png',
    '192':'android-icon-192x192.png',
    '32':'favicon-32x32.png',
    '96':'favicon-96x96.png',
    '16':'favicon-16x16.png',
    '144':'ms-icon-144x144.png'
    }
    return pool
def executeCompile(sourceImage):
    """
    Creates a directory called [favicons]
    and resizes and copies your sample image
    into the [favicons] directory.
    """
    try:
        targetDir = 'favicons'
        makedirs(targetDir)
        chdir(targetDir)
        src = '../' + sourceImage
        myImage = Image.open(src)
        for key in dataPool():
            size = int(key)
            new_image = myImage.resize((size, size))
            newString = dataPool()[key]
            new_image.save(newString)
    except Exception as error:
        print(str(error))
        exit()
def version():
    """
    A small version message.
    """
    print('Fi v.1.0.0 by Alexander Abraham.')
    exit()
def cli():
    """
    The tool's command-line
    interface.
    """
    parser = ArgumentParser()
    parser.add_argument('--source', help='source image to use')
    parser.add_argument('--version', help='displays version info', action='store_true')
    args = parser.parse_args()
    if args.version:
        version()
    elif args.source:
        executeCompile(args.source)
    else:
        print('Invalid arguments! Use the "--help" flag!')
        exit()
def main():
    """
    Main entry-point for the
    Python 3 interpreter.
    """
    cli()
if __name__ == '__main__':
    """
    Invokes the main function
    if the tools is called as
    a script.
    """
    main()
