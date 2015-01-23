import os
import glob
import sys
import getopt

VERSION = "0.1"

def usage():
    print('Usage: '+sys.argv[0]+' [-h] [--version] [--help] [--folder=<path>] [--prefix=<name>] [--extension=<extension>]')
    print()
    print('OPTIONS')
    print()
    print('  --help, -h')
    print('        Output the help message, which means this message and exits')
    print('  --folder=<path>')
    print('        Path to the folder containing the images. By default, it is the current folder')
    print('  --prefix=<name>')
    print('        Word that will prefix all renamed images. By default, it is defined as "new_"')
    print('  --extension=<extension>')
    print('        Case sensitive extension filter. Only the files with this extension will be renamed. Default is JPG')
    print('  --version')
    print('        Output the version of the software and exits')

def version():
    print('ImgRenamer v'+VERSION)
    print('Software developed by Yoann Gesquiere <yoann.gesquiere@gmail.com>')

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
extension = 'JPG'

try:
    opts, args = getopt.getopt(sys.argv[1:], "h", ["prefix=", "folder=", "help", "version", "extension="])
except getopt.GetoptError:
    print('Unknown option')
    usage()
    exit(2)

for opt, arg in opts:
    if opt in ("--prefix"):
        prefix = arg
    elif opt in ("--folder"):
        folder = arg
    elif opt in ("--extension"):
        extension = arg
    elif opt in ("--help", "-h"):
        usage()
        exit(0)
    elif opt in ("--version"):
        version()
        exit(0)

_renameMultipleFiles(folder, extension, prefix)
