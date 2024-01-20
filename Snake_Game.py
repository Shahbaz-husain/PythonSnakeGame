import pygame
pygame.init()
pygame.mixer.init()
import random
import os


screen_width = 1000
screen_height = 500

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My Snake Game')
pygame.display.update()
font= pygame.font.SysFont(None,30)
clock = pygame.time.Clock()

bg= pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()


#Colors :
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = ( 0 , 255,0)
blue = (0,0,255)
orange = (255,204,153)


def create_snake(snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,white,[x,y,snake_size,snake_size])

def screen_text(text,color,x,y):
    stext=font.render(text,True,color)
    gameWindow.blit(stext,[x,y])
    

def welcome():
    exit_game = False
    while not exit_game :
        gameWindow.fill(black)
        screen_text('Press Enter to Enter the Game',red,(screen_width/2)-150,(screen_height/2)-50)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game=True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # pygame.mixer.music.load('bg.mp3')
                    # pygame.mixer.music.play()
                    gameloop()

                if event.key == pygame.K_ESCAPE:
                    exit_game=True

        pygame.display.update()
        clock.tick(30)


def gameloop():
#Game Variables
    game_over = False
    exit_game = False
    fps = 60
    snake_size= 20
    snake_x=45
    snake_y=45
    velocity_x=0
    velocity_y=0
    score=0
    initvelocity = 3
    food_x=random.randint(10,screen_width-50)
    food_y=random.randint(100,screen_height-20)
    snake_len=1
    snake_list=[]

    if (not os.path.exists('highscore.txt')):
        with open('highscore.txt','w')as f:
            f.write('0')

    with open('highscore.txt') as f:
            highscore=f.read()

    while not exit_game:
        
        if game_over :
            gameWindow.fill(black)
            screen_text('Game Over',red,(screen_width/2)-60,screen_height/2)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                    if event.key==pygame.K_ESCAPE:
                        exit_game=True
                if event.type==pygame.QUIT:
                    exit_game=True
        else:
            
            for event in pygame.event.get():


                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x+=initvelocity
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x-=initvelocity
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_y-=initvelocity
                        velocity_x=0

                    if event.key == pygame.K_DOWN:
                        velocity_y+=initvelocity
                        velocity_x=0

                    if event.key == pygame.K_SPACE:
                        velocity_x=0
                        velocity_y=0

                    if event.key==pygame.K_ESCAPE:
                        exit_game=True

                    if event.key == pygame.K_q:
                        score+=5

                    if event.key == pygame.K_v:
                        initvelocity+=1

                    if event.key==pygame.K_b:
                        initvelocity-=1
                    

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                pygame.mixer.music.load('gulp2.mp3')
                pygame.mixer.music.play()
                score+=10
                # print('Score : ',score*10)
                snake_len+=5
                food_x=random.randint(0,screen_width/2)
                food_y=random.randint(0,screen_height/2)
                if score>int(highscore):
                    with open('highscore.txt','w') as f:
                        highscore=score
                        f.write(str(score))
        
            gameWindow.blit(bg,(0,0))

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_len:
                del snake_list[0]

            screen_text('Score : '+str(score),blue,0,0)

            screen_text('Highscore : '+str(highscore),white,(screen_width/2)-20,0)


            pygame.draw.circle(gameWindow,red,[food_x,food_y],(snake_size/2)+5)
            pygame.draw.rect(gameWindow,white,[snake_x,snake_y,snake_size,snake_size])

            create_snake(snake_list,snake_size)

            if (snake_x<=0 or snake_x>=screen_width or snake_y<=0 or snake_y>=screen_height):
                game_over=True
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()

            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()

            # for x,y in snake_list[:-1]:
            #     if snake_x==x and snake_y==y :
            #         game_over=True 

            
            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()




if __name__=='__main__':
    # gameloop()
    welcome()