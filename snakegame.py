#bibliotecas importadas
import pygame, random
from pygame.locals import *

#spaw aleatorio pelo mapa das maças

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

#colisao 

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
#moveset da cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

#principais variaveis

my_direction = LEFT #cobra sempre spawna para o oeste
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',18) #fonte
score = 0 
game_over = False

#looping do propio jogo
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    #colisao da cobra com ela mesma
        
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    if collision(snake[0],apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
    
    #colisáo com a borda do mapa
    
    if snake[0][0] == 600 or snake [0][1] == 600  or snake [0][0] < 0 or snake [0] [1] < 0:
        game_over = True 
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break  
    
    

    screen.fill((0,0,0))
    
    screen.blit(apple, apple_pos)
    
    
    for pos in snake:
        screen.blit(snake_skin,pos)
    for x in range(0,600,10):#desenhar as linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (x,0),(x, 600))
    for y in range(0,600,10):#desenhar as linhas horizontais 
        pygame.draw.line(screen,(40, 40, 40), (0,y), (600, y))    

    score_font = font.render('Score: %s' % (score), True , (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topright = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake: 
        screen.blit(snake_skin,pos)


    pygame.display.update()

#looping do game over
    
while True:
    game_over_font = pygame.font.Font('freesansbold.ttf',75)
    game_over_screen = game_over_font.render('Game Over', True, (255,255,255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
      for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               exit()
               