import os
import glob
import sys
import getopt

#Function to rename file
def _renameFile(originalFile, newName):
    os.rename(originalFile, newName)

#Function that renames all the images in a folder
def _renameMultipleFiles(folder, extension, prefix):
    iIncrement = 1
    l = glob.glob(folder+"/*."+extension)
    
    for element in l:
        if os.path.isfile(element) and (os.path.basename(element)).endswith(extension) > 0 :
            _renameFile(element, folder+"/"+prefix+str(iIncrement).zfill(5)+"."+extension)
            iIncrement = iIncrement + 1

folder = './'
prefix = 'new_'

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["prefix=", "folder="])
except getopt.GetoptError:
    print('KO')
    exit(2)

for opt, arg in opts:
    if opt in ("--prefix"):
        prefix = arg
    elif opt in ("--folder"):
        folder = arg

_renameMultipleFiles(folder, 'JPG', prefix)
