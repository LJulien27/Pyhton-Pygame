import pygame, sys, random, secrets

pygame.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("Times new roman", int(WIDTH/20))
pygame.display.set_caption("Pong")

FPS = 60
player = pygame.Rect(WIDTH-90,HEIGHT/2-50,10,100)
opponent = pygame.Rect(90,HEIGHT/2-50,10,100)
ball = pygame.Rect(WIDTH/2-10,HEIGHT/2-20,20,20)
x_speed = 3
y_speed = 3
player_score, opponent_score = 0, 0


def draw_window():
    WIN.fill((255,255,255))
    
    pygame.draw.rect(WIN, "black", player)
    pygame.draw.rect(WIN, "black", opponent)
    pygame.draw.circle(WIN, "black", ball.center, 10)
    player_score_text = FONT.render(str(player_score), True, "black")
    opponent_score_text = FONT.render(str(opponent_score), True, "black")

    WIN.blit(player_score_text,(WIDTH/2+50, 50))
    WIN.blit(opponent_score_text,(WIDTH/2-50, 50))

    pygame.display.update()

clock = pygame.time.Clock()
run = True
while run:
    keys_pressed = pygame.key.get_pressed()
        
    if keys_pressed[pygame.K_w]:
        player.top -= 10
            
    if keys_pressed[pygame.K_s]:
        player.top += 10
        
    if player.top > HEIGHT-100:
        player.top = HEIGHT-100
    if player.top < 0:
        player.top = 0

    if opponent.top > HEIGHT-100:
        opponent.top = HEIGHT-100
    if opponent.top < 0:
        opponent.top = 0
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if ball.y > HEIGHT-10:
        y_speed = -3
    if ball.y < 0:
        y_speed = 3
    if ball.x < 0:
        player_score += 1
        ball.center = (WIDTH/2-10, HEIGHT/2-10)
        x_speed, y_speed = secrets.choice([3,-3,4,-4,-5,5]), random.randrange(3,-3,-1)
    if ball.x > WIDTH-10:
        opponent_score += 1
        ball.center = (WIDTH/2-10, HEIGHT/2-10)
        x_speed, y_speed = secrets.choice([3,-3,4,-4,-5,5]), random.randrange(3,-3,-1)
    if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):
        x_speed = secrets.choice([-3,-4,-5])
        y_speed = random.randrange(3,-3,-1)
    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range(opponent.top-ball.width, opponent.bottom+ball.width):
        x_speed = secrets.choice([3,4,5])
        y_speed = random.randrange(3,-3,-1)
                
    ball.x += x_speed * 3
    ball.y += y_speed * 3

    if opponent.y+50 < ball.y:
        opponent.top += 5
    if opponent.y+50 > ball.y:
        opponent.top -= 5
        
    draw_window()
    clock.tick(FPS)

