from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, 'white', self.position, 
                                  self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)

        vector_1 = self.velocity.rotate(new_angle)
        vector_2 = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        roid1 = Asteroid(self.position.x, self.position.y, new_radius)
        roid1.velocity = vector_1 * 1.2
        
        roid2 = Asteroid(self.position.x, self.position.y, new_radius)
        roid2.velocity = vector_2 * 1.2
