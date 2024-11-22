import pygame
pygame.init()
pygame.mixer.music.load('ex0021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.fadeout(20000)
input()
pygame.event.wait()
