from ImageProcess import *

InputDir=0
OutputDir=0

ChangeDir=input("Would you like to change your directories? (Y/N) ")
if ChangeDir=="Y" or ChangeDir=="y":
    InputDir=str(input("Please specify your Input Directory path: "))
    OutputDir=str(input("Please specify your Output Directory path: "))
    docProcessing(InputDir,OutputDir,blur=0,thresh=0)
    docProcessing(InputDir,OutputDir,thresh=0,blur=0,sharp=0)

if InputDir and OutputDir:
    docProcessing(InputDir,OutputDir,blur=0,thresh=0)
    docProcessing(InputDir,OutputDir,thresh=0,blur=0,sharp=0)
else:
    docProcessing(blur=0,thresh=0)
    docProcessing(thresh=0,blur=0,sharp=0)
