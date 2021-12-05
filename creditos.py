def creditos(t, s):
    t.fill((0, 0, 0))
    creditos = pygame.image.load("Recursos/Creditos.png")
    FrameAtual = 0



    button_1 = pygame.Rect(700, 215, 400, 50)

    Running = True
    while Running:

        mx, my = pygame.mouse.get_pos()

        naTela = creditos.subsurface((FrameAtual * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if FrameAtual == 0:
                        if s:
                            Som_pagina.play()
                        fase[0] = -1
                        Q = main_menu(t, s)
                        Running = False
                        return Q
                    if FrameAtual == 1:
                        if s:
                            Som_pagina.play()
                        FrameAtual = 0


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if button_1.collidepoint(mx, my):
                if click:
                    if FrameAtual == 0:
                        if s:
                            Som_pagina.play()
                        FrameAtual = 1
                    else:
                        if s:
                            Som_pagina.play()
                        FrameAtual = 0


        pygame.display.update()
        pygame.time.Clock().tick(30)
