import pygame
import Mapa
import Telas

# Tempo dos sprites
sprites_tempo = [0]
# Qual sprite está ativo
sprites_ativos = {"Abelha": 0, "Aranha": 0}

# Imagens
# Abelha
Abelha_Baixo = pygame.image.load("Recursos/Abelha_Baixo_4-1.png")
Abelha_Cima = pygame.image.load("Recursos/Abelha_Cima_4-1.png")
Abelha_Direita = pygame.image.load("Recursos/Abelha_Direita_4-1.png")
Abelha_Esquerda = pygame.image.load("Recursos/Abelha_Esquerda_4-1.png")
# Aranha
Aranha_Baixo = pygame.image.load("Recursos/Aranha_Baixo_9-1.png")
Aranha_Cima = pygame.image.load("Recursos/Aranha_Cima_9-1.png")
Aranha_Direita = pygame.image.load("Recursos/Aranha_Direita_9-1.png")
Aranha_Esquerda = pygame.image.load("Recursos/Aranha_Esquerda_9-1.png")
# Paredes
Arvores = pygame.image.load("Recursos/Arvores.png")
Pedras = pygame.image.load("Recursos/Pedras.png")
estalagmite = pygame.image.load("Recursos/estalagmite.png")
# Espinhos
spikes_Ativo = pygame.image.load("Recursos/spikes.png")
spikes_Desativado = pygame.image.load("Recursos/spikes.png")
# Outros
bau = pygame.image.load("Recursos/Bau.png")
Chave = pygame.image.load("Recursos/Chave.png")
Coracao = pygame.image.load("Recursos/Coracao_3-1.png")
Porta = pygame.image.load("Recursos/Porta.png")
saida = pygame.image.load("Recursos/saida.png")

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
Bau.image = bau
Bau.image = pygame.transform.scale(Bau.image, (90, 90))
Bau.rect = pygame.Rect(0, 0, 0, 0)
# Chave
Ch = pygame.sprite.Sprite()
Ch.image = Chave
Ch.image = pygame.transform.scale(Ch.image, (70, 26))
Ch.rect = pygame.Rect(0, 0, 0, 0)
# Coração
Co = pygame.sprite.Sprite()
Co.image = Coracao.subsurface((0, 0), (59, 64))
Co.image = pygame.transform.scale(Co.image, (37, 40))
Co.rect = pygame.Rect(0, 0, 0, 0)
# Porta
Por = pygame.sprite.Sprite()
Por.image = Porta
Por.image = pygame.transform.scale(Por.image, (Mapa.bloco_largura, Mapa.bloco_altura))
Por.rect = pygame.Rect(0, 0, 0, 0)
# Espinhos
Es = pygame.sprite.Sprite()
Es.image = pygame.image.load("Recursos/NADA.jpg").subsurface((0, 0), (64, 64))
Es.rect = pygame.Rect(0, 0, 0, 0)
# Fim
Fim = pygame.sprite.Sprite()
Fim.image = saida
Fim.image = pygame.transform.scale(Fim.image, (Mapa.bloco_largura, Mapa.bloco_altura))
Fim.rect = pygame.Rect(0, 0, 0, 0)


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
# Porta
Grupo_sprites_Por = pygame.sprite.Group()
Grupo_sprites_Por.add(Por)
# Espinhos
Grupo_sprites_Es = pygame.sprite.Group()
Grupo_sprites_Es.add(Es)
# Fim
Grupo_sprites_Fim = pygame.sprite.Group()
Grupo_sprites_Fim.add(Fim)

def TemposDosSprites():
    # Abelha
    sprites_tempo[0] += 1
    if sprites_tempo[0] > 2:
        sprites_tempo[0] = 1

# Atualiza sprites
def Atualiza_sprites():
    # Abelha
    if sprites_tempo[0] == 2:
        sprites_ativos["Abelha"] += 1
        if sprites_ativos["Abelha"] > 1:
            sprites_ativos["Abelha"] = 0
    # Aranha
    if sprites_tempo[0] == 2:
        if sprites_ativos["Aranha"] == 0:
            sprites_ativos["Aranha"] = 4
        elif sprites_ativos["Aranha"] == 4:
            sprites_ativos["Aranha"] = 0

# Desenha todos os sprites
def Desenha_sprites(screen):
    # Fundo
    if Telas.fase[0] == -4:
        screen.fill((79, 125, 79))
        '''elif Telas.fase == -?:
        screen.fill((109, 88, 54))
    elif Telas.fase[0] == -?:
        screen.fill((51, 48, 44))'''

    # Parede
    for i in range(len(Mapa.Paredes)):
        Pa.rect = Mapa.Paredes[i]
        # Arvore
        if Telas.fase[0] == -4:
            Pa.image = Arvores
        '''# Pedras
        elif Telas.fase[0] == -?:
            Pa.image = Pedras'''
        '''# Estalagmite
        elif Telas.fase[0] == -?:
            Pa.image = estalagmite'''
        Pa.image = pygame.transform.scale(Pa.image, (Mapa.bloco_largura, Mapa.bloco_altura))
        if Pa.rect.left > -Mapa.bloco_largura and Pa.rect.right < 1216 + Mapa.bloco_largura and Pa.rect.top > - Mapa.bloco_altura and Pa.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_Pa.draw(screen)

    # Chave
    for i in range(len(Mapa.Chaves)):
        Ch.rect = Mapa.Chaves[i]
        if Ch.rect.left > -Mapa.bloco_largura and Ch.rect.right < 1216 + Mapa.bloco_largura and Ch.rect.top > - Mapa.bloco_altura and Ch.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_Ch.draw(screen)

    # Baú
    for i in range(len(Mapa.Baus)):
        Bau.rect = Mapa.Baus[i]
        if Bau.rect.left > -Mapa.bloco_largura and Bau.rect.right < 1216 + Mapa.bloco_largura and Bau.rect.top > - Mapa.bloco_altura and Bau.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_Bau.draw(screen)

    # Coração
    for i in range(len(Mapa.coracao)):
        Co.rect = Mapa.coracao[i]
        if Co.rect.left > -Mapa.bloco_largura and Co.rect.right < 1216 + Mapa.bloco_largura and Co.rect.top > - Mapa.bloco_altura and Co.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_Co.draw(screen)

    # Porta
    for i in range(len(Mapa.Portas)):
        Por.rect = Mapa.Portas[i]
        if Por.rect.left > -Mapa.bloco_largura and Por.rect.right < 1216 + Mapa.bloco_largura and Por.rect.top > - Mapa.bloco_altura and Por.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_Por.draw(screen)

    # Espinho
    for i in range(len(Mapa.Espinhos)):
        Es.rect = Mapa.Espinhos[i]
        if Mapa.Espinhos_estado[i] == "ativo":
            Es.image = spikes_Ativo.subsurface((0, 0), (64, 64))
        elif Mapa.Espinhos_estado[i] == "desativado":
            Es.image = spikes_Desativado.subsurface((64, 0), (64, 64))
        Es.image = pygame.transform.scale(Es.image, (Mapa.bloco_largura, Mapa.bloco_altura))
        if Es.rect.left > -Mapa.bloco_largura and Es.rect.right < 1216 + Mapa.bloco_largura and Es.rect.top > - Mapa.bloco_altura and Es.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_Es.draw(screen)

    # Fim
    for i in range(len(Mapa.Fim)):
        Fim.rect = Mapa.Fim[i]
        if Fim.rect.left > -Mapa.bloco_largura and Fim.rect.right < 1216 + Mapa.bloco_largura and Fim.rect.top > - Mapa.bloco_altura and Fim.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_Fim.draw(screen)

    # Inimigo Vertical
    for i in range(len(Mapa.InimigosV)):
        IV.rect = Mapa.InimigosV[i]
        # Abelha
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = Abelha_Baixo.subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IV.image = Abelha_Cima.subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
        '''# Aranha
        elif Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoV[i] > 0:
                IV.image = Aranha_Baixo.subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IV.image = Aranha_Cima.subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))'''
        IV.image = pygame.transform.scale(IV.image, (Mapa.bloco_largura, Mapa.bloco_altura))
        if IV.rect.left > -Mapa.bloco_largura and IV.rect.right < 1216 + Mapa.bloco_largura and IV.rect.top > - Mapa.bloco_altura and IV.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_IV.draw(screen)

    # Inimigo Horizontal
    for i in range(len(Mapa.InimigosH)):
        IH.rect = Mapa.InimigosH[i]
        # Abelha
        if Telas.fase[0] == -4:
            if Mapa.Inimigos_direcaoH[i] > 0:
                IH.image = Abelha_Direita.subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
            else:
                IH.image = Abelha_Esquerda.subsurface((sprites_ativos["Abelha"] * 64, 0), (64, 64))
        '''
        # Aranha
        elif Telas.fase[0] == -?:
            if Mapa.Inimigos_direcaoH[i] > 0:
                IH.image = Aranha_Direita.subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))
            else:
                IH.image = Aranha_Esquerda.subsurface((sprites_ativos["Aranha"] * 64, 0), (64, 64))'''
        IH.image = pygame.transform.scale(IH.image, (Mapa.bloco_largura, Mapa.bloco_altura))
        if IH.rect.left > -Mapa.bloco_largura and IH.rect.right < 1216 + Mapa.bloco_largura and IH.rect.top > - Mapa.bloco_altura and IH.rect.bottom < 704 + Mapa.bloco_altura:
            Grupo_sprites_IH.draw(screen)

