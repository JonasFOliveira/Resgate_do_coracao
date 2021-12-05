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
