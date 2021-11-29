import pygame
from spritesheet import SpriteSheet, Origin
import Mapa
import Mapa_matriz

pygame.init()
fase = [1]
Som_pagina = pygame.mixer.Sound("Recursos/PassandoAPagina.wav")
font = pygame.font.SysFont('Arial', 25, True, False)


def FaseJogo(screen, retjogador):
    Q =False
    if fase[0] == 1:
        Mapa.Deletar_mapa()
        Mapa.Vidas = ["vida", "vida", "vida"]
        Q = main_menu(screen)
    elif fase[0] == 2:
        Q = cutscene1(screen)
    elif fase[0] == 3:
        Q = options(screen)
    elif fase[0] == 4:
        Mapa.Deletar_mapa()
        Mapa.Monta_mapa(Mapa_matriz.Matriz_mapa1)
        fase[0] = -4
    if Mapa.Vidas == []:
        fase[0] = 1
    # passa para o proximo
    for i in range(len(Mapa.Fim)):
        if retjogador.left > Mapa.Fim[i].left and retjogador.right < Mapa.Fim[i].right and retjogador.top > Mapa.Fim[i].top -10 and retjogador.bottom < Mapa.Fim[i].bottom +10:
            if fase[0] == -4:
                fase[0] = 1
    return Q

# Menu -> 1
def main_menu(t):
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    print('comecei')
    menu = SpriteSheet('Recursos/menu-livro.png', 4, 1)
    menu.blit(t, 0, (0, 0), Origin.TopLeft)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(700, 215, 200, 50)
    button_2 = pygame.Rect(700, 290, 200, 50)
    button_3 = pygame.Rect(700, 365, 200, 50)

    if button_1.collidepoint((mx, my)):
        menu.blit(t, 1, (0, 0), Origin.TopLeft)
    if button_2.collidepoint((mx, my)):
        menu.blit(t, 2, (0, 0), Origin.TopLeft)
    if button_3.collidepoint((mx, my)):
        menu.blit(t, 3, (0, 0), Origin.TopLeft)

    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
                
    if button_1.collidepoint((mx, my)):
        if click:
            fase[0] = 2
    if button_2.collidepoint((mx, my)):
        if click:
            fase[0] = 3




# cutscene1 -> 2
def cutscene1(t):
    running = True
    menu = False
    cutscene = SpriteSheet("Recursos/Cutscene1.png", 7, 1)
    plaquinhas = SpriteSheet("Recursos/Placa_Cutscene1.png", 7, 1)
    FrameAtualcutscene = 0

    while running:
        if FrameAtualcutscene > 5:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    FrameAtualcutscene += 1
                    Som_pagina.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = True
                    fase[0] = 1

        t.fill((0, 0, 0))
        cutscene.blit(t, FrameAtualcutscene, (64 * 2, 64), Origin.TopLeft)
        plaquinhas.blit(t, FrameAtualcutscene, (64 * 5, 64 * 7), Origin.TopLeft)
        escrever_texto('Pressione "Espaço" para continuar...', font, (255, 255, 255), t, 750, 670)

        pygame.display.update()
        pygame.time.Clock().tick(60)

    if not menu:
        fase[0] = 4

# opções -> 3
def options(t):
    t.fill((0, 0, 0))
    button_1 = pygame.Rect(50, 100, 200, 50)
    button_2 = pygame.Rect(50, 200, 200, 50)

    pygame.draw.rect(t, (255, 0, 0), button_1)
    pygame.draw.rect(t, (255, 0, 0), button_2)

    escrever_texto('Efeitos', font, (255, 255, 255), t, 50, 100)
    escrever_texto('Musica', font, (255, 255, 255), t, 50, 200)

    escrever_texto('Opções', font, (255, 255, 255), t, 20, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                fase[0] = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True


def escrever_texto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)