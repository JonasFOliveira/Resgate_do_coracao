import pygame
from Mapa_matriz import Matriz_mapa

# Variaveis
bloco_largura = 60
bloco_altura = 60
velocidade = 1
Paredes = []
TodasAsCoisas = [Paredes]

# Constroi mapa
for Y in range(len(Matriz_mapa)):
    for X in range(len(Matriz_mapa[Y])):
        if Matriz_mapa[Y][X] == 1:
           Paredes.append(pygame.Rect(X * bloco_largura, Y * bloco_altura, bloco_largura, bloco_altura))

# Move tudo do mapa
def Move_mapa(RetDoJogador, direcao = "nada"):
    for i in range(len(TodasAsCoisas)):
        for tc in TodasAsCoisas[i]:
            if direcao == "direita":
                tc.left -= velocidade
            elif direcao == "esquerda":
                tc.left += velocidade
            elif direcao == "cima":
                tc.top += velocidade
            elif direcao == "baixo":
                tc.top -= velocidade
            if tc.colliderect(RetDoJogador):
                for index in range(len(TodasAsCoisas)):
                    for tudo in TodasAsCoisas[index]:
                        if direcao == "direita":
                            tudo.left += velocidade
                        elif direcao == "esquerda":
                            tudo.left -= velocidade
                        elif direcao == "cima":
                            tudo.top -= velocidade
                        elif direcao == "baixo":
                            tudo.top += velocidade
# Desenha tudo do mapa
def Desenha_coisas(screen):
    for p in Paredes:
        pygame.draw.rect(screen, (105, 33, 133), p)