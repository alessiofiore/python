import shutil

mie = open("mie.txt", "r")
tutte = open("tutte.txt", "r")
movedFiles = 0
res = open("res.txt", "w")
for lineMie in mie:
    lineMie = lineMie.rstrip('\n')
    found = False
    for lineTutte in tutte:
        lineTutte = lineTutte.rstrip('\n')
        if lineMie == lineTutte:
            found = True
            break
    if not found:
        fileName = lineMie + ".CR2"
        shutil.move("/Users/alessiofiore/Pictures/foto/Altro/Nostre/Tommaso/MIE/" + fileName, "/Users/alessiofiore/Pictures/foto/Altro/Nostre/Tommaso/" + fileName)
        movedFiles += 1
        res.write(lineMie + "\n")
res.close()
print str(movedFiles) + " files moved"
tutte.close()
mie.close()
