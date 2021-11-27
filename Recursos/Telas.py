import pygame, sys
import Mapa

fase = [1]
font = pygame.font.SysFont('Arial', 25, True, False)
def FaseJogo(screen, retjogador):
    Q =False
    if fase[0] == 1:
        Mapa.Deletar_mapa()
        Q = main_menu(screen)
    elif fase[0] == 2:
        Mapa.Deletar_mapa()
        Mapa.Monta_mapa()
        fase[0] = -2
    for i in range(len(Mapa.Fim)):
        if retjogador.left > Mapa.Fim[i].left and retjogador.right < Mapa.Fim[i].right and retjogador.top > Mapa.Fim[i].top and retjogador.bottom < Mapa.Fim[i].bottom:
            if fase[0] == -2:
                fase[0] = 1
    return Q


def main_menu(t):
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    t.fill((0, 0, 0))
    escrever_texto('Menu Principal', f, (255, 255, 255), t, 20, 20)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(50, 100, 200, 50)
    button_2 = pygame.Rect(50, 200, 200, 50)

    if button_1.collidepoint((mx, my)):
        if click:
            fase[0] = 4
    if button_2.collidepoint((mx, my)):
        if click:
            fase[0] = 3
    pygame.draw.rect(t, (255, 0, 0), button_1)
    escrever_texto('Botão 1', f, (255, 255, 255), t, 50, 100)
    pygame.draw.rect(t, (255, 0, 0), button_2)
    escrever_texto('Botão 2', f, (255, 255, 255), t, 50, 200)




def escrever_texto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)