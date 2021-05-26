import pygame, sys
import numpy as np

pygame.init()

#Consts para largura e altura da tela, e cor do fundo
WIDTH = 650
T_WIDTH = WIDTH/3
HEIGHT = 650
T_HEIGHT = HEIGHT/3
CROSS_SPACE = 55

BLACK = (0,0,0)
WHITE = (255,255,255)

#Gera a tela
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jogo da velha')
screen.fill(BLACK)

#Método para desenhar o board do game
def drawBoard():
    pygame.draw.line(screen, WHITE, (25,225),(625,225),15) #Primeira linha horizontal
    pygame.draw.line(screen, WHITE, (25,425),(625,425),15) #Primeira linha vertical
    pygame.draw.line(screen, WHITE, (225,25),(225,625),15) #Segunda linha horizontal
    pygame.draw.line(screen, WHITE, (425,25),(425,625),15) #Segunda linha vertical

drawBoard()

#Método para desenhar as figuras (Circulo e X)
def drawFigs():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 2:
                pygame.draw.circle(screen,WHITE,(int(col*(WIDTH/3) + (HEIGHT/6)), int(row*(WIDTH/3) + (HEIGHT/6))), 60, 15)
            elif board[row][col] == 1:
                pygame.draw.line(screen,WHITE,(col*T_WIDTH + CROSS_SPACE,row*T_HEIGHT + T_HEIGHT - CROSS_SPACE),(col*T_WIDTH + T_WIDTH - CROSS_SPACE,row*T_HEIGHT + CROSS_SPACE), 25)
                pygame.draw.line(screen,WHITE,(col*T_WIDTH + CROSS_SPACE,row*T_HEIGHT + CROSS_SPACE),(col*T_WIDTH + T_WIDTH - CROSS_SPACE,row*T_HEIGHT + T_HEIGHT - CROSS_SPACE), 25)


#Método para verificar se um player ganhou (Checa todas as possibilidades)
def win(player):
    #Qualquer vitoria horizontal
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        else:
            return False

    #Qualquer vitoria vertical
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
        else:
            return False
    
    #Checa vitoria nas diagonais
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
   
    
    return False #So ira retornar false se nao houver nenhum caso de vitoria

#Criando uma matriz de zeros para representar o board vazio
board = np.zeros((3,3))
print(board)

#Métodos que checa se o espaço desejado está vazio
def check_empty_space(row, col):
    if board[row][col] == 0:
        return True
    else: 
        return False

#Método para verificar se o board está cheio ou não
def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
            else:
                return True


#Método que preenche o espaco se este estiver vazio
def mark_empty_space(row,col,player):
    if check_empty_space(row, col):
        board[row][col] = player
    else:
        return False

player = 1 




#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 225)
            clicked_col = int(mouseX // 225)

            if check_empty_space(clicked_row, clicked_col):
                if player == 1:
                    mark_empty_space(clicked_row,clicked_col,player)
                    player = 2
                elif player == 2: 
                    mark_empty_space(clicked_row,clicked_col,player)
                    player = 1
                
                
                drawFigs()

                if win(player):
                    print("ganhou")
                else:
                    print("nada")

                print(board)   


    pygame.display.update()

