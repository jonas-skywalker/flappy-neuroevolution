import neuralnetwork
import my_matrix_lib as matrix


class Bird:
    def __init__(self, x, y, windowh, nn = None):
        if nn:
            self.brain = nn
        self.x = x
        self.y = y
        self.vel = 0
        self.grav = 0.3
        self.r = 20
        self.score = 0
        self.windowheight = windowh
        self.alive = True
    
    def update(self):
        self.vel += self.grav
        self.y += self.vel
    
    def show(self):
        push()
        fill(255, 255, 255, 255/2)
        circle(self.x, self.y, self.r)
        pop()
    
    def jump(self):
        self.vel -= 8
        # make space key released for real game
    
    def obs_pass(self, obs):
        if self.x == obs.x + obs.x_size:
            self.score += 1

    def obs_hit(self, obs):
        if (obs.x < self.x < obs.x + obs.x_size) and ((0 < self.y < obs.y_top) or (obs.y_top + obs.distance < self.y < obs.windowheight)):
            self.alive = False
            self.score = 0
            return True
        return False
    
    def off_window(self):
        if (self.y < 0) or (self.y > self.windowheight):
            self.alive = False
            self.score = 0
            return True
        return False
            
    def choice(self, obs):
        distance = obs.x - self.x
        input_list = [self.x, self.y, self.vel, distance, obs.y_top, obs.y_top + obs.distance]
        # feedforward
        output = self.brain.feed_forward(input_list)
        # do action
        # print(output.matrix_data[0][0])
        if output.matrix_data[0][0] < 0.5:
            self.jump()
        else:
            pass
