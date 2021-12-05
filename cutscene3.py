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
                        fase[0] = 7

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
