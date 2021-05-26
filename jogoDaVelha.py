import pygame, sys

pygame.init()

#Consts para largura e altura da tela, e cor do fundo
WIDTH = 600
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)

#Gera a tela
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jogo da velha')
screen.fill(BLACK)

#Método para desenhar o board do game
def drawBoard():
    pygame.draw.line(screen, WHITE, (40,200),(560,200),15) #Primeira linha horizontal
    pygame.draw.line(screen, WHITE, (40,400),(560,400),15) #Primeira linha vertical
    pygame.draw.line(screen, WHITE, (200,40),(200,560),15) #Segunda linha horizontal
    pygame.draw.line(screen, WHITE, (400,40),(400,560),15) #Segunda linha vertical

drawBoard()





#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()

