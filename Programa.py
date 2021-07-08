import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

pygame.init()

# Funçoes


def aleatorioDecimal(v, v2):
    valor = randint(v, v2)
    return (valor // 10 * 10)


def almenta_cobra(lista):
    cores = {'verde': (0, 255, 0), 'amarelo': (255, 255, 0), 'vermelho': (255, 0, 0), 'roxo': (255, 0, 255)}
    cor = 'verde'
    for c, xy in enumerate(lista):
        if c >= 30:
            cor = 'roxo'
        elif c >= 20:
            cor = 'vermelho'
        elif c >= 10:
            cor = 'amarelo'
        else:
            pass

        pygame.draw.circle(tela, cores[cor], (xy[0], xy[1]), 10)


def reniciar_jogo():
    global pontos, comprimento_cobra, VELOCIDADE, x_cobra, y_cobra, appleY, appleX, Morreu
    pos_cobra.clear()
    cabeça_cobra.clear()
    pontos = 0
    comprimento_cobra = 5
    VELOCIDADE = 10
    x_cobra = 200
    y_cobra = 200
    appleY = aleatorioDecimal(0, altura-15)
    appleX = aleatorioDecimal(0, largura-15)
    Morreu = False

# tela

largura = 900
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Python Cobra')

# Musica de fundo

Musica_fundo = pygame.mixer.music.load('BoxCat_Games_-_Mission.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

# Musicas de efeitos
Musica_point = pygame.mixer.Sound('smw_coin.wav')
Musica_point.set_volume(1)
Musica_point2 = pygame.mixer.Sound('smw_1-up.wav')
Musica_point2.set_volume(1)
Musica_derrota = pygame.mixer.Sound('smw_game_over.wav')
Musica_derrota.set_volume(1)


# Cobra
x_cobra = 200
y_cobra = 200
pos_cobra = list()
comprimento_cobra = 5

Morreu = False

# maçã

appleX = aleatorioDecimal(20, largura-40)
appleY = aleatorioDecimal(20, altura-40)

# Parede
parede_Tam = 10
parede_Spaco = 100
# Movimento

VELOCIDADE = 3
FPS = 120

PARADO = -1
UP = 0
LEFT = 1
RIGHT = 2
DOWM = 3

movimento = LEFT

# Clock
Clock = pygame.time.Clock()

# Texto
font_pontos = pygame.font.SysFont('Cambria', 40, True, True)
font_Derrota = pygame.font.SysFont('Impact', 100, False, False)
font_Recomeçar = pygame.font.SysFont('arial', 20, True, True)
cor_dos_pontos = (20, 245, 102)

pontos = 0
while True:
    tela.fill((0, 0, 0))
    Clock.tick(FPS)

    # Marcador de pontos
    if pontos == 10:
        cor_dos_pontos = (200, 245, 20)
    elif pontos == 20:
        cor_dos_pontos = (255, 20, 20)
    elif pontos == 25:
        cor_dos_pontos = (200, 85, 200)
    elif pontos == 30:
        cor_dos_pontos = (255, 0, 255)
    txt_Formatado = font_pontos.render(f'Pontos {pontos}', True, cor_dos_pontos)

    # Eventos feitos
    Enter = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if movimento != DOWM:
                if event.key == K_UP:
                    movimento = UP
            if movimento != RIGHT:
                if event.key == K_LEFT:
                    movimento = LEFT
            if movimento != LEFT:
                if event.key == K_RIGHT:
                    movimento = RIGHT
            if movimento != UP:
                if event.key == K_DOWN:
                    movimento = DOWM


    # Teclas de movimento

    if movimento == UP:
        y_cobra -= VELOCIDADE
    if movimento == DOWM:
        y_cobra += VELOCIDADE
    if movimento == LEFT:
        x_cobra -= VELOCIDADE
    if movimento == RIGHT:
        x_cobra += VELOCIDADE

    # Limite de tela

    if y_cobra < 0:
        y_cobra -= VELOCIDADE
        y_cobra = altura-10
    if y_cobra > altura:
        y_cobra += VELOCIDADE
        y_cobra = 10
    if x_cobra < 0:
        x_cobra -= VELOCIDADE
        x_cobra = largura-10
    if x_cobra > largura:
        x_cobra += VELOCIDADE
        x_cobra = 10

    # Objetos
    cobra = pygame.draw.circle(tela, (0, 255, 0), (x_cobra, y_cobra), 10)
    Apple = pygame.draw.circle(tela, (255, 0, 0), (appleX, appleY), 7)
    AppleGold = pygame.draw.circle(tela, (205, 201, 0), (-10, -10), 10)

    # Paredes
    parede1x = pygame.draw.line(tela, (0, 255, 0), (0, 0), (largura/2 - parede_Spaco, 0), 10)
    parede2x = pygame.draw.line(tela, (0, 255, 0), (largura/2 + parede_Spaco, 0), (largura, 0), 10)
    parede3x = pygame.draw.line(tela, (0, 255, 0), (largura, 0), (largura, altura / 2 - parede_Spaco), 10)
    parede4x = pygame.draw.line(tela, (0, 255, 0), (largura, altura / 2 + parede_Spaco), (largura, altura), 10)
    parede1y = pygame.draw.line(tela, (0, 255, 0), (0, 0), (0, altura / 2 - parede_Spaco), 10)
    parede2y = pygame.draw.line(tela, (0, 255, 0), (0, altura / 2 + parede_Spaco), (0, altura), 10)
    parede3y = pygame.draw.line(tela, (0, 255, 0), (0, altura), (largura / 2 - parede_Spaco, altura), 10)
    parede4y = pygame.draw.line(tela, (0, 255, 0), (largura / 2 + parede_Spaco, altura), (largura, altura), 10)

    if pontos == 15 or pontos == 30 or pontos == 45:
        AppleGold = pygame.draw.circle(tela, (205, 201, 0), (appleX, appleY), 10)

    # Pega maçã

    if cobra.colliderect(AppleGold):
        Musica_point2.play()
        AppleGold = pygame.draw.circle(tela, (205, 201, 0), (appleX, appleY), 10)
        comprimento_cobra += 3
        pontos += 3
        VELOCIDADE += 0.5
        appleX = aleatorioDecimal(10, largura-10)
        appleY = aleatorioDecimal(10, altura-10)

    elif cobra.colliderect(Apple):
        VELOCIDADE += 0.2
        comprimento_cobra += 1
        pontos += 1
        Musica_point.play()
        appleX = aleatorioDecimal(20, largura-20)
        appleY = aleatorioDecimal(200, altura-20)

    # posição cobra
    cabeça_cobra = list()
    cabeça_cobra.append(x_cobra)
    cabeça_cobra.append(y_cobra)

    if len(pos_cobra) > comprimento_cobra:
        del pos_cobra[0]

    pos_cobra.append(cabeça_cobra)

    almenta_cobra(pos_cobra)

    # mote por colizão parede
    if (cobra.colliderect(parede1x) or cobra.colliderect(parede2x)
    or cobra.colliderect(parede3x) or cobra.colliderect(parede4x)
    or cobra.colliderect(parede1y) or cobra.colliderect(parede2y)
    or cobra.colliderect(parede3y) or cobra.colliderect(parede4y)):
        Morreu = True

    # morte da cobra
    if pos_cobra.count(cabeça_cobra) > 1 or Morreu == True:
        reniciar_jogo()
        Morreu = True
        while Morreu:
            tela.fill((40, 40, 40))
            fim = font_Derrota.render('     PERDEU', True, (255, 0, 0))
            recomeçar = font_Recomeçar.render('R para Recomeçar', True, (255, 255, 0))
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    pygame.mixer.music.play()
                    if event.key == K_r:
                        Morreu = False
                        VELOCIDADE = 3
                        cor_dos_pontos = (20, 245, 102)

            Musica_derrota.play()
            tela.blit(recomeçar, (largura/2-50, altura/2))
            tela.blit(fim, (0, altura/2-120))
            pygame.display.update()

    tela.blit(txt_Formatado, (500, 20))
    pygame.display.update()