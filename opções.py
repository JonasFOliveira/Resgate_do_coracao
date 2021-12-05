def options(t, s, m):
    t.fill((0, 0, 0))
    options = pygame.image.load("Recursos/Opcoes.png")
    FrameAtual = 0

    button_1 = pygame.Rect(600, 215, 300, 50)
    button_2 = pygame.Rect(600, 290, 300, 50)
    button_3 = pygame.Rect(600, 365, 300, 50)

    Running = True
    while Running:
        naTela = options.subsurface((FrameAtual*1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))

        mx, my = pygame.mouse.get_pos()
        if FrameAtual == 0:
            if s:
                escrever_texto('ON', font, (0, 0, 0), t, 790, 308)
            else:
                escrever_texto('OFF', font, (0, 0, 0), t, 790, 308)
            if m:
                escrever_texto('ON', font, (0, 0, 0), t, 850, 230)
            else:
                escrever_texto('OFF', font, (0, 0, 0), t, 850, 230)


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if FrameAtual == 0:
                        if s:
                            Som_pagina.play()
                        Running = False
                        fase[0] = 1
                    if FrameAtual == 1:
                        if s:
                            Som_pagina.play()
                        FrameAtual = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint(mx, my) and FrameAtual == 0:
            if click:
                if m:
                    m = False
                else:
                    m = True
        if button_2.collidepoint(mx, my) and FrameAtual == 0:
            if click:
                if s:
                    s = False
                else:
                    s = True
        if button_3.collidepoint(mx, my) and FrameAtual == 0:
            if click:
                FrameAtual = 1
                if s:
                    Som_pagina.play()
        pygame.display.update()
        pygame.time.Clock().tick(30)
