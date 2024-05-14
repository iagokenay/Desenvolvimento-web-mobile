import pygame
import sys

pygame.init()

largura, altura = 800,600
fps = 60
gravidade = 1
pulo_jogador = -15
velocidade_jogador = 5
velocidade_inimigo = 5
cor_branco = (255,255,255)

janela=pygame.display.set_mode((largura, altura))
pygame.display.set_caption('DBZ')

jogador = pygame.transform.scale(pygame.image.load('newgame\goku-removebg-preview.png'),(50, 50))
inimigo = pygame.transform.scale(pygame.image.load('newgame\maidnbu-removebg-preview.png'),(80,80))
fundo = pygame.transform.scale(pygame.image.load('newgame\Dragonball_Z_007_-_Day_1.mkv_000197655.png'),(largura,altura))

retangulo_jogador = jogador.get_rect(topleft=(50, altura-jogador.get_height()-20))
velo_y_jogador = 0
pulando_jogador = False

retangulo_inimigo = inimigo.get_rect(topleft=(50,altura-inimigo.get_height()-20))
direcao_inimigo = 'esquerda'

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_LEFT] and retangulo_jogador.left > 0:
        retangulo_jogador.x -= velocidade_jogador
    if tecla[pygame.K_RIGHT] and retangulo_jogador.right < largura:
        retangulo_jogador.x += velocidade_jogador
    if not pulando_jogador:
        if tecla[pygame.K_SPACE]:
            velo_y_jogador = pulo_jogador
            pulando_jogador = True
    else:
        velo_y_jogador += gravidade
        retangulo_jogador.y += velo_y_jogador

        if retangulo_jogador.y >= altura - jogador.get_height() - 20:
            retangulo_jogador.y = altura - jogador.get_height() -20
            pulando_jogador = False