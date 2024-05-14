import pygame

import pygame

#inicializando modulos de pygame
pygame.init()
#criando uma janela com o titulo "ola, mundo"
janela = pygame.display.set_mode((400,300))
pygame.display.set_caption("ola mundo")

deve_continuar = True
#loop do jogo
while deve_continuar:
    #checando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
#encerrendo o modolos de pygame
pygame.quit()
