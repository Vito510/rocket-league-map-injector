import os
import shutil
path = '.'
dstFile = open("dst.txt", "r")
gameDir = dstFile.read()+'/TAGame/CookedPCConsole'
print("Created by https://github.com/Vito510\n")
i = int(1)
directory_contents = os.listdir("MapFolders")
for item in directory_contents:
    print(i,"> ",item)
    i = i + 1
i = int(1)
x = int(input("\nMap number >"))

for item in directory_contents:
    if i == x:
     print("\n"+item)
     folderName = item
     path = item
     i = i + 1
    else:
     i = i + 1
path = "MapFolders/"+path
directory_contents = os.listdir(path)
item = ''
for item in directory_contents:
    if os.path.isdir(item):
        item = item

path = path+"/"+item
gameDir = gameDir+"/Labs_Utopia_P.upk"
print("\nsource > ",path)
print("destination > ",gameDir)
shutil.copyfile(path,gameDir)

print("\nDone!")
input("press ENTER to close")


   





