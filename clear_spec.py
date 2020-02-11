import os

dir = os.listdir("Dataset")
dir.remove("replace.py")

for genre in dir:
    folder=os.listdir(f'Dataset/{genre}/spec/')
    for i in folder:
        os.remove(f'Dataset/{genre}/spec/{i}')