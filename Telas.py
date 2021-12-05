import pygame
import Mapa
import Mapa_matriz

pygame.init()
fase = [1]
Som_pagina = pygame.mixer.Sound("Recursos/sons e musicas/PassandoAPagina.wav")
font = pygame.font.SysFont('Arial', 25, True, False)


def FaseJogo(screen, retjogador, musica, som):
    Q = False
    # menu
    if fase[0] == 1:
        # finaliza
        Mapa.Deletar_mapa()
        pygame.mixer.music.stop()
        # inicia
        if musica:
            pygame.mixer.music.load("Recursos/sons e musicas/menu_cutscene_tema_Vashti_Bunyan_If_I_Were_Same_But_Different.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
        Mapa.Vidas = ["vida", "vida", "vida"]
        fase[0] = 5
    elif fase[0] == -1:
        Q = main_menu(screen, som)
    # cutscene 1
    elif fase[0] == 2:
        Q = cutscene1(screen, som)
    # opçoes
    elif fase[0] == 3:
        Q = options(screen, som)
    # fase 1
    elif fase[0] == 4:
        # finaliza
        Mapa.Deletar_mapa()
        pygame.mixer.music.stop()
        # inicia
        if musica:
            pygame.mixer.music.load("Recursos/sons e musicas/fase1_tema.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
        Mapa.Monta_mapa(Mapa_matriz.Matriz_mapa1)
        fase[0] = -4
    # fase 2
    elif fase[0] == 5:
        # finaliza
        Mapa.Deletar_mapa()
        pygame.mixer.music.stop()
        # inicia
        if musica:
            pygame.mixer.music.load("Recursos/sons e musicas/fase2_tema.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
        Mapa.Monta_mapa(Mapa_matriz.Matriz_mapa2)
        fase[0] = -5
    # fase 3
    elif fase[0] == 6:
        # finaliza
        Mapa.Deletar_mapa()
        pygame.mixer.music.stop()
        # inicia
        if musica:
            pygame.mixer.music.load("Recursos/sons e musicas/fase3_tema.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
        Mapa.Monta_mapa(Mapa_matriz.Matriz_mapa3)
        fase[0] = -6
    # cutscene 2
    elif fase[0] == 7:
        # finaliza
        Mapa.Deletar_mapa()
        pygame.mixer.music.stop()
        # inicia
        if musica:
            pygame.mixer.music.load("Recursos/sons e musicas/menu_cutscene_tema_Vashti_Bunyan_If_I_Were_Same_But_Different.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
        fase[0] = -7
    elif fase[0] == -7:
        Q = cutscene2(screen, som)
    # cutscene 3
    elif fase[0] == 8:
        # finaliza
        Mapa.Deletar_mapa()
        pygame.mixer.music.stop()
        # inicia
        if musica:
            pygame.mixer.music.load("Recursos/sons e musicas/menu_cutscene_tema_Vashti_Bunyan_If_I_Were_Same_But_Different.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.4)
        fase[0] = -8
    elif fase[0] == -8:
        Q = cutscene3(screen, som)
    # game over
    elif fase[0] == 10:
        # finaliza
        Mapa.Deletar_mapa()
        pygame.mixer.music.stop()
        # inicia
        if musica:
            pygame.mixer.music.load("Recursos/sons e musicas/game-over.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.2)
        Mapa.Vidas = ["vida", "vida", "vida"]
        fase[0] = -10
    elif fase[0] == -10:
        Q = Fim_de_jogo(screen, som)
    # Quando perder todas as vidas
    if Mapa.Vidas == []:
        fase[0] = 10
    # passa para o proximo
    for i in range(len(Mapa.Fim)):
        if retjogador.left > Mapa.Fim[i].left and retjogador.right < Mapa.Fim[i].right and \
                retjogador.top > Mapa.Fim[i].top - 10 and retjogador.bottom < Mapa.Fim[i].bottom + 10:
            if fase[0] == -4:
                if som:
                    Som_pagina.play()
                fase[0] = 7
            if fase[0] == -5:
                if som:
                    Som_pagina.play()
                fase[0] = 8
            if fase[0] == -6:
                if som:
                    Som_pagina.play()
                fase[0] = 1
    return Q

# Menu -> 1
def main_menu(t, s):
    menu = pygame.image.load("Recursos/menu-livro.png")
    naTela = menu.subsurface((0, 0), (1216, 704))
    t.blit(naTela, (0, 0))

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(700, 215, 200, 50)
    button_2 = pygame.Rect(700, 290, 200, 50)
    button_3 = pygame.Rect(700, 365, 200, 50)

    if button_1.collidepoint((mx, my)):
        naTela = menu.subsurface((1 * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))
    if button_2.collidepoint((mx, my)):
        naTela = menu.subsurface((2 * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))
    if button_3.collidepoint((mx, my)):
        naTela = menu.subsurface((3 * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))

    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    if button_1.collidepoint((mx, my)):
        if click:
            if s:
                Som_pagina.play()
            fase[0] = 2
    if button_2.collidepoint((mx, my)):
        if click:
            if s:
                Som_pagina.play()
            fase[0] = 3

# cutscene1 -> 2
def cutscene1(t, s):
    running = True
    t.fill((0, 0, 0))
    cutscene = pygame.image.load("Recursos/Cutscene1_7-1.png")
    FrameAtualcutscene = 0

    while running:
        if FrameAtualcutscene > 5:
            running = False
            fase[0] = 4

        t.fill((0, 0, 0))
        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))
        escrever_texto('Pressione "Espaço" para continuar...', font, (255, 255, 255), t, 750, 670)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    FrameAtualcutscene += 1
                    if s:
                        Som_pagina.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    if s:
                        Som_pagina.play()
                    fase[0] = 1
        pygame.display.update()
        pygame.time.Clock().tick(30)

# cutscene 2 -> 7
def cutscene2(t, s):
    running = True
    t.fill((0, 0, 0))
    cutscene = pygame.image.load('Recursos/Cutscene2_15-1.png')
    FrameAtualcutscene = 0

    button_1 = pygame.Rect(256, 500, 700, 50)
    button_2 = pygame.Rect(256, 555, 700, 50)
    button_3 = pygame.Rect(256, 610, 700, 50)

    while running:

        mx, my = pygame.mouse.get_pos()

        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))
        if FrameAtualcutscene == 4 or FrameAtualcutscene == 10:
            escrever_texto('Selecione uma opção', font, (255, 255, 255), t, 750, 670)
        else:
            escrever_texto('Pressione "Espaço" para continuar...', font, (255, 255, 255), t, 750, 670)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    if s:
                        Som_pagina.play()
                    fase[0] = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if FrameAtualcutscene < 4:
                        FrameAtualcutscene += 1
                        if s:
                            Som_pagina.play()
                    if 6 <= FrameAtualcutscene <= 9:
                        FrameAtualcutscene += 1
                        if s:
                            Som_pagina.play()
                        if FrameAtualcutscene == 9:
                            running = False
                            fase[0] = 5

                    if FrameAtualcutscene == 5:
                        FrameAtualcutscene = 0
                        if s:
                            Som_pagina.play()
                    if FrameAtualcutscene == 9:
                        FrameAtualcutscene = 10
                        if s:
                            Som_pagina.play()
                    if FrameAtualcutscene == 14:
                        FrameAtualcutscene = 4
                        if s:
                            Som_pagina.play()
                    if 11 <= FrameAtualcutscene <= 13:
                        FrameAtualcutscene = 14
                        if s:
                            Som_pagina.play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint(mx, my):
            if click:
                if FrameAtualcutscene == 4:
                    FrameAtualcutscene = 5
                    naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                    t.blit(naTela, (0, 0))
                    if s:
                        Som_pagina.play()
                if FrameAtualcutscene == 10:
                    FrameAtualcutscene = 11
                    naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                    t.blit(naTela, (0, 0))
                    if s:
                        Som_pagina.play()
        if button_2.collidepoint(mx, my):
            if click:
                if FrameAtualcutscene == 4:
                    FrameAtualcutscene = 6
                    naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                    t.blit(naTela, (0, 0))
                    if s:
                        Som_pagina.play()
                if FrameAtualcutscene == 10:
                    FrameAtualcutscene = 12
                    naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                    t.blit(naTela, (0, 0))
                    if s:
                        Som_pagina.play()
        if button_3.collidepoint(mx, my):
            if click:
                if FrameAtualcutscene == 4:
                    FrameAtualcutscene = 9
                    naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                    t.blit(naTela, (0, 0))
                    if s:
                        Som_pagina.play()
                if FrameAtualcutscene == 10:
                    FrameAtualcutscene = 13
                    naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                    t.blit(naTela, (0, 0))
                    if s:
                        Som_pagina.play()

        pygame.display.update()
        pygame.time.Clock().tick(30)

# cutscene 3 -> 8
def cutscene3(t, s):
    running = True
    t.fill((0, 0, 0))
    cutscene = pygame.image.load('Recursos/Cutscene3_11-1.jpg')
    FrameAtualcutscene = 0

    button_1 = pygame.Rect(256, 500, 700, 50)
    button_2 = pygame.Rect(256, 555, 700, 50)
    button_3 = pygame.Rect(256, 610, 700, 50)

    while running:

        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))

        if FrameAtualcutscene == 2:
            escrever_texto('Selecione uma opção', font, (255, 255, 255), t, 750, 670)
        else:
            escrever_texto('Pressione "Espaço" para continuar...', font, (255, 255, 255), t, 750, 670)

        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    if s:
                        Som_pagina.play()
                    fase[0] = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if FrameAtualcutscene < 2:
                        FrameAtualcutscene += 1
                        if s:
                            Som_pagina.play()
                    if 3 <= FrameAtualcutscene <= 6:
                        FrameAtualcutscene += 1
                        if s:
                            Som_pagina.play()
                    if FrameAtualcutscene == 8:
                        FrameAtualcutscene = 2
                        if s:
                            Som_pagina.play()
                    if 9 <= FrameAtualcutscene <= 10:
                        FrameAtualcutscene += 1
                        if s:
                            Som_pagina.play()
                    if FrameAtualcutscene > 10:
                        FrameAtualcutscene = 2
                        if s:
                            Som_pagina.play()
                    if FrameAtualcutscene == 7:
                        running = False
                        fase[0] = 6

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if button_1.collidepoint(mx, my):
                if click:
                    if FrameAtualcutscene == 2:
                        FrameAtualcutscene = 3
                        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                        t.blit(naTela, (0, 0))
                        if s:
                            Som_pagina.play()
            if button_2.collidepoint(mx, my):
                if click:
                    if FrameAtualcutscene == 2:
                        FrameAtualcutscene = 8
                        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                        t.blit(naTela, (0, 0))
                        if s:
                            Som_pagina.play()
            if button_3.collidepoint(mx, my):
                if click:
                    if FrameAtualcutscene == 2:
                        FrameAtualcutscene = 9
                        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                        t.blit(naTela, (0, 0))
                        if s:
                            Som_pagina.play()
        pygame.display.update()
        pygame.time.Clock().tick(30)

# opções -> 3
def options(t, s):
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
                if s:
                    Som_pagina.play()
                fase[0] = -1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

# Game Over
def Fim_de_jogo(t, s):
    t.fill((0, 0, 0))
    escrever_texto("Fim de Jogo", font, (255, 255, 255), t, 530, 250)
    escrever_texto('Pressione "Espaço" para voltar ao menu', font, (255, 255, 255), t, 720, 670)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                if s:
                    Som_pagina.play()
                fase[0] = 1

def escrever_texto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)