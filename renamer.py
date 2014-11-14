import os
import glob
import sys

#Function to rename file
def _renameFile(originalFile, newName):
    os.rename(originalFile, newName)

def _renameMultipleFiles(folder, extension, prefix):
    sFilePrefix = prefix
    iIncrement = 1
    l = glob.glob(folder+"/*."+extension)
    
    for element in l:
        if os.path.isfile(element) and (os.path.basename(element)).endswith(extension) > 0 :
            _renameFile(element, folder+"/"+sFilePrefix+str(iIncrement).zfill(5)+"."+extension)
            iIncrement = iIncrement + 1

OPTION_PREFIX = "--"
OPTION_EQUAL = "="
aListOptions = {}
FOLDER_OPTION = "folder"
PREFIX_OPTION = "prefix"
for argument in sys.argv:
    if argument.find(OPTION_PREFIX) == 0 and argument.find(OPTION_EQUAL) > 0 :
        option = argument[2:argument.index(OPTION_EQUAL)]
        value = argument[argument.index(OPTION_EQUAL)+1:]
        aListOptions[option] = value
folder = './'
prefix = 'new_'
if FOLDER_OPTION in aListOptions.keys():
    folder = aListOptions[FOLDER_OPTION]
if PREFIX_OPTION in aListOptions.keys():
    prefix = aListOptions[PREFIX_OPTION]

_renameMultipleFiles(folder, 'JPG', prefix)
