import pygame as pg
import random

white = (255, 255, 255)
black = (0, 0, 0)
red=(255,0,0)
src = "highest_score.txt"
width = 720
height = 480

pg.init()

dis = pg.display.set_mode((width, height))
pg.display.set_caption("Blob")
clock = pg.time.Clock()

def message(msg,color, x, y, s=50):
    mesg = pg.font.SysFont(None, s).render(msg, True, color)
    dis.blit(mesg, [x, y])

def game_loop():
    try:
        file_high = open(src, "r")
    except FileNotFoundError:
        file_not_found = open(src, 'x+')
        file_not_found.write("0")
        file_not_found.close()
        file_high = open(src, "r")
    highest_score = int(file_high.read())
    file_high.close()
    score = 0
    speed = 20
    game_close = False
    game_over = False
    snake = 20
    place_x = 355
    place_y = 235
    food_x = random.randrange(0, width-snake)
    food_y = random.randrange(60, height-snake)
    x_change = 0
    y_change = 0
    while game_over==False:
        if score>=highest_score:
            highest_score = score
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_DOWN:
                    x_change = 0
                    y_change = 10
                elif event.key==pg.K_UP:
                    x_change = 0
                    y_change = -10
                elif event.key==pg.K_LEFT:
                    x_change = -10
                    y_change = 0 
                elif event.key==pg.K_RIGHT:
                    x_change = 10
                    y_change = 0
        if place_x >= width or place_x < 0 or place_y >= height or place_y < 60:
            game_over = True
        place_x += x_change 
        place_y += y_change
        dis.fill(white)
        message("Your score : "+str(score)+"   Highest score : "+str(highest_score), black, 10, 10)
        pg.draw.rect(dis, black, [0, 60, 720, 1])
        pg.draw.rect(dis, red, [food_x, food_y, 10, 10])
        pg.draw.rect(dis, black, [place_x, place_y, snake, snake])
        pg.display.update()

        for i in list(range(place_x, place_x+20)):
            for  j in list(range(place_y, place_y+20)):
                if i in list(range(food_x, food_x+10)) and j in list(range(food_y, food_y+10)):
                    food_x = random.randrange(0, width-snake)
                    food_y = random.randrange(60, height-snake)
                    score += 1
                    speed += 0.5

        clock.tick(speed)

    dis.fill(white)
    if score==highest_score:
        file = open(src, "w+")
        file.write(str(score))
        file.close()
    message("You lost",black, 300, 100)
    message("Your score is "+str(score),black, 250, 150)
    message("Press Q to quit or C to play again", black, 110, 250)
    message("Mohamed Nasraoui",black, 263, 440, 30)
    pg.display.update()
    while game_close==False:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_q:
                    game_close = True
                elif event.key==pg.K_c:
                    game_close = False
                    game_loop()

    pg.quit()
    quit()

game_loop()
