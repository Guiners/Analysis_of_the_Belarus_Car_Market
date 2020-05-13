import pygame
import numpy as np
import random as random

pygame.init()

screen_width = 1200
screen_height = 600
background_colour = (0,0,0)
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(background_colour)
pygame.display.set_caption("Generic Algoritm")
font = pygame.font.SysFont("comicsansms", 50)
font1 = pygame.font.SysFont("comicsansms", 40)
clock = pygame.time.Clock()



nump = np.random.randint(2, size=50)

nump1 = np.array2string(nump, separator=".")
text_best_individual = font1.render(nump1, True, (0,255,65))

file_name = font.render('File name: ' + "x", True, (0,255,65))
text1 = font.render('Population number: ' , True, (0,255,65))
text2 = font.render('Best individual in all populations: ' , True, (0,255,65))
text3 = font.render('Avrage: ' , True, (0,255,65))
text4 = font.render('Currently best individual: ' , True, (0,255,65))
text5 = font.render('Individuals: ' , True, (0,255,65))
text6 = font.render('Genes: ' , True, (0,255,65))
text7 = font.render('Chance for mutation: ' , True, (0,255,65))
text8 = font.render('Click SPACE to start', True, (0,255,65))

"""file_name = font.render('File name: ' + "x", True, (0,255,65))
text1 = font.render('Population number: ' + i, True, (0,255,65))
text2 = font.render('Best individual in all populations: ' + best_in_all, True, (0,255,65))
text3 = font.render('Avrage: ' + avrage, True, (0,255,65))
text4 = font.render('Currently best individual: ' + best_in_population, True, (0,255,65))
text5 = font.render('Individuals: ' + individual, True, (0,255,65))
text6 = font.render('Genes: ' + genes, True, (0,255,65))
text7 = font.render('Chance for mutation: ' + chance_for_mutation, True, (0,255,65))
text8 = font.render('Click SPACE to start', True, (0,255,65))"""
screen.blit(file_name,(10, 10))
screen.blit(text1 , (10, (20 + text1.get_height())))
screen.blit(text3, (10, (30 + text1.get_height()*2)))
screen.blit(text2, (10, (40 + text1.get_height()*3)))
screen.blit(text4, (10, round((screen_height - text_best_individual.get_height())/2 - text1.get_height() + 70)))
screen.blit(text5, (10, (50 + text1.get_height()*4)))
screen.blit(text6, (10, (60 + text1.get_height()*5)))
screen.blit(text7, (10, (70 + text1.get_height()*6)))
screen.blit(text8, (10, (screen_height - text1.get_height())))

screen.blit(text_best_individual, (round((screen_width - text_best_individual.get_width())/2), round((screen_height - text_best_individual.get_height())/2) + 100))
pygame.display.update()

running = True
while running:
    clock.tick(32)
    keys =pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False