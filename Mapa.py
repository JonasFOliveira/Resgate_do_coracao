import pygame
from Mapa_matriz import Matriz_mapa

# Variaveis
bloco_largura = 64
bloco_altura = 64
velocidade = 6
VelocidadeInimigo = 5
Vidas = []
Chave_pega = []
Paredes = []
Portas = []
Baus = []
Chaves = []
Espinhos = []
Espinhos_estado = []
Espinhos_tempo = []
InimigosH = []
Inimigos_direcaoH = []
InimigosV = []
Inimigos_direcaoV = []
Fim = []
TodasAsCoisas = [Paredes, Portas, Baus, Chaves, Espinhos, InimigosH, InimigosV, Fim]

def Monta_mapa():
    # Posição inicial
    inix = 0
    iniy = 0
    for Y in range(len(Matriz_mapa)):
        for X in range(len(Matriz_mapa[Y])):
            if Matriz_mapa[Y][X] == 9:
                inix = X * bloco_largura - 593
                iniy = Y * bloco_altura -322

    # Constroi mapa
    for Y in range(len(Matriz_mapa)):
        for X in range(len(Matriz_mapa[Y])):
            if Matriz_mapa[Y][X] == 1:
               Paredes.append(pygame.Rect(X * bloco_largura -inix, Y * bloco_altura -iniy, bloco_largura, bloco_altura))
            elif Matriz_mapa[Y][X] == 2:
                Portas.append(pygame.Rect(X * bloco_largura -inix, Y * bloco_altura -iniy, bloco_largura, bloco_altura))
            elif Matriz_mapa[Y][X] == 3:
                Baus.append(pygame.Rect(X * bloco_largura -inix, Y * bloco_altura -iniy, bloco_largura, bloco_altura))
                Chaves.append(pygame.Rect(X * bloco_largura -inix + 10, Y * bloco_altura -iniy + 20, 40, 20))
            elif Matriz_mapa[Y][X] == 4:
                Espinhos.append(pygame.Rect(X * bloco_largura -inix, Y * bloco_altura -iniy, bloco_largura, bloco_altura))
                Espinhos_estado.append("ativo")
                Espinhos_tempo.append(0)
            elif Matriz_mapa[Y][X] == 5:
                InimigosH.append(pygame.Rect(X * bloco_largura - inix, Y * bloco_altura - iniy, bloco_largura, bloco_altura))
                Inimigos_direcaoH.append(VelocidadeInimigo)
            elif Matriz_mapa[Y][X] == 6:
                InimigosV.append(pygame.Rect(X * bloco_largura -inix, Y * bloco_altura -iniy, bloco_largura, bloco_altura))
                Inimigos_direcaoV.append(VelocidadeInimigo)
            elif Matriz_mapa[Y][X] == 8:
                Fim.append(pygame.Rect(X * bloco_largura -inix, Y * bloco_altura -iniy, bloco_largura, bloco_altura))


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
                if tc not in Espinhos and tc not in InimigosH and tc not in InimigosV and tc not in Fim:
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

# Baú
def Bau(retjogador):
    for i in range(len(Baus)):
        if retjogador.right > Baus[i].left - 20 and retjogador.left < Baus[i].right + 20 and retjogador.bottom > Baus[i].top - 20 and retjogador.top < Baus[i].bottom + 20 and pygame.key.get_pressed()[pygame.K_SPACE]:
            del Baus[i]
            break

# Move o inimigo horizontal
def InimigoH(retjogador):
    for i in range(len(InimigosH)):
        InimigosH[i].left += Inimigos_direcaoH[i]
        for p in Paredes:
            if InimigosH[i].colliderect(p):
                InimigosH[i].left -= Inimigos_direcaoH[i]
                Inimigos_direcaoH[i] = -Inimigos_direcaoH[i]
        if InimigosH[i].colliderect(retjogador):
            Deletar_mapa()
            Monta_mapa()
            del Vidas[-1]

# Move o inimigo vertical
def InimigoV(retjogador):
    for i in range(len(InimigosV)):
        InimigosV[i].top += Inimigos_direcaoV[i]
        for p in Paredes:
            if InimigosV[i].colliderect(p):
                InimigosV[i].top -= Inimigos_direcaoV[i]
                Inimigos_direcaoV[i] = -Inimigos_direcaoV[i]
        if InimigosV[i].colliderect(retjogador):
            Deletar_mapa()
            Monta_mapa()
            del Vidas[-1]

# Espinhos
def Espinho(retjogador):
    for i in range(len(Espinhos)):
        if Espinhos_estado[i] == "ativo":
            Espinhos_tempo[i] += 1
            if Espinhos_tempo[i] >= 60:
                Espinhos_estado[i] = "desativado"
                Espinhos_tempo[i] = 0
        if Espinhos_estado[i] == "desativado":
            Espinhos_tempo[i] += 1
            if Espinhos_tempo[i] >= 120:
                Espinhos_estado[i] = "ativo"
                Espinhos_tempo[i] = 0
        if Espinhos[i].colliderect(retjogador):
            if Espinhos_estado[i] == "ativo":
                Deletar_mapa()
                Monta_mapa()
                del Vidas[-1]

# Deleta mapa
def Deletar_mapa():
    del Paredes[:]
    del Portas[:]
    del Baus[:]
    del Chaves[:]
    del Chave_pega[:]
    del Espinhos[:]
    del Espinhos_estado[:]
    del Espinhos_tempo[:]
    del InimigosH[:]
    del Inimigos_direcaoH[:]
    del InimigosV[:]
    del Inimigos_direcaoV[:]
    del Fim[:]

# Desenha tudo do mapa
def Desenha_coisas(screen):
    for p in Paredes:
        pygame.draw.rect(screen, (105, 33, 133), p)
    for por in Portas:
        pygame.draw.rect(screen, (50, 50, 50), por)
    for ch in Chaves:
        pygame.draw.rect(screen, (255, 255, 0), ch)
    for b in Baus:
        pygame.draw.rect(screen, (85, 25, 0), b)
    for inimh in InimigosH:
        pygame.draw.rect(screen, (255, 0, 0), inimh)
    for inimv in InimigosV:
        pygame.draw.rect(screen, (255, 0, 0), inimv)
    for i in range(len(Espinhos)):
        if Espinhos_estado[i] == "ativo":
            pygame.draw.rect(screen, (255, 0, 0), Espinhos[i])
        elif Espinhos_estado[i] == "desativado":
            pygame.draw.rect(screen, (0, 255, 0), Espinhos[i])
    for f in Fim:
        pygame.draw.rect(screen, (0, 0, 0), f)