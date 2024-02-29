instruction = print('PROJECT GAMEX', "a colaboation from VISHVVESH, SNEHIT , SAURABH AND DRUV ")
print('TYPE  THE CORESPONGING LETTERS FOR THE GAME TO BE PLAYED ')
print('enter v for SPACE INVADERS(vishvvesh)')
print('enter b for JUMPING STEVE ULTIMATE VERSION (sneith)')
print('enter c for PONG   (saurabh) ')
print('enter d for SNAKE (sneith)')
print('enter f SNAKE (druv)')

gv = input('enter a alpabet = ')

# vishvvesh's  space invader's game

while gv == 'v':
    gv = print('you are playing space invaders')

    import pygame
    import random
    import math
    from pygame import mixer

    # intializing

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load('background.png')
    mixer.music.load('Fun Time - AShamaluevMusic (2).wav')
    mixer.music.play(-1)
    pygame.display.set_caption("SPACE INVADERS")
    icon = pygame.image.load('rocket.py.png')
    pygame.display.set_icon(icon)

    playerimg = pygame.image.load('thor hammer 2.png')
    playerx = 370
    playery = 480
    playerx_change = 0

    enemyimg = []
    enemyx = []
    enemyy = []
    enemyx_change = []
    enemyy_change = []
    num_of_enemies = 6

    for i in range(num_of_enemies):
        enemyimg.append(pygame.image.load('iron man.png'))
        # enemyx = 370
        # enemyy = 50
        # enemyx_change = 0
        enemyx.append(random.randint(0, 800))
        enemyy.append(random.randint(50, 150))
        enemyx_change.append(4)
        enemyy_change.append(40)

    bulletimg = pygame.image.load('thunder.png')
    bulletx = 0
    bullety = 480
    bulletx_change = 0
    bullety_change = 10
    bullet_state = "ready"
    # score = 0
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textx = 10
    texty = 10


    def show_score(x, y):
        score = font.render("Score :" + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


    def player(x, y):
        screen.blit(playerimg, (x, y))


    def enemy(x, y, i):
        screen.blit(enemyimg[i], (x, y))


    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletimg, (x + 16, y + 10))


    def iscollition(enemyx, enemyy, bulletx, bullety):
        distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
        if distance < 27:
            return True
        else:
            return False


    running = True
    while running:

        screen.fill((204, 204, 255))
        screen.blit(background, (0, 0))
        # playerx += 0.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerx_change = -5
                if event.key == pygame.K_RIGHT:
                    playerx_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bullet_sound = mixer.Sound('scifi002.wav')
                        bullet_sound.play()

                        bulletx = playerx
                        fire_bullet(bulletx, bullety)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerx_change = 0

        playerx += playerx_change
        if playerx <= 0:
            playerx = 0
        elif playerx >= 736:
            playerx = 736

        for i in range(num_of_enemies):
            enemyx[i] += enemyx_change[i]
            if enemyx[i] <= 0:
                enemyx_change[i] = 4
                enemyy[i] += enemyy_change[i]
            elif enemyx[i] >= 736:
                enemyx_change[i] = -4
                enemyy[i] += enemyy_change[i]

            collition = iscollition(enemyx[i], enemyy[i], bulletx, bullety)
            if collition:
                explosion_sound = mixer.Sound('scifi011.wav')
                explosion_sound.play()
                bullety = 480
                bullet_state = "ready"
                score_value += 1
                # print(score)
                enemyx[i] = random.randint(0, 800)
                enemyy[i] = random.randint(50, 150)

            enemy(enemyx[i], enemyy[i], i)
        if bullety <= 0:
            bullety = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletx, bullety)
            bullety -= bullety_change
        # collition = iscollition(enemyx, enemyy, bulletx, bullety)
        # if collition:
        #    bullety = 480
        #    bullet_state = "ready"
        #    score += 1
        #    print(score)
        #    enemyx = random.randint(0, 735)
        #    enemyy = random.randint(50, 150)

        player(playerx, playery)
        show_score(textx, texty)
        pygame.display.update()

# snehit's game


if gv == 'b':
    gv = print('you are playing jumping steve the ultimate version')
    import pygame
    from pygame.locals import *

    # sounds
    from pygame import mixer

    pygame.init()
    mixer.music.load('bensound-beyondtheline . WAV.mp3')
    mixer.music.play(-1)

    # modules initialized
    pygame.init()
    # screen height and width
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption("JUMP DINO AND MARIO")
    # font
    font = pygame.font.Font('freesansbold.ttf', 20)
    # variables
    backx = 0
    backy = 0
    drax = 50
    dray = 275
    treex = 650
    treey = 282
    backvelo = 0
    walkpoint = 0
    gravity = 3
    game = False
    jump = False
    gameover = False
    score = 0
    # colours
    white = (255, 255, 255)
    black = (0, 0, 0)

    # images
    tree = pygame.image.load('brick1.png')
    tree = pygame.transform.scale(tree, (70, 50))
    tree1 = pygame.image.load('brick1.png')
    tree1 = pygame.transform.scale(tree1, (70, 50))
    tree2 = pygame.image.load('mario_grass.png')
    tree2 = pygame.transform.scale(tree2, (80, 55))
    tree3 = pygame.image.load('flower_PNG.png')
    tree3 = pygame.transform.scale(tree3, (70, 50))
    tree4 = pygame.image.load('flower_PNG.png')
    tree4 = pygame.transform.scale(tree4, (70, 50))
    tree5 = pygame.image.load('mario_cylinder.png')
    tree5 = pygame.transform.scale(tree5, (25, 80))
    tree6 = pygame.image.load('mario_grass.png')
    tree6 = pygame.transform.scale(tree6, (80, 55))
    tree7 = pygame.image.load('mario_grass.png')
    tree7 = pygame.transform.scale(tree7, (80, 55))
    tree8 = pygame.image.load('flower_PNG.png')
    tree8 = pygame.transform.scale(tree8, (70, 50))
    tree9 = pygame.image.load('flower_PNG.png')
    tree9 = pygame.transform.scale(tree9, (70, 50))
    tree10 = pygame.image.load('flower_PNG.png')
    tree10 = pygame.transform.scale(tree10, (70, 50))
    tree11 = pygame.image.load('mario_cylinder.png')
    tree11 = pygame.transform.scale(tree11, (250, 80))
    tree12 = pygame.image.load('mario_grass.png')
    tree12 = pygame.transform.scale(tree12, (80, 55))
    tree13 = pygame.image.load('mario_grass.png')
    tree13 = pygame.transform.scale(tree13, (80, 55))
    tree14 = pygame.image.load('mario_grass.png')
    tree14 = pygame.transform.scale(tree14, (80, 55))
    dragon = pygame.image.load('mariodra_PNG.png')
    dragon = pygame.transform.scale(dragon, (80, 50))

    background = pygame.image.load("background10.png")


    def gameloop():
        backx = 0
        backy = 0
        drax = 50
        dray = 275
        treex = 650
        treey = 282
        backvelo = 0
        walkpoint = 0
        gravity = 3
        game = False
        jump = False
        gameover = False
        score = 0


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if dray == 275:
                        jump = True
                        backvelo = 5
                        game = True
                if event.key == K_SPACE:
                    gameloop()
        if backx == -600:
            backx = 0
        if treex < -3400:
            treex = 900
        # jump
        if 276 > dray > 125:
            if jump == True:
                dray -= 6
        else:
            jump = False
        if dray < 275:
            if jump == False:
                dray += gravity
        # collission
        if treex < drax + 70 < treex + 70 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 90 < drax + 70 < treex + 160 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 400 < drax + 70 < treex + 470 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 800 < drax + 70 < treex + 870 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 910 < drax + 70 < treex + 980 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 1300 < drax + 70 < treex + 1370 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 1800 < drax + 70 < treex + 1870 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 1900 < drax + 70 < treex + 1970 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 2200 < drax + 70 < treex + 2270 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 2280 < drax + 70 < treex + 2350 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 2360 < drax + 70 < treex + 2430 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 2660 < drax + 70 < treex + 2730 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 3200 < drax + 70 < treex + 3270 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 3280 < drax + 70 < treex + 3350 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if treex + 3360 < drax + 70 < treex + 3430 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True
        if game == True:
            score += 1
        screen.fill(black)
        text = font.render("SCORE - " + str(score), True, white)
        text1 = font.render("GAME OVER PRESS Space To Continue", True, black)
        screen.blit(text1, [50, 250])
        backx -= backvelo
        treex -= backvelo
        screen.blit(background, [backx + 2900, backy])
        screen.blit(background, [backx, backy])
        screen.blit(text, [400, 150])
        if gameover == True:
            if walkpoint > 15:
                walkpoint = 0
        screen.blit(dragon, [drax, dray])
        screen.blit(tree, (treex, treey))
        screen.blit(tree1, [treex + 90, treey])
        screen.blit(tree2, [treex + 400, treey - 8])
        screen.blit(tree3, [treex + 800, treey - 4])
        screen.blit(tree4, [treex + 910, treey - 4])
        screen.blit(tree5, [treex + 1300, treey - 4])
        screen.blit(tree6, [treex + 1800, treey - 4])
        screen.blit(tree7, [treex + 1900, treey - 4])
        screen.blit(tree8, [treex + 2200, treey - 4])
        screen.blit(tree9, [treex + 2280, treey - 4])
        screen.blit(tree10, [treex + 2360, treey - 4])
        screen.blit(tree11, [treex + 2660, treey - 4])
        screen.blit(tree12, [treex + 3200, treey - 4])
        screen.blit(tree13, [treex + 3280, treey - 4])
        screen.blit(tree14, [treex + 3360, treey - 4])
        pygame.display.update()

        gameloop()



# saurab's game

if gv == 'c':
    # pong!
    import pygame
    from pygame import mixer

    pygame.init()
    mixer.music.load('Summer Trip - AShamaluevMusic.wav')
    mixer.music.play(-1)

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    # Coordinates p1, p2 and ball
    x1 = 490
    y1 = 250
    x2 = 0
    y2 = 250
    xb = 300
    yb = 300

    dbo = 'left'
    dbv = 'down'

    scorep1 = 0
    scorep2 = 0

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("My game" + "Score player 1: " + str(scorep1) + " - Score player 2: " + str(scorep2))

    pygame.init()


    def ball():
        "Draw the ball"
        global xb, yb
        pygame.draw.ellipse(screen, GREEN, (xb, yb, 10, 10))


    def sprite1(x, y):
        "Draw Player 1"
        pygame.draw.rect(screen, RED, (x, y, 10, 50))


    def sprite2(x, y):
        "Draw Player 2"
        pygame.draw.rect(screen, GREEN, (x, y, 10, 50))


    def move_ball(x, y):
        "The ball moves"
        global xb, yb, dbo, dbv
        if dbo == "left":
            xb -= 10
        if dbv == 'down':
            yb += 10
            if yb > 490:
                dbv = 'up'
        if dbv == 'up':
            yb -= 10
            if yb < 10:
                dbv = 'down'
        if dbo == "right":
            xb += 10


    def collision():
        global x1, y1  # the player 1 x and y (on the right)
        global x2, y2  # the player 2 x and y (on the left)
        global xb, yb  # the ball x and y
        global dbo
        global scorep1, scorep2
        if dbo == "left":
            if xb < 10:
                if yb >= y2 and yb < y2 + 50:
                    dbo = "right"
                else:
                    pygame.draw.ellipse(screen, BLACK, (xb, yb, 10, 10))
                    pygame.display.update()
                    xb, yb = 300, 300
                    scorep2 += 10
                    pygame.display.set_caption(
                        "My game" + "Score player 1: " + str(scorep1) + " - Score player 2: " + str(scorep2))
        else:
            if xb > 480:
                if yb >= y1 and yb < y1 + 50:
                    dbo = "left"
                else:
                    pygame.draw.ellipse(screen, BLACK, (xb, yb, 10, 10))
                    pygame.display.update()
                    xb, yb = 300, 300
                    scorep1 += 10
                    pygame.display.set_caption(
                        "My game" + "Score player 1: " + str(scorep1) + " - Score player 2: " + str(scorep2))


    def move1():
        global y2
        if y2 <= 450:
            if keys[pygame.K_z]:
                y2 += 20
        if y2 > 0:
            if keys[pygame.K_a]:
                y2 -= 20


    def move2():
        global y1
        if y1 <= 450:
            if keys[pygame.K_m]:
                y1 += 20
        if y1 > 0:
            if keys[pygame.K_k]:
                y1 -= 20


    loop = 1
    while loop:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
        move1()
        move2()
        move_ball(xb, yb)
        ball()
        sprite1(x1, y1)
        sprite2(x2, y2)
        collision()
        pygame.display.update()
        screen.fill((0, 0, 0))
        clock.tick(30)

    pygame.quit()

# druv's snake game

if gv == 'f':
    import pygame
    import sys
    from pygame.math import Vector2
    import random

    from pygame import mixer

    pygame.init()
    mixer.music.load('Simple Creatures - Drug.WAV.mp3')
    mixer.music.play(-1)


    class SNAKE():
        def __init__(self):
            self.body = [Vector2(11, 10), Vector2(12, 10), Vector2(13, 10)]
            self.direction = Vector2(0, 0)
            self.new_block = False

            self.head_up = pygame.image.load("graphics/head_up.png")
            self.head_down = pygame.image.load("graphics/head_down.png")
            self.head_left = pygame.image.load("graphics/head_left.png")
            self.head_right = pygame.image.load("graphics/head_right.png")

            self.tail_up = pygame.image.load("graphics/tail_up.png")
            self.tail_down = pygame.image.load("graphics/tail_down.png")
            self.tail_left = pygame.image.load("graphics/tail_left.png")
            self.tail_right = pygame.image.load("graphics/tail_right.png")

            self.body_horizontal = pygame.image.load("graphics/body_horizontal.png")
            self.body_vertical = pygame.image.load("graphics/body_vertical.png")

            self.body_topleft = pygame.image.load("graphics/body_topleft.png")
            self.body_topright = pygame.image.load("graphics/body_topright.png")
            self.body_bottomleft = pygame.image.load("graphics/body_bottomleft.png")
            self.body_bottomright = pygame.image.load("graphics/body_bottomright.png")
            self.crunch_sound = pygame.mixer.Sound("sound/crunch.wav")

        def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()

            for index, block in enumerate(self.body):
                x_position = (block.x * cell_size)
                y_position = (block.y * cell_size)
                block_rect = pygame.Rect(x_position, y_position, cell_size, cell_size)

                if index == 0:
                    screen.blit(self.head, block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail, block_rect)

                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.y == next_block.y:
                        screen.blit(self.body_horizontal, block_rect)
                    elif previous_block.x == next_block.x:
                        screen.blit(self.body_vertical, block_rect)
                    else:
                        if previous_block.y == -1 and next_block.x == -1 or previous_block.x == -1 and next_block.y == -1:
                            screen.blit(self.body_topleft, block_rect)
                        elif previous_block.y == -1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == -1:
                            screen.blit(self.body_topright, block_rect)
                        elif previous_block.y == 1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == 1:
                            screen.blit(self.body_bottomright, block_rect)
                        else:
                            screen.blit(self.body_bottomleft, block_rect)

        def update_head_graphics(self):
            head_relation = self.body[1] - self.body[0]

            if head_relation == Vector2(1, 0):
                self.head = self.head_left
            elif head_relation == Vector2(-1, 0):
                self.head = self.head_right
            elif head_relation == Vector2(0, 1):
                self.head = self.head_up
            elif head_relation == Vector2(0, -1):
                self.head = self.head_down

        def update_tail_graphics(self):
            tail_relation = self.body[- 2] - self.body[- 1]

            if tail_relation == Vector2(1, 0):
                self.tail = self.tail_left
            elif tail_relation == Vector2(-1, 0):
                self.tail = self.tail_right
            elif tail_relation == Vector2(0, 1):
                self.tail = self.tail_up
            elif tail_relation == Vector2(0, -1):
                self.tail = self.tail_down

        def move_snake(self):
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]

        def add_block(self):
            self.new_block = True

        def sound(self):
            self.crunch_sound.play()

        def reset_game(self):
            self.body = [Vector2(11, 10), Vector2(12, 10), Vector2(13, 10)]
            self.direction = Vector2(0, 0)


    class FRUIT:
        def __init__(self):
            self.randomize()

        def draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size,
                                     cell_size)
            screen.blit(apple, fruit_rect)
            # pygame.draw.ellipse(screen, "red", fruit_rect)

        def randomize(self):
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
            self.position = Vector2(self.x, self.y)


    class MAIN:
        def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

        def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()

        def check_collision(self):
            if self.fruit.position == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.position:
                    self.fruit.randomize()

        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number:
                self.game_over()

            if not 0 <= self.snake.body[0].y < cell_number:
                self.game_over()

            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()

        def game_over(self):
            self.snake.reset_game()

        def draw_grass(self):
            grass_color = (180, 240, 90)

            for rows in range(cell_number):
                if rows % 2 == 0:
                    for columns in range(cell_number):
                        if columns % 2 == 0:
                            grass_rectangle = pygame.Rect(columns * cell_size, rows * cell_size, cell_size, cell_size)
                            pygame.draw.rect(screen, grass_color, grass_rectangle)
                else:
                    for columns in range(cell_number):
                        if columns % 2 == 1:
                            grass_rectangle = pygame.Rect(columns * cell_size, rows * cell_size, cell_size, cell_size)
                            pygame.draw.rect(screen, grass_color, grass_rectangle)

        def draw_score(self):
            score_text = str((len(self.snake.body) - 3) * 10)
            score_surface = game_font.render(score_text, True, (50, 80, 20))
            score_x = int((cell_size * cell_number) - 60)
            score_y = int((cell_size * cell_number) - 60)
            score_rect = score_surface.get_rect(center=(score_x, score_y))
            apple_rect = apple.get_rect(center=(score_x - 25, score_y))
            bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 5,
                                  apple_rect.height)

            pygame.draw.rect(screen, (160, 200, 60), bg_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(apple, apple_rect)
            pygame.draw.rect(screen, (50, 80, 60), bg_rect, 2)


    pygame.init()
    cell_size = 30
    cell_number = 20
    framerate = 60
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    clock = pygame.time.Clock()
    apple = pygame.image.load("graphics/apple.png").convert_alpha()
    game_font = pygame.font.Font(None, 25)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 200)

    main_game = MAIN()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        screen.fill((175, 225, 100))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(framerate)


