import pygame  # importando a bib pygame

pygame.init() # inicianlizando a bib pygame
largura, altura = 800,600  # definindo a largura e altura da tela 
tela = pygame.display.set_mode((largura, altura)) # criando a tela 
clock = pygame.time.Clock() # crindo relogio

x = 50
y = 50 # posição inicial da ping-pong
velocidade_x = 150 # velocidade da ping-pong eixo horizontal
velocidade_y = 300 # velocidade da ping-pong eixo vertical 
largura_ret, altura_ret = 50, 50 # largura e altura do retangulo (PIXELS )

rodando = True # variavel para controlar o loop principal 
while rodando: # loop principal
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

     #  taxa de atualiza 
    x += velocidade_x
    y += velocidade_y 

    # Invertendo a direção se ela atingir as bordas
    if x + largura_ret > largura or x < 0:
        velocidade_x *= -1 
    if y + altura_ret > altura or y < 0:
        velocidade_y *= -1

    tela.fill((0,191,255)) # verde claro em RGB  a tela 
    pygame.draw.rect(tela, (106,90,205), (x,y, largura_ret, altura_ret))
    pygame.display.update() # atualiza tela
    clock.tick(60)  # limita a  taxa de atualização para 60 FPS

pygame.quit() # encerra o pygame