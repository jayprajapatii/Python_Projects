import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Load images
bg = pygame.image.load("flappy_bird/img/background.jpg")
ground_img = pygame.image.load("flappy_bird/img/ground.jpg")
pipe_img = pygame.image.load("flappy_bird/img/pipe.jpg")

bird_frames = [
    pygame.image.load("flappy_bird/img/Bird.jpg"),
    pygame.image.load("flappy_bird/img/Bird.jpg"),
    pygame.image.load("flappy_bird/img/Bird.jpg")
]

# Load sounds
flap_sound = pygame.mixer.Sound("flappy_bird/audio/flap.mp3")
hit_sound = pygame.mixer.Sound("flappy_bird/audio/hit.mp3")
point_sound = pygame.mixer.Sound("flappy_bird/audio/point.mp3")

# Bird
bird_index = 0
bird_x = 100
bird_y = 350
bird_velocity = 0
gravity = 0.5
jump = -8

# Ground
ground_x = 0

# Pipes
pipe_gap = 250
pipe_speed = 4
pipes = []

score = 0
game_over = False

# High Score
try:
    with open("highscore.txt","r") as f:
        highscore = int(f.read())
except:
    highscore = 0


def create_pipe():
    height = random.randint(200, 350)
    return {"x": WIDTH, "height": height}


def move_pipes():
    global score

    for pipe in pipes:
        pipe["x"] -= pipe_speed

    if pipes and pipes[0]["x"] < -80:
        pipes.pop(0)
        score += 1
        point_sound.play()

    if len(pipes) < 2:
        pipes.append(create_pipe())


def draw_pipes():
    for pipe in pipes:
        top = pygame.transform.flip(pipe_img, False, True)
        screen.blit(top, (pipe["x"], pipe["height"] - pipe_img.get_height()))
        screen.blit(pipe_img, (pipe["x"], pipe["height"] + pipe_gap))


def check_collision():
    global game_over

    if bird_y > HEIGHT - 100 or bird_y < 0:
        hit_sound.play()
        game_over = True

    for pipe in pipes:
        if bird_x + 30 > pipe["x"] and bird_x < pipe["x"] + 80:
            if bird_y < pipe["height"] or bird_y > pipe["height"] + pipe_gap:
                hit_sound.play()
                game_over = True


def reset_game():
    global bird_y, bird_velocity, pipes, score, game_over

    bird_y = 350
    bird_velocity = 0
    pipes = [create_pipe()]
    score = 0
    game_over = False


reset_game()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                if game_over:

                    if score > highscore:
                        with open("highscore.txt","w") as f:
                            f.write(str(score))

                    reset_game()

                else:
                    bird_velocity = jump
                    flap_sound.play()

    if not game_over:

        bird_velocity += gravity
        bird_y += bird_velocity

        move_pipes()
        check_collision()

    # Background
    screen.blit(bg,(0,0))

    # Bird animation
    bird_index += 0.2
    if bird_index >= len(bird_frames):
        bird_index = 0

    bird = bird_frames[int(bird_index)]
    screen.blit(bird,(bird_x,int(bird_y)))

    # Pipes
    draw_pipes()

    # Moving ground
    ground_x -= 2
    if ground_x <= -WIDTH:
        ground_x = 0

    screen.blit(ground_img,(ground_x,HEIGHT-100))
    screen.blit(ground_img,(ground_x+WIDTH,HEIGHT-100))

    # Score
    score_text = font.render("Score: "+str(score),True,(255,255,255))
    screen.blit(score_text,(10,10))

    high_text = font.render("High: "+str(highscore),True,(255,255,255))
    screen.blit(high_text,(350,10))

    if game_over:
        over = font.render("GAME OVER - SPACE",True,(255,0,0))
        screen.blit(over,(120,350))

    pygame.display.update()
    clock.tick(60)