import os

print("Enter the folder you want to clean up: ")
folder=input()
songs = os.listdir(f'{folder}')
print(songs)
songs.remove('spec')

for song in songs:
    os.rename(f'./{folder}/{song}',f'./{folder}/{song.replace(" ","_")}')
