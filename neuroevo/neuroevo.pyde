from bird import Bird
from obstacle import Obstacle
from random import randint
import neuralnetwork
import my_matrix_lib as matrix


player = None
obstacle = []
birds = []
birdcount = 10


def setup():
    size(900, 500)
    #fullScreen()
    #global player
    #player = Bird(100, height/2, height, nn = neuralnetwork.NeuralNetwork([6, 64, 1]))
    for i in range(birdcount):
        birds.append(Bird(100, height/2, height, nn = neuralnetwork.NeuralNetwork([6, 64, 1])))
                       
    for i in range(int((width/180))):
        obstacle.append(Obstacle(400 + 200*i, randint(50, height - 150), height, 150))


def draw():
    global deathcount
    background(51)
    
    for bird_obj in birds:
        if bird_obj.alive:
            bird_obj.off_window()
            bird_obj.obs_hit(obstacle[0])
            bird_obj.choice(obstacle[0])
            bird_obj.update()
            bird_obj.show()
            bird_obj.obs_pass(obstacle[0])
            draw_score(bird_obj)
        else:
            del(birds[birds.index(bird_obj)])
            
    if len(birds) == 0:
        reset_game()
    
    for obs in obstacle:
        obs.update()
        obs.show()
    if obstacle[0].x + obstacle[0].x_size < 0:
        del(obstacle[0])
        obstacle.append(Obstacle(obstacle[-1].x + 200, randint(50, height - 150), height, 150))
    

'''
def keyPressed():
    player.jump()
'''


def draw_score(bird):
    push()
    rectMode(CENTER)
    textAlign(CENTER)
    fill(0)
    translate(bird.x, bird.y)
    text(str(bird.score), 0, 0)
    pop()


def reset_game():
    del(birds[:])
    for i in range(birdcount):
        birds.append(Bird(100, height/2, height, nn = neuralnetwork.NeuralNetwork([6, 64, 1])))
    
    del(obstacle[:])
    for i in range(int((width/180))):
        obstacle.append(Obstacle(400 + 200*i, randint(50, height - 150), height, 150))
