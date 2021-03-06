import pygame
from jumper.entities.bullet import Bullet
from math import pi, sin, cos

class BBBullet(Bullet):
    def __init__(self, environment, position, angle, speed=1000):
        super().__init__(environment, position)

        self.speed = speed
        self.angle = angle

    def update(self, delta):
        if not self.is_alive:
            return

        x = self.position.x + self.speed * delta * cos(self.angle / 180 * pi)
        y = self.position.y + self.speed * delta * sin(self.angle / 180 * pi)

        camera = self.environment.camera
        (bound_x, bound_y) = self.environment.scene.get_bound()

        if (x < 0 or x > bound_x) or (y > bound_y + camera.pos() or y < 0):
            self.destory()
        else:
            self.set_position(x, y)

    def render_bullet(self, surface, position):
        (w, h) = self.get_size().int()
        (x, y) = int(position[0] + w/2), int(position[1] + h/2)
        r = int(w/2)

        pygame.draw.circle(surface, self.get_color(), (x, y), r)

    def get_color(self):
        return (255, 255, 0)
