def cutscene1():
    running = True
    screen.fill((0, 0, 0))
    cutscene = SpriteSheet('Recursos/Cutscene1_7-1.png', 7, 1)
    FrameAtualcutscene = 0

    while running:
        if FrameAtualcutscene > 5:
            running = False

        screen.fill(constantes.Preto)
        cutscene.blit(screen, FrameAtualcutscene, (0, 0), Origin.TopLeft)
        escrever_texto('Pressione "Espaço" para continuar...', font, constantes.Branco, screen, 750, 670)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FrameAtualcutscene += 1
                    musica.play()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        fpsClock.tick(60)
