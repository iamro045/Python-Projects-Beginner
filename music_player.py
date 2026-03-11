import pygame
import os

pygame.init()
pygame.mixer.init()

folder = "music"

songs = os.listdir(folder)

print("Songs:")
for i, s in enumerate(songs):
    print(i, s)

choice = int(input("Choose song number: "))

song_path = os.path.join(folder, songs[choice])

pygame.mixer.music.load(song_path)
pygame.mixer.music.play()

input("Press Enter to stop...")
