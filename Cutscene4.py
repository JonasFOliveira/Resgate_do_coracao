def cutscene4(t, s):
    running = True
    t.fill((0, 0, 0))
    cutscene = pygame.image.load("Recursos/cutscene4_43_1.png.png")
    FrameAtualcutscene = 0
    
    button_1 = pygame.Rect(256, 525, 700, 50)
    button_2 = pygame.Rect(256, 575, 700, 50)
    
    while running:
        
        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
        t.blit(naTela, (0, 0))

        if FrameAtualcutscene == 3 or FrameAtualcutscene == 11:
            
            escrever_texto('Selecione uma opção', font, (255, 255, 255), t, 750, 670)
        else:
            escrever_texto('Pressione "Espaço" para continuar...', font, (255, 255, 255), t, 750, 670)
            
        mx, my = pygame.mouse.get_pos()
         
        click = False
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    if FrameAtualcutscene <= 2:
                        FrameAtualcutscene += 1
                        if s:
                            Som_pagina.play()
                    
                    if FrameAtualcutscene == 4:
                               FrameAtualcutscene = 3
                               if s:
                                   Som_pagina.play()      
                    
                    if 5 <= FrameAtualcutscene <= 11:                 
                        FrameAtualcutscene += 1       
                        if s:
                           Som_pagina.play()
                            
                           if FrameAtualcutscene == 42:
                               running = False
                               fase[0] = 9 
                            
                                                                           
                                       
                    if FrameAtualcutscene == 12:
                              FrameAtualcutscene = 11
                              if s:
                                  Som_pagina.play()      
                    
                            
                    if FrameAtualcutscene >= 13:
                             FrameAtualcutscene += 1
                             if s:
                                 Som_pagina.play()              
                            
                                                     
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True                    
                  
                    
            if button_1.collidepoint(mx, my):
                if click:
                    if FrameAtualcutscene == 3:
                        FrameAtualcutscene = 5
                        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                        t.blit(naTela, (0, 0))
                        if s:
                            Som_pagina.play()     
                            
                    if FrameAtualcutscene == 11:
                        FrameAtualcutscene = 13
                        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                        t.blit(naTela, (0, 0))
                        if s:
                            Som_pagina.play()     
              
            if button_2.collidepoint(mx, my):
                if click:        
                    
                    if FrameAtualcutscene == 3:
                        FrameAtualcutscene = 4
                        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                        t.blit(naTela, (0, 0))
                        if s:
                            Som_pagina.play()       
                    
                    
                    if FrameAtualcutscene == 11:
                        FrameAtualcutscene = 12
                        naTela = cutscene.subsurface((FrameAtualcutscene * 1216, 0), (1216, 704))
                        t.blit(naTela, (0, 0))
                        if s:
                            Som_pagina.play()                           
                    
            pygame.display.update()
            pygame.time.Clock().tick(30)                    
                    
