from bird import Bird
from obstacle import Obstacle
from random import randint, uniform
import neuralnetwork
import my_matrix_lib as matrix
import copy


obstacle = []
birds = []
saved_birds = []
birdcount = 10


def setup():
    size(900, 500)
    for i in range(birdcount):
        birds.append(Bird(100, height/2, height, nn = neuralnetwork.NeuralNetwork([6, 64, 1])))
                       
    for i in range(int((width/180))):
        obstacle.append(Obstacle(400 + 200*i, randint(50, height - 150), height, 150))


def draw():
    background(51)
    
    for i in range(10):
        for bird_obj in birds:
            if bird_obj.alive:
                bird_obj.off_window()
                bird_obj.obs_hit(obstacle[0])
                bird_obj.choice(obstacle[0])
                bird_obj.update()
                bird_obj.score_ += 1
            else:
                saved_birds.append(birds[birds.index(bird_obj)])
                del(birds[birds.index(bird_obj)])
                
        if len(birds) == 0:
            reset_pop()
        
        for obs in obstacle:
            obs.update()
        if obstacle[0].x + obstacle[0].x_size < 0:
            del(obstacle[0])
            obstacle.append(Obstacle(obstacle[-1].x + 200, randint(50, height - 150), height, 150))
    
    for bird_obj in birds:    
        bird_obj.show()
        bird_obj.obs_pass(obstacle[0])
        draw_score(bird_obj)
    
    for obs in obstacle:
        obs.show()


def draw_score(bird):
    push()
    rectMode(CENTER)
    textAlign(CENTER)
    fill(0)
    translate(bird.x, bird.y)
    text(str(bird.score), 0, 0)
    pop()


def reset_pop():
    calc_fitness()
    del(birds[:])
    for i in range(birdcount):
        birds.append(pick_bird())
    
    del(saved_birds[:])
    
    del(obstacle[:])
    for i in range(int((width/180))):
        obstacle.append(Obstacle(400 + 200*i, randint(50, height - 150), height, 150))
        

def pick_bird():
    index = 0
    r = uniform(0, 1)
    while r > 0:
        r = r - saved_birds[index].fitness
        index += 1
    index -= 1
    
    bird = saved_birds[index]
    child = Bird(100, height/2, height, nn = bird.brain)
    child.brain.mutate(0.1)
    return child


def calc_fitness():
    sum = 0
    overall = 0
    for bird in saved_birds:
        sum += bird.score_
    for bird in saved_birds:
        bird.fitness += float(bird.score_)/float(sum)
        overall += bird.fitness
