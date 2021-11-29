import pygame
import Mapa
import Telas

# Tempo dos sprites
sprites_tempo = {"Abelha": 0}

# Qual sprite está ativo
sprites_ativos = {"Abelha": 0}

# Sprites
# Inimigo Vertical
IV = pygame.sprite.Sprite()
IV.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
IV.rect = pygame.Rect(0, 0, 0, 0)

# Inimigo Horizontal
IH = pygame.sprite.Sprite()
IH.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
IH.rect = pygame.Rect(0, 0, 0, 0)



# Grupo de todos os sprites
Grupo_sprites = pygame.sprite.Group()
Grupo_sprites.add(IV)
Grupo_sprites.add(IH)

def TemposDosSprites():
    sprites_tempo["Abelha"] += 1
    if sprites_tempo["Abelha"] > 2:
        sprites_tempo["Abelha"] = 1

# Atualiza sprites
def Atualiza_sprites():
    if sprites_tempo["Abelha"] == 2:
        sprites_ativos["Abelha"] += 1
        if sprites_ativos["Abelha"] > 3:
            sprites_ativos["Abelha"] = 0

# Desenha todos os sprites
def Desenha_sprites(screen):
    # Inimigo Vertical
    for i in range(len(Mapa.InimigosV)):
        IV.rect = Mapa.InimigosV[i]
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = pygame.image.load("Recursos/Abelha_Baixo_4-1.png").subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IV.image = pygame.image.load("Recursos/Abelha_Cima_4-1.png").subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
        Grupo_sprites.draw(screen)
    # Inimigo Horizontal
    for i in range(len(Mapa.InimigosH)):
        IH.rect = Mapa.InimigosH[i]
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoH[i] > 0:
                IH.image = pygame.image.load("Recursos/Abelha_Direita_4-1.png").subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IH.image = pygame.image.load("Recursos/Abelha_Esquerda_4-1.png").subsurface((sprites_ativos["Abelha"] *64, 0), (64, 64))
        Grupo_sprites.draw(screen)