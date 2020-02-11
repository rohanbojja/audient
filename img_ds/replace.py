import os

Genres = os.listdir()
Genres.remove('replace.py')
for genre in Genres:
    Songs  = os.listdir(f"{genre}")
    i=0
    for song in Songs:
        os.rename(f'./{genre}/{song}',f'./{genre}/{genre}{i}.png')
        i+=1


