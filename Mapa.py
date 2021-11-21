import pygame
from Mapa_matriz import Matriz_mapa

# Variaveis
bloco_largura = 60
bloco_altura = 60
velocidade = 6
Chave_pega = ["chave", "chave", "chave"]
Paredes = []
Portas = []
Chaves = []
TodasAsCoisas = [Paredes, Portas, Chaves]

# Constroi mapa
for Y in range(len(Matriz_mapa)):
    for X in range(len(Matriz_mapa[Y])):
        if Matriz_mapa[Y][X] == 1:
           Paredes.append(pygame.Rect(X * bloco_largura, Y * bloco_altura, bloco_largura, bloco_altura))
        elif Matriz_mapa[Y][X] == 2:
            Portas.append(pygame.Rect(X * bloco_largura, Y * bloco_altura, bloco_largura, bloco_altura))
        elif Matriz_mapa[Y][X] == 3:
            Chaves.append(pygame.Rect((X * bloco_largura) + 10, (Y * bloco_altura + 10), 40, 20))

# Move tudo do mapa e gerencia as colissões do mapa
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
                PortaChave(RetDoJogador, direcao)
                PegaChave(RetDoJogador, direcao)
                Para_mapa(direcao)

# Faz o mapa parar
def Para_mapa(direcao="nada"):
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

# Mecanica da Porta e da chave
def PortaChave(retjogador, direcao):
    for i in range(len(Portas)):
        if Portas[i].colliderect(retjogador) and len(Chave_pega) > 0:
            del Chave_pega[-1]
            if Portas[i] != Portas[-1]:
                del Portas[i]
                if direcao == "direita":
                    Portas[i].left -= velocidade
                elif direcao == "esquerda":
                    Portas[i].left += velocidade
                elif direcao == "cima":
                    Portas[i].top += velocidade
                elif direcao == "baixo":
                    Portas[i].top -= velocidade
            else:
                del Portas[i]
            break

# Pega chave
def PegaChave(retjogador, direcao):
    for i in range(len(Chaves)):
        if Chaves[i].colliderect(retjogador):
            Chave_pega.append("chave")
            if Chaves[i] != Chaves[-1]:
                del Chaves[i]
                if direcao == "direita":
                    Chaves[i].left -= velocidade
                elif direcao == "esquerda":
                    Chaves[i].left += velocidade
                elif direcao == "cima":
                    Chaves[i].top += velocidade
                elif direcao == "baixo":
                    Chaves[i].top -= velocidade
            else:
                del Chaves[i]
            break


# Desenha tudo do mapa
def Desenha_coisas(screen):
    for p in Paredes:
        pygame.draw.rect(screen, (105, 33, 133), p)
    for por in Portas:
        pygame.draw.rect(screen, (50, 50, 50), por)
    for ch in Chaves:
        pygame.draw.rect(screen, (255, 255, 0), ch)