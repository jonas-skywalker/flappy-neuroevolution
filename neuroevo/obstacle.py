class Obstacle:
    def __init__(self, x, y_top, windowheight, distance):
        self.x = x
        self.y_top = y_top
        self.vel = -2
        self.x_size = 50
        self.windowheight = windowheight
        self.distance = distance
    
    def update(self):
        self.x += self.vel
        
    def show(self):
        push()
        fill(255, 255, 255)
        rect(self.x, 0, self.x_size, self.y_top)
        rect(self.x, self.y_top + self.distance, self.x_size, self.windowheight - self.y_top + self.distance)
        pop()
