import pygame
import Mapa
import Mapa_matriz
import Telas
import Sprites

pygame.init()
TLargura = 1216
TAltura = 704
JLargura = 58
JAltura = 68
# janela
tela = pygame.display.set_mode([TLargura, TAltura])
pygame.display.set_caption("Resgate do coração")
pygame.display.set_icon(pygame.image.load("Recursos/icone.png"))
# retangulo do jogador
retJ = pygame.Rect((TLargura/2) - (JLargura/2), (TAltura/2) - (JAltura/2), JLargura, JAltura)
andando = False
Musica = True
Som = True

Quit = False
while not Quit:
    pygame.display.update()
    pygame.time.Clock().tick(30)
    #tela.fill((255, 255, 255))
    #Mapa.Desenha_coisas(tela)
    Quit = Telas.FaseJogo(tela, retJ, Musica, Som)
    Sprites.TemposDosSprites()
    Sprites.Atualiza_sprites(andando)
    Sprites.Desenha_sprites(tela)
    if Telas.fase[0] == -4 or Telas.fase[0] == -5 or Telas.fase[0] == -6:
        #pygame.draw.rect(tela, (0, 0, 255), retJ)
        Sprites.Player_sprite(retJ, tela)
        Sprites.Status(tela)

    chave = pygame.key.get_pressed()
    if chave[pygame.K_w]:
        Mapa.Move_mapa(retJ, Mapa.velocidade, Som, direcao="cima")
        andando = True
    if chave[pygame.K_s]:
        Mapa.Move_mapa(retJ, Mapa.velocidade, Som, direcao="baixo")
        andando = True
    if chave[pygame.K_a]:
        Mapa.Move_mapa(retJ, Mapa.velocidade, Som, direcao="esquerda")
        andando = True
    if chave[pygame.K_d]:
        Mapa.Move_mapa(retJ, Mapa.velocidade, Som, direcao="direita")
        andando = True

    if Telas.fase[0] == -4:
        mapa = Mapa_matriz.Matriz_mapa1
    elif Telas.fase[0] == -5:
        mapa = Mapa_matriz.Matriz_mapa2
    elif Telas.fase[0] == -6:
        mapa = Mapa_matriz.Matriz_mapa3
    else:
        mapa = None
    Mapa.Bau(retJ, Som)
    Mapa.Vida(retJ, Som)
    Mapa.InimigoH(retJ, mapa, Som)
    Mapa.InimigoV(retJ, mapa, Som)
    Mapa.Espinho(retJ, mapa, Som)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Telas.Som_pagina.play()
                Telas.fase[0] = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                andando = False
        if event.type == pygame.QUIT:
            Quit = True

pygame.quit()