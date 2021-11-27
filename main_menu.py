import pygame, sys, constantes
from pygame.locals import *
from spritesheet import SpriteSheet, Origin


fpsClock = pygame.time.Clock()


pygame.init()
pygame.display.set_caption('Resgate do coração')
screen = pygame.display.set_mode(constantes.Tela, 0, 32)

font = pygame.font.SysFont('Arial', 25, True, False)



fundo = pygame.image.load("fundo.png").convert()
musica = pygame.mixer.Sound("PassandoAPagina.wav")

def escrever_texto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)




def main_menu():
    while True:

        screen.fill(constantes.Preto)
        escrever_texto('Menu Principal', font, constantes.Branco, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                cutscene1()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        escrever_texto('Botão 1', font, constantes.Branco, screen, 50, 100)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        escrever_texto('Botão 2', font, constantes.Branco, screen, 50, 200)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        fpsClock.tick(60)


def game():
    running = True
    while running:

        screen.fill(constantes.Preto)

        escrever_texto('Jogo Resgate do Coração', font, constantes.Branco, screen, 20, 20)



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        fpsClock.tick(60)


def options():

    running = True

    while running:
        screen.fill(constantes.Preto)

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)



        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        escrever_texto('Efeitos', font, constantes.Branco, screen, 50, 100)
        escrever_texto('Musica', font, constantes.Branco, screen, 50, 200)


        escrever_texto('Opções', font, constantes.Branco, screen, 20, 20)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        fpsClock.tick(60)

def cutscene1():
    running = True
    cutscene = SpriteSheet('C:/Users/Jonas Felipe/Desktop/UFPB/Introdução a programação/resgatedocoracao/primeira_cutscene/imagem 2.png', 7, 1)
    FrameAtualcutscene = 0

    plaquinhas = SpriteSheet("plaquinha.png", 7, 1)


    while running:
        if FrameAtualcutscene > 5:
            running = False


        screen.fill(constantes.Preto)
        cutscene.blit(screen, FrameAtualcutscene, (64*2, 64), Origin.TopLeft)
        plaquinhas.blit(screen, FrameAtualcutscene,(64*5, 64*7), Origin.TopLeft)
        escrever_texto('Pressione "Espaço" para continuar...', font, constantes.Branco, screen, 750, 670)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    FrameAtualcutscene += 1
                    musica.play()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        fpsClock.tick(60)

main_menu()