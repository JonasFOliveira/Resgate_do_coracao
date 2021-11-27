import pygame
import Mapa

fase = [1]
def FaseJogo(screen, retjogador):
    Q =False
    if fase[0] == 1:
        Mapa.Deletar_mapa()
        Q = Menu(screen)
    elif fase[0] == 2:
        Mapa.Deletar_mapa()
        Mapa.Monta_mapa()
        fase[0] = -2
    for i in range(len(Mapa.Fim)):
        if retjogador.left > Mapa.Fim[i].left and retjogador.right < Mapa.Fim[i].right and retjogador.top > Mapa.Fim[i].top and retjogador.bottom < Mapa.Fim[i].bottom:
            if fase[0] == -2:
                fase[0] = 1
    return Q


def Menu(t):
    start = pygame.Rect(510, 270, 180, 60)
    pygame.draw.rect(t, (50, 50, 50), start)
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            X, Y = pygame.mouse.get_pos()
            if start.x < X < (start.x + 180) and start.y < Y < (start.y + 60):
                fase[0] = 2
        if evento.type == pygame.QUIT:
            return True

