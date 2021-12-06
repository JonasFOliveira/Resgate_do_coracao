import pygame
import Sons

# Variaveis
velocidade = 18
Vidas = []
coracao = []
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
TodasAsCoisas = [Paredes, Portas, Baus, Chaves, Espinhos, InimigosH, InimigosV, coracao, Fim]

def Monta_mapa(matriz):
    bloco_largura = 200
    bloco_altura = 200
    caixa = 90
    # Posição inicial
    inix = 0
    iniy = 0
    for Y in range(len(matriz)):
        for X in range(len(matriz[Y])):
            if matriz[Y][X] == 9:
                inix = X * bloco_largura - 593 + 50
                iniy = Y * bloco_altura -322 + 50

    # Constroi mapa
    for Y in range(len(matriz)):
        for X in range(len(matriz[Y])):
            if matriz[Y][X] == 1:
               Paredes.append(pygame.Rect(X * bloco_largura - inix, Y * bloco_altura - iniy, bloco_largura, bloco_altura))
            elif matriz[Y][X] == 2:
                Portas.append(pygame.Rect(X * bloco_largura - inix, Y * bloco_altura - iniy, bloco_largura, bloco_altura))
            elif matriz[Y][X] == 3:
                Baus.append(pygame.Rect(X * bloco_largura - inix + (200 - caixa)//2, Y * bloco_altura - iniy + (200 - caixa)//2, caixa, caixa))
                Chaves.append(pygame.Rect(X * bloco_largura - inix + 66, Y * bloco_altura - iniy + 87, 71, 26))
            elif matriz[Y][X] == 4:
                Espinhos.append(pygame.Rect(X * bloco_largura - inix, Y * bloco_altura - iniy, bloco_largura, bloco_altura))
                Espinhos_estado.append("ativo")
                Espinhos_tempo.append(0)
            elif matriz[Y][X] == 5:
                InimigosH.append(pygame.Rect(X * bloco_largura - inix, Y * bloco_altura - iniy, 133, bloco_altura))
                Inimigos_direcaoH.append(24)
            elif matriz[Y][X] == 6:
                InimigosV.append(pygame.Rect(X * bloco_largura - inix, Y * bloco_altura - iniy, bloco_largura, 133))
                Inimigos_direcaoV.append(24)
            elif matriz[Y][X] == 7:
                if len(Vidas) != 3:
                    coracao.append(pygame.Rect(X * bloco_largura - inix + 81, Y * bloco_altura - iniy + 80, 37, 40))
            elif matriz[Y][X] == 8:
                Fim.append(pygame.Rect(X * bloco_largura - inix, Y * bloco_altura - iniy, bloco_largura, bloco_altura))

# Move tudo do mapa e gerencia as colissões do mapa
def Move_mapa(RetDoJogador, V, som, direcao = "nada"):
    for i in range(len(TodasAsCoisas)):
        for tc in TodasAsCoisas[i]:
            if direcao == "direita":
                tc.left -= V
            elif direcao == "esquerda":
                tc.left += V
            elif direcao == "cima":
                tc.top += V
            elif direcao == "baixo":
                tc.top -= V
            if tc.colliderect(RetDoJogador):
                PortaChave(RetDoJogador, direcao, som, V)
                PegaChave(RetDoJogador, direcao, som, V)
                if tc not in Espinhos and tc not in InimigosH and tc not in InimigosV and tc not in coracao and tc not in Fim:
                    Para_mapa(V, direcao)

# Faz o mapa parar
def Para_mapa( v, direcao="nada"):
    for index in range(len(TodasAsCoisas)):
        for tudo in TodasAsCoisas[index]:
            if direcao == "direita":
                tudo.left += v
            elif direcao == "esquerda":
                tudo.left -= v
            elif direcao == "cima":
                tudo.top -= v
            elif direcao == "baixo":
                tudo.top += v

# Mecanica da Porta e da chave
def PortaChave(retjogador, direcao, s, v):
    for i in range(len(Portas)):
        if Portas[i].colliderect(retjogador) and len(Chave_pega) > 0:
            del Chave_pega[-1]
            if Portas[i] != Portas[-1]:
                del Portas[i]
                if s:
                    Sons.Destranca_porta.play()
                if direcao == "direita":
                    Portas[i].left -= v
                elif direcao == "esquerda":
                    Portas[i].left += v
                elif direcao == "cima":
                    Portas[i].top += v
                elif direcao == "baixo":
                    Portas[i].top -= v
            else:
                del Portas[i]
                if s:
                    Sons.Destranca_porta.play()
            break

# Pega chave
def PegaChave(retjogador, direcao, s, v):
    for i in range(len(Chaves)):
        if Chaves[i].colliderect(retjogador):
            Chave_pega.append("chave")
            if Chaves[i] != Chaves[-1]:
                del Chaves[i]
                if s:
                    Sons.Pega_chave.play()
                if direcao == "direita":
                    Chaves[i].left -= v
                elif direcao == "esquerda":
                    Chaves[i].left += v
                elif direcao == "cima":
                    Chaves[i].top += v
                elif direcao == "baixo":
                    Chaves[i].top -= v
            else:
                del Chaves[i]
                if s:
                    Sons.Pega_chave.play()
            break

# Baú
def Bau(retjogador, som):
    for i in range(len(Baus)):
        if retjogador.right > Baus[i].left - 20 and retjogador.left < Baus[i].right + 20 and retjogador.bottom > Baus[i].top - 20 and retjogador.top < Baus[i].bottom + 20 and pygame.key.get_pressed()[pygame.K_SPACE]:
            del Baus[i]
            if som:
                Sons.Abre_bau.play()
            break

# Vida
def Vida(retjogador, som):
    for i in range(len(coracao)):
        if coracao[i].colliderect(retjogador):
            Vidas.append("vida")
            del coracao[i]
            if som:
                Sons.Pega_vida.play()
            break

# Move o inimigo horizontal
def InimigoH(retjogador, map, som):
    for i in range(len(InimigosH)):
        InimigosH[i].left += Inimigos_direcaoH[i]
        for p in Paredes:
            if InimigosH[i].colliderect(p):
                InimigosH[i].left -= Inimigos_direcaoH[i]
                Inimigos_direcaoH[i] = -Inimigos_direcaoH[i]
        if InimigosH[i].colliderect(retjogador):
            Deletar_mapa()
            if som:
                Sons.Dano.play()
            del Vidas[-1]
            Monta_mapa(map)

# Move o inimigo vertical
def InimigoV(retjogador, map, som):
    for i in range(len(InimigosV)):
        InimigosV[i].top += Inimigos_direcaoV[i]
        for p in Paredes:
            if InimigosV[i].colliderect(p):
                InimigosV[i].top -= Inimigos_direcaoV[i]
                Inimigos_direcaoV[i] = -Inimigos_direcaoV[i]
        if InimigosV[i].colliderect(retjogador):
            Deletar_mapa()
            if som:
                Sons.Dano.play()
            del Vidas[-1]
            Monta_mapa(map)

# Espinhos
def Espinho(retjogador, map, som):
    for i in range(len(Espinhos)):
        if Espinhos_estado[i] == "ativo":
            Espinhos_tempo[i] += 1
            if Espinhos_tempo[i] >= 30:
                Espinhos_estado[i] = "desativado"
                Espinhos_tempo[i] = 0
        if Espinhos_estado[i] == "desativado":
            Espinhos_tempo[i] += 1
            if Espinhos_tempo[i] >= 35:
                Espinhos_estado[i] = "ativo"
                Espinhos_tempo[i] = 0
        if Espinhos[i].colliderect(retjogador):
            if Espinhos_estado[i] == "ativo":
                Deletar_mapa()
                if som:
                    Sons.Dano.play()
                del Vidas[-1]
                Monta_mapa(map)

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
    del coracao[:]
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
    for c in coracao:
        pygame.draw.rect(screen, (155, 0, 0), c)
    for i in range(len(Espinhos)):
        if Espinhos_estado[i] == "ativo":
            pygame.draw.rect(screen, (255, 0, 0), Espinhos[i])
        elif Espinhos_estado[i] == "desativado":
            pygame.draw.rect(screen, (0, 255, 0), Espinhos[i])
    for f in Fim:
        pygame.draw.rect(screen, (0, 0, 0), f)