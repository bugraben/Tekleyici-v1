from os import listdir, system
from time import sleep

system("title Tekleyici v1")
system("color 3f")
system("echo Tekleyici v1")

allLines = []
retry = True

def read():
    global allLines
    global retry
    for f in listdir('./folderX'):
        print(f)
        path = "./folderX/" + f
        with open(path, 'r') as file1:
            lines = file1.readlines()
            allLines += [f, "\n"]
            allLines += lines
            allLines += ["\n"]
    retry = False
    print("Tümü Tarandı")

def write():
    global allLines
    for line in allLines:
        with open("Summary.txt", "a") as sumFile:
            sumFile.write(line)
    sleep(0.5)
    print("Tümü Yazıldı")

while retry == True:
    try:
        read()
        write()
        sleep(0.5)
        system("pause")
    except UnicodeDecodeError:
        retry = True
        print("Bu araç yalnızca txt dosyalarını destekler. folderX içinde desteklenmeyen dosya bulunuyor! ")
        system("pause")


