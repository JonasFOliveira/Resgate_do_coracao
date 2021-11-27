import pygame
import Mapa
import Telas

pygame.init()

tela = pygame.display.set_mode([1200, 600])
retJ = pygame.Rect(585, 285, 30, 30)

Quit = False
while not Quit:
    pygame.display.update()
    pygame.time.Clock().tick(60)
    tela. fill((255, 255, 255))
    Quit = Telas.FaseJogo(tela, retJ)
    Mapa.Desenha_coisas(tela)
    if Telas.fase[0] == -4:
        pygame.draw.rect(tela, (0, 0, 255), retJ)

    chave = pygame.key.get_pressed()
    if chave[pygame.K_w]:
        Mapa.Move_mapa(retJ, direcao="cima")
    if chave[pygame.K_s]:
        Mapa.Move_mapa(retJ, direcao="baixo")
    if chave[pygame.K_a]:
        Mapa.Move_mapa(retJ, direcao="esquerda")
    if chave[pygame.K_d]:
        Mapa.Move_mapa(retJ, direcao="direita")

    Mapa.Bau(retJ)
    Mapa.Inimigo(retJ)
    Mapa.Espinho(retJ)

    if Mapa.Vidas == []:
        Telas.fase[0] = 1
        Mapa.Vidas = ["vida", "vida", "vida"]

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Telas.fase[0] = 1
        if event.type == pygame.QUIT:
            Quit = True

pygame.quit()