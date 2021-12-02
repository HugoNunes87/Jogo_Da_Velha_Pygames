import pygame
import sys

pygame.init()

#Tela
tamanho = comprimento, altura = 600, 600
janela = pygame.display.set_mode(tamanho)

#imagens
xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola2.png")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola,(100,100))

# Cores De Fundo 
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
ciano = 27, 242, 213
rosa = 203, 7, 118
roxo = 158, 151, 255



cores = [preto, branco, vermelho, verde, azul, ciano, rosa, roxo]

vencedorUM = ""
vez = 'X'
rodada = 0

jogo = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'], ]

# quadrantes
quadrante_linha = [50 , 250, 450]
quadrante_coluna = [50, 250, 450]

#Preenche a janela (0.Preto - 1.branco - 2.vermelho - 3.verde - 4.azul - 5.ciano - 6.rosa - 7.roxo)
janela.fill(cores[5]) 

#Desenha o jogo da velha
def desenha_quadro():
    pygame.draw.line(janela, preto, (200,0),(200,600),10)
    pygame.draw.line(janela, preto, (400,0),(400,600),10)
    pygame.draw.line(janela, preto, (0,200),(600,200),10)
    pygame.draw.line(janela, preto, (0,400),(600,400),10)


# Inserir imagem X ou O
def faz_jogada_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    
    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'O'
        return True
    else:
        print('Essa Posição ja esta ocupada!!!!')
        return False


def faz_jogada_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)

    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'X'
        return True

    else:
        print('Essa Posição já esta ocupada!!!!')
        return False
    
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

def ganhou1():
    vencedor = ''
    
    # Verifica Linhas
    if (jogo[0][0]== "X") and (jogo[0][1]== "X") and (jogo[0][2]== "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, preto,(0,100), [600,100], 10)
        vencedor = 'X'
    if (jogo[1][0] == "X") and (jogo[1][1]== "X") and (jogo[1][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, preto, (0, 300), (600, 300), 5)
        vencedor = 'X'
    if (jogo[2][0] == "X") and (jogo[2][1] == "X") and(jogo[2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        
        pygame.draw.line(janela, preto, (0, 500), (600, 500), 5)
        vencedor = 'X'

    # Verifica Coluna   
    if (jogo[0][0] == "X") and (jogo[1][0] == "X") and(jogo[2][0] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, preto, (100, 0), (100, 600), 5) 
        vencedor = 'X'
    if (jogo[0][1] == "X") and (jogo[1][1] == "X") and(jogo[2][1] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, preto, (300, 0), (300, 600), 5)
        vencedor = 'X'
    if (jogo[0][2] == "X") and (jogo[1][2] == "X") and(jogo[2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, preto, (500, 0), (500, 600), 5)
        vencedor = 'X'

    # Verifica Diagonal
    if (jogo[0][0] == "X") and (jogo[1][1] == "X") and (jogo[2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, preto, (0, 0), (600, 600), 5)
        vencedor = 'X'
    if (jogo[0][2] == "X") and (jogo[1][1] == "X") and (jogo[2][0] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, preto, (0, 600), (600, 0), 5)
        vencedor = 'X'    
    return vencedor

def ganhou2():
    vencedor = ''
    if (jogo[0][0]== "O") and (jogo[0][1]== "O") and (jogo[0][2]== "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto,(0,100), [600,100], 10)
        vencedor = 'O'
    if (jogo[1][0] == "O") and (jogo[1][1]== "O") and (jogo[1][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto, (0, 300), (600, 300), 5)
        vencedor = 'O'
    if (jogo[2][0] == "O") and (jogo[2][1] == "O") and(jogo[2][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto, (0, 500), (600, 500), 5)
        vencedor = 'O'

    # Verifica Coluna   
    if (jogo[0][0] == "O") and (jogo[1][0] == "O") and(jogo[2][0] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto, (100, 0), (100, 600), 5) 
        vencedor = 'O'
    if (jogo[0][1] == "O") and (jogo[1][1] == "O") and(jogo[2][1] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto, (300, 0), (300, 600), 5)
        vencedor = 'O'
    if (jogo[0][2] == "O") and (jogo[1][2] == "O") and(jogo[2][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto, (500, 0), (500, 600), 5)
        vencedor = 'O'

    # Verifica Diagonal
    if (jogo[0][0] == "O") and (jogo[1][1] == "O") and (jogo[2][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto, (0, 0), (600, 600), 5)
        vencedor = 'O'
    if (jogo[0][2] == "O") and (jogo[1][1] == "O") and (jogo[2][0] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, preto, (0, 600), (600, 0), 5)
        vencedor = 'O'    
    return vencedor

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
while True:
    desenha_quadro()   
    #Verifica eventos na janela do jogo
    for event in pygame.event.get():
        # fechar a janela e o jogo é encerrado
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
                            
            if (vez=='X'):
                print("Vez de X")
                fez_jogada = faz_jogada_xis(click_pos)
                vencedorUM = ganhou1()
                if (fez_jogada == True):
                        vez='O'
                        rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'X'
                                        
            elif (vez=='O'):
                print("Vez de O")
                fez_jogada = faz_jogada_bola(click_pos)
                vencedorUM = ganhou2()
                if (fez_jogada == True):
                    vez = 'X'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'O'
                        
    pygame.display.flip() #Atualiza a janela

    if (rodada>=9) or (vencedorUM !=''):
        print ('Jogo Finalizado!')
        print(jogo)
        break

    

