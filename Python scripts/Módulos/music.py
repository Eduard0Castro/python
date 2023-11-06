import pygame

pygame.init()
pygame.mixer.music.load('charlie_brown.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
