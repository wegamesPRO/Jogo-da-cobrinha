from random import randint
import pygame


def aleatorioDecimal(v, v2):
    valor = randint(v, v2)
    return valor // 10 * 10


def almenta_cobra(lugar, lista, cor=(0, 255, 0)):
    for c, xy in enumerate(lista):
        cobra = pygame.draw.rect(lugar, cor, (xy[c], xy[c], 10, 10))
        return cobra