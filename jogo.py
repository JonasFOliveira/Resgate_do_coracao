import pygame
from pygame.locals import *
from sys import exit
from spritesheet import SpriteSheet, Origin



# Inicialização do Pygame
pygame.init()

# Dimensões da tela
Altura = 704
Largura = 1216









# Configurções da tela
screen = pygame.display.set_mode((Largura, Altura))  # definição do tamanho da tela
pygame.display.set_caption("Resgate do Coração")  # Definição do nome na aba
fps = 60  # definindo taxa de atualização de quadros
fpsClock = pygame.time.Clock()  # chamada da função clock do pygame
screen.fill((0, 0, 0))  # definindo a tela com a cor preta (RGB = 0, 0, 0)
icone = pygame.image.load("icon.png") #carregando icone
pygame.display.set_icon(icone) #selecionando o icone na janela

# Carregamento do Gif como SpriteSheet
morcego_frente = SpriteSheet("morcego_frente_spritesheet.png", 5, 1)
qntFramesMorcego = morcego_frente.sprite_count() - 1
FrameAtualMorcegoFrente = 0

morcego_tras = SpriteSheet("morcego_tras_spritesheet.png", 5, 1)
qntFramesMorcego_tras = morcego_tras.sprite_count() -1
FrameAtualMorcegoTras = 0


branco_fundo = pygame.image.load('branco.png')

# carregamentos para a tela
imagem = pygame.image.load("teste.png").convert()  # Carregamento de imagem do pygame
screen.blit(imagem, (0, 0))  # Colocando a imagem como o fundo

#realizando movimentação
x = 0
y = 32
mudanca = 0

al_ret = 100
la_ret = 200













# Game Loop
jogo = True
while jogo:

    screen.blit(imagem, (0, 0))  # Colocando a imagem como o fundo
    for evento in pygame.event.get():

        if evento.type == QUIT:
            pygame.quit()
            exit()

    #movimentar o personagem (retangulo) com de forma constante
    if pygame.key.get_pressed()[K_a]:
        la_ret -= 5
    if pygame.key.get_pressed()[K_s]:
        al_ret += 5
    if pygame.key.get_pressed()[K_d]:
        la_ret += 5
    if pygame.key.get_pressed()[K_w]:
        al_ret -= 5
    pygame.draw.rect(screen, (255, 167, 25), (la_ret, al_ret, 40, 50))  # criando um retangulo

    # transformando as imagens em um Gif
    if FrameAtualMorcegoFrente >= qntFramesMorcego:
        FrameAtualMorcegoFrente = 0
    else:
        FrameAtualMorcegoFrente += .07

    # transformando as imagens em um Gif
    if FrameAtualMorcegoTras >= qntFramesMorcego_tras:
        FrameAtualMorcegoTras = 0
    else:
        FrameAtualMorcegoTras += .07



    if mudanca == 0:
        morcego_frente.blit(screen, int(FrameAtualMorcegoFrente), (255, y),Origin.Center)  # inserindo o gif de morcego na tela
        y += 1

    elif mudanca == 1: #se ocorrer a mudança, ou sjea, chegar no final, o morcego vai voltar de costas
        morcego_tras.blit(screen, int(FrameAtualMorcegoTras), (255, y),Origin.Center)  # inserindo o gif de morcego tras na tela
        y -= 1

    if y >= Altura-32:
        mudanca = 1
    elif y == 32:
        mudanca = 0











    # atualização da tela
    pygame.display.flip()
    fpsClock.tick(fps)


