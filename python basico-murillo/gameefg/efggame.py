import pygame

#inicia o pygame e criar a tela 

pygame.init()

#configura a tela do jogo 

display = pygame.display.set_mode([800,400])
pygame.display.set_caption('efGGame')
 
 #criar o sprite do mario 
 
mario = pygame.sprite.Sprite()
mario.image = pygame.image.load("D:\Estudos\python basico-murillo\gameefg\player\mario.png")
mario.image = pygame.transform.scale(mario.image,[100,100])
mario.rect = mario.image.get_rect()
mario.rect.topleft = (100,200)

# carregar e reproduzir a musica de fundo 

pygame.mixer.music.load("D:\Estudos\python basico-murillo\gameefg\Audio\mario.mp3")
pygame.mixer.music.load('D:\Estudos\python basico-murillo\gameefg\Audio\mario.mp3')
pygame.mixer.music.play(-1)

#carregamento da imagem de fundo 

backgrond = pygame.image.load('D:\Estudos\python basico-murillo\gameefg\Fundo\Background.jpg')

#variavel para controlar o loop principal do jogo 

gameloop = True

#loop principal do jogo

if __name__=='__main__':
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False

        #capturar as teclas pressionadas
        keys = pygame.key.get_pressed()

        #mover o mariocom base nas teclas declaradas
        if keys[pygame.K_a]:
            mario.rect.x -= 1
        elif keys[pygame.K_d]:
            mario.rect.x += 1
        
        #desenhar o fundo 
        display.blit(backgrond,(0,0))

        #desenhar o retangulo do mario diretamente na tela 
        display.blit(mario.image, mario.rect)

        # atualizar atela 
        pygame.display.update()
