import pygame
from jumper.entities.weapon import Weapon
from jumper.entities.bullets.bb_bullet import BBBullet
from jumper.resource import R

class BBGun(Weapon):
    def __init__(self, environment, position):
        super().__init__(environment, position, 'BB Gun')
        self.image = pygame.transform.scale(R.get_image("bb_gun"), self.size.int())

    def trigger(self, env, player):
        x = player.get_position().x
        x = x if player.direction == 0 else x + 60
        y = player.get_position().y + 30

        env.add_bullet(BBBullet(env, (x, y), 90, speed=2000))
        R.play_sound("bb_gun")

    def get_color(self):
        return (255, 0, 255)
