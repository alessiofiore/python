''' 
This script reads a source list of file names, reads a list of target file names and moves all files except for the ones present in both lists.
This script also produce a dest.txt file that contains the moved filenames.
'''
import shutil

source = open("source.txt", "r")
target = open("target.txt", "r")
movedFiles = 0
dest = open("dest.txt", "w")
for lineSource in source:
    lineSource = lineSource.rstrip('\n')
    found = False
    for lineTarget in target:
        lineTarget = lineTarget.rstrip('\n')
        if lineSource == lineTarget:
            found = True
            break
    if not found:
        fileName = lineSource + ".CR2"
        shutil.move("~/sourcedir/" + fileName, "~/destdir/" + fileName)
        movedFiles += 1
        dest.write(lineSource + "\n")
dest.close()
print str(movedFiles) + " files moved"
target.close()
source.close()
