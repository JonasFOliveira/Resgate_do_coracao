def cutscene2():
    running = True
    cutscene = SpriteSheet('Recursos/cutscene2_15-1.png', 15, 1)

    FrameAtualcutscene = 0

    button_1 = pygame.Rect(256, 500, 700, 50)
    button_2 = pygame.Rect(256, 555, 700, 50)
    button_3 = pygame.Rect(256, 610, 700, 50)

    while running:

        mx, my = pygame.mouse.get_pos()

        cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if FrameAtualcutscene < 4:
                        FrameAtualcutscene += 1
                        musica.play()
                    if 6 <= FrameAtualcutscene <= 9:
                        FrameAtualcutscene += 1
                        musica.play()
                        if FrameAtualcutscene == 9:
                            main_menu()

                    if FrameAtualcutscene == 5:
                        FrameAtualcutscene = 0
                        musica.play()
                    if FrameAtualcutscene == 9:
                        FrameAtualcutscene = 10
                        musica.play()
                    if FrameAtualcutscene == 14:
                        FrameAtualcutscene = 4
                        musica.play()
                    if 11 <= FrameAtualcutscene <= 13:
                        FrameAtualcutscene = 14
                        musica.play()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint(mx, my):
            if click:
                if FrameAtualcutscene == 4:
                    FrameAtualcutscene = 5
                    cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)
                    musica.play()
                if FrameAtualcutscene == 10:
                    FrameAtualcutscene = 11
                    cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)
                    musica.play()
        if button_2.collidepoint(mx, my):
            if click:
                if FrameAtualcutscene == 4:
                    FrameAtualcutscene = 6
                    cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)
                    musica.play()
                if FrameAtualcutscene == 10:
                    FrameAtualcutscene = 12
                    cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)
                    musica.play()
        if button_3.collidepoint(mx, my):
            if click:
                if FrameAtualcutscene == 4:
                    FrameAtualcutscene = 9
                    cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)
                    musica.play()
                if FrameAtualcutscene == 10:
                    FrameAtualcutscene = 13
                    cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)
                    musica.play()

        pygame.display.update()
        fpsClock.tick(30)
