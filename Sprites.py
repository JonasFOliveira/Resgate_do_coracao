import pygame
import Mapa
import Telas

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
Pa.rect = pygame.Rect(0, 0, 0, 0)
# Baú
Bau = pygame.sprite.Sprite()
Bau.image = pygame.image.load("Recursos/Bau.png")
Bau.image = pygame.transform.scale(Bau.image, (90, 90))
Bau.rect = pygame.Rect(0, 0, 0, 0)
# Chave
Ch = pygame.sprite.Sprite()
Ch.image = pygame.image.load("Recursos/Chave.png")
Ch.image = pygame.transform.scale(Ch.image, (85, 87))
Ch.rect = pygame.Rect(0, 0, 0, 0)
# Coração
Co = pygame.sprite.Sprite()
Co.image = pygame.image.load("Recursos/Coracao_3-1.png").subsurface((0, 0), (59, 64))
Co.image = pygame.transform.scale(Co.image, (37, 40))
Co.rect = pygame.Rect(0, 0, 0, 0)

# Grupo de todos os sprites
# Inimigo Vertical
Grupo_sprites_IV = pygame.sprite.Group()
Grupo_sprites_IV.add(IV)
# Inimigo Horizontal
Grupo_sprites_IH = pygame.sprite.Group()
Grupo_sprites_IH.add(IH)
# Parede
Grupo_sprites_Pa = pygame.sprite.Group()
Grupo_sprites_Pa.add(Pa)
#Baú
Grupo_sprites_Bau = pygame.sprite.Group()
Grupo_sprites_Bau.add(Bau)
# Chave
Grupo_sprites_Ch = pygame.sprite.Group()
Grupo_sprites_Ch.add(Ch)
# Coração
Grupo_sprites_Co = pygame.sprite.Group()
Grupo_sprites_Co.add(Co)

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
        if sprites_ativos["Aranha"] == 0:
            sprites_ativos["Aranha"] = 4
        elif sprites_ativos["Aranha"] == 4:
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
        '''# Aranha
        elif Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = pygame.image.load("Recursos/Aranha_Baixo_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IV.image = pygame.image.load("Recursos/Aranha_Cima_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))'''
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
        elif Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoH[i] > 0:
                IH.image = pygame.image.load("Recursos/Aranha_Direita_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IH.image = pygame.image.load("Recursos/Aranha_Esquerda_9-1.png").subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))'''
        IH.image = pygame.transform.scale(IH.image, (120, 120))
        Grupo_sprites_IH.draw(screen)

    # Parede
    for i in range(len(Mapa.Paredes)):
        Pa.rect = Mapa.Paredes[i]
        # Arvore
        if Telas.fase[0] == -4:
            Pa.image = pygame.image.load("Recursos/Arvores.png")
        '''# Pedras
        elif Telas.fase[0] == -5:
            Pa.image = pygame.image.load("Recursos/Pedras.png")'''
        Pa.image = pygame.transform.scale(Pa.image, (120, 120))
        Grupo_sprites_Pa.draw(screen)

    # Chave
    for i in range(len(Mapa.Chaves)):
        Ch.rect = Mapa.Chaves[i]
        Grupo_sprites_Ch.draw(screen)

    # Baú
    for i in range(len(Mapa.Baus)):
        Bau.rect = Mapa.Baus[i]
        Grupo_sprites_Bau.draw(screen)

    # Coração
    for i in range(len(Mapa.coracao)):
        Co.rect = Mapa.coracao[i]
        Grupo_sprites_Co.draw(screen)