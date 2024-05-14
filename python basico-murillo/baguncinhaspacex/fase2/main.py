import pygame
import sys
import random

pygame.init()
x=0
largura = 1280
altura = 720
WHITE = (255, 255, 255)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('naveLast')

fundo = pygame.image.load('D:/Estudos/python basico-murillo/baguncinhaspacex/fase2/fundo.png').convert_alpha()
fundo = pygame.transform.scale(fundo, (largura, altura))

# vitoria = pygame.image.load('D:/Estudos/python basico-murillo/navelast/vitoria.png').convert_alpha()
# vitoria = pygame.transform.scale(fundo, (largura, altura))

inimigo = pygame.image.load('D:/Estudos/python basico-murillo/baguncinhaspacex/fase2/p2.png').convert_alpha()
inimigo =  pygame.transform.scale(inimigo, (150,150))

jogador = pygame.image.load('D:/Estudos/python basico-murillo/baguncinhaspacex/fase2/p1.png').convert_alpha()
jogador = pygame.transform.scale(jogador, (300,150))

missil = pygame.image.load('D:/Estudos/python basico-murillo/baguncinhaspacex/fase2/misill.png').convert_alpha()
missil = pygame.transform.scale(missil, (100,100))

pygame.mixer.music.load('D:/Estudos/python basico-murillo/baguncinhaspacex/fase2/Stalin loves disco.mp3')
pygame.mixer.music.play(-1)#para reproduzir a musica continua -1

pos_inimigox = 500
pos_inimigoy = 360

pos_jogadorx = 200
pos_jogadory = 300

vel_missil = 0
pos_missilx = 228
pos_missily = 350 
 
pontos = 6 # Variável para armazenar a pontuação
font = pygame.font.Font(None, 36) # Define uma fonte para exibir a pontuação

triggered = False
rodando = True

jogador_rect = jogador.get_rect()
inimigo_rect = inimigo.get_rect()
missil_rect = missil.get_rect()

#função de renacer aleatorio do inimigo

def respawn():
    x = 1350
    y = random.randint(1,640)
    return[x,y]

def respawn_missil():
    triggered = False
    respawn_missilx = pos_jogadorx
    respawn_missily = pos_jogadory
    vel_missil = 0
    return [respawn_missilx, respawn_missily, triggered, vel_missil]

def colisions():
    global pontos
    if jogador_rect.colliderect(inimigo_rect) or inimigo_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(inimigo_rect):
        pontos += 1
        return True
    else:
        return False
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    tela.blit(fundo, (0,0))
    rel_x = x % fundo.get_rect().width
    tela.blit(fundo, (rel_x - fundo.get_rect().width,0)) #cria fundo apos o fundo
    if rel_x < 1280:
        tela.blit(fundo, (rel_x, 0))
    #comando de movimento 
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_jogadory > 1:
        pos_jogadory -= 1.5
        if not triggered:
            pos_missily -= 1
    if tecla[pygame.K_DOWN] and pos_jogadory < 665:
        pos_jogadory += 1.5
        if not triggered:
            pos_missily += 1 
    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil = 2
    if pontos== -1:
        rodando = False
    # if pontos == 10:
    #     tela.blit(vitoria)
    #respawn inimigo 
    if pos_inimigox == 50:
        pos_inimigox = respawn()[0]
        pos_inimigoy = respawn()[1]
    if pos_missilx == 1250:
        pos_missilx, pos_missily, triggered, vel_missil = respawn_missil()
    if pos_inimigox == 50 or colisions():
        pos_inimigox = respawn()[0]
        pos_inimigoy = respawn()[1]

    #rect posiçao
    jogador_rect.x = pos_jogadorx
    jogador_rect.y = pos_jogadory

    inimigo_rect.x = pos_inimigox
    inimigo_rect.y = pos_inimigoy

    missil_rect.x = pos_missilx
    missil_rect.y = pos_missily

    x -= 1 # velocidade de movimennto 
    pos_inimigox -= 2

    pos_missilx += vel_missil

    # pygame.draw.rect(tela, (0, 0, 0), jogador_rect, 4)
    # pygame.draw.rect(tela, (0, 0, 0), inimigo_rect, 4)
    # pygame.draw.rect(tela, (0, 0, 0), missil_rect, 4)

    score_text = font.render("Pontuação: {}".format(pontos), True, WHITE)
    tela.blit(score_text, (10, 10))


    tela.blit(inimigo, (pos_inimigox, pos_inimigoy))
    tela.blit(missil, (pos_missilx, pos_missily))
    tela.blit(jogador, (pos_jogadorx, pos_jogadory))

    

    pygame.display.update()

