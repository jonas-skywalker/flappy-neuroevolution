from bird import Bird
from obstacle import Obstacle
from random import randint


player = None
obstacle = []
dead = False


def setup():
    size(900, 500)
    #fullScreen()
    global player
    player = Bird(100, height/2, height)
                       
    for i in range(int((width/180))):
        obstacle.append(Obstacle(400 + 200*i, randint(50, height - 150), height, 150))


def draw():
    background(51)
    
    player.off_window()
    player.obs_hit(obstacle[0])
    player.update()
    player.show()
    player.obs_pass(obstacle[0])
    draw_score(player)
    
    for obs in obstacle:
        obs.update()
        obs.show()
    if obstacle[0].x + obstacle[0].x_size < 0:
        del(obstacle[0])
        obstacle.append(Obstacle(obstacle[-1].x + 200, randint(50, height - 150), height, 150))
    
    if player.alive == False:
        reset_game()        
    

def keyPressed():
    player.jump()


def draw_score(bird):
    push()
    rectMode(CENTER)
    textAlign(CENTER)
    fill(0)
    translate(bird.x, bird.y)
    text(str(bird.score), 0, 0)
    pop()


def reset_game():
    player.alive = True
    player.x = 100
    player.y = height/2
    player.vel = 0    
    del(obstacle[:])
    for i in range(int((width/180))):
        obstacle.append(Obstacle(400 + 200*i, randint(50, height - 150), height, 150))
