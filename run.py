import os
import glob
import shutil
path = '.'
dstFile = open("dst.txt", "r")
gameDir = dstFile.read()+'/TAGame/CookedPCConsole'
print("Created by https://github.com/Vito510\n")
i = int(1)
fc = int(0)
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

array = os.listdir(path)
for x in range(len(array)):
    if array[x].split(".")[-1] == 'upk' or array[x].split(".")[-1] == 'udk':
        item = array[x]
        fc = fc + 1
        
if fc == 1:
    path = path+"/"+item
    gameDir = gameDir+"/Labs_Utopia_P.upk"
    print("\nsource > ",path)
    print("destination > ",gameDir)
    shutil.copyfile(path,gameDir)
    if len(array) > 1:
        print("\nWarning: \nfolder contains more than just a upk/udk file.\nSome maps require more than just a upk/udk file to work! \nThis program currently only moves the udk/upk file to the 'CookedPCConsole' folder")
    print("\nDone!")
    input("press ENTER to close")
elif fc > 1:
    print("\nError: Multiple upk/udk files found!")
    input("press ENTER to close")
else:
    print("\nError: No upk/udk files found!")
    input("press ENTER to close")


   





