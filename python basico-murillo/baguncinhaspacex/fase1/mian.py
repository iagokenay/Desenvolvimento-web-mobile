import pygame
import sys
import random 

# Inicialização do Pygame 
pygame.init()
# Definição de variáveis globais
WIDTH, HEIGHT = 800, 600
FPS = 60
# Definição de cores
WHITE = (255, 255, 255)
# Inicialização da janela e carregamento de imagens
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Baguncinha Space X")
background = pygame.image.load("D:\Estudos\python basico-murillo/baguncinhaspacex/fase1/fundo.png").convert()
player_image = pygame.image.load("D:\Estudos\python basico-murillo/baguncinhaspacex/fase1/jogador.png").convert_alpha()
enemy_image = pygame.image.load("D:\Estudos\python basico-murillo/baguncinhaspacex/fase1/inimigo.png").convert_alpha()

pygame.mixer.music.load('D:\Estudos\python basico-murillo/baguncinhaspacex/fase1/Stalin loves disco.mp3')
pygame.mixer.music.play(-1)#para reproduzir a musica continua -1

# Definição da nave do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_image, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5
# Definição do projétil
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10), pygame.SRCALPHA)
        pygame.draw.rect(self.image, WHITE, (0, 0, 5, 10))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
# Definição do inimigo (sanduíche)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_image, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(-40, 0)
        self.speed_y = random.randint(1, 5)
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-40, 0)
            self.rect.x = random.randint(0, WIDTH - 50)
# Inicialização
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
score = 0 # Variável para armazenar a pontuação
font = pygame.font.Font(None, 36) # Define uma fonte para exibir a pontuação
for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
# Loop do jogo
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
    all_sprites.update()

    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
      
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        score += 10 # Incrementa a pontuação quando um inimigo é atingido
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
            running = False
    # Desenha o fundo
    screen.blit(background, (0, 0))
    # Desenha os sprites na tela
    all_sprites.draw(screen)
    # Exibe a pontuação na tela
    score_text = font.render("Pontuação: {}".format(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    # Atualiza a tela
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()