import pygame

pygame.init()
pygame.mixer.music.load('Como Dizia o Mestre.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
