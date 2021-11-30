import pygame
import Mapa
import Telas
from spritesheet import SpriteSheet, Origin

# Tempo dos sprites
sprites_tempo = {"Abelha": 0, "Aranha": 0}
# Qual sprite está ativo
sprites_ativos = {"Abelha": 0, "Aranha": 0}

# Sprites
# Inimigo Vertical
IV = pygame.sprite.Sprite()
IV.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
IV.rect = pygame.Rect(0, 0, 0, 0)
# Inimigo Horizontal
IH = pygame.sprite.Sprite()
IH.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
IH.rect = pygame.Rect(0, 0, 0, 0)
# Parede
Pa = pygame.sprite.Sprite()
Pa.image = pygame.image.load(("Recursos/Arvores.png"))
Pa.image = pygame.transform.scale(Pa.image, (120, 120))
Pa.rect = pygame.Rect(0, 0, 0, 0)

# Grupo de todos os sprites
Grupo_sprites_IV = pygame.sprite.Group()
Grupo_sprites_IV.add(IV)
Grupo_sprites_IH = pygame.sprite.Group()
Grupo_sprites_IH.add(IH)
Grupo_sprites_Pa = pygame.sprite.Group()
Grupo_sprites_Pa.add(Pa)

def TemposDosSprites():
    # Abelha
    sprites_tempo["Abelha"] += 1
    if sprites_tempo["Abelha"] > 3:
        sprites_tempo["Abelha"] = 1
    # Aranha
    sprites_tempo["Aranha"] += 1
    if sprites_tempo["Aranha"] > 3:
        sprites_tempo["Aranha"] = 1

# Atualiza sprites
def Atualiza_sprites():
    # Abelha
    if sprites_tempo["Abelha"] == 3:
        sprites_ativos["Abelha"] += 1
        if sprites_ativos["Abelha"] > 1:
            sprites_ativos["Abelha"] = 0
    # Aranha
    if sprites_tempo["Aranha"] == 3:
        sprites_ativos["Aranha"] += 1
        if sprites_ativos["Aranha"] > 8:
            sprites_ativos["Aranha"] = 0

# Desenha todos os sprites
def Desenha_sprites(screen):
    # Inimigo Vertical
    for i in range(len(Mapa.InimigosV)):
        IV.rect = Mapa.InimigosV[i]
        # Abelha
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = pygame.image.load("Recursos/Abelha_Baixo_4-1.png").subsurface(
                    (sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IV.image = pygame.image.load("Recursos/Abelha_Cima_4-1.png").subsurface(
                    (sprites_ativos["Abelha"] * 64, 0), (64, 64))
        '''
        # Aranha
        if Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = pygame.image.load("Recursos/Aranha_Baixo_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IV.image = pygame.image.load("Recursos/Aranha_Cima_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
        '''
        IV.image = pygame.transform.scale(IV.image, (120, 120))
        Grupo_sprites_IV.draw(screen)

    # Inimigo Horizontal
    for i in range(len(Mapa.InimigosH)):
        IH.rect = Mapa.InimigosH[i]
        # Abelha
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoH[i] > 0:
                IH.image = pygame.image.load("Recursos/Abelha_Direita_4-1.png").subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IH.image = pygame.image.load("Recursos/Abelha_Esquerda_4-1.png").subsurface((sprites_ativos["Abelha"] *64, 0), (64, 64))
        '''
        # Aranha
        if Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IH.image = pygame.image.load("Recursos/Aranha_Direita_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IH.image = pygame.image.load("Recursos/Aranha_Esquerda_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
        '''
        IH.image = pygame.transform.scale(IH.image, (120, 120))
        Grupo_sprites_IH.draw(screen)

    # Parede
    for i in range(len(Mapa.Paredes)):
        Pa.rect = Mapa.Paredes[i]
        Grupo_sprites_Pa.draw(screen)