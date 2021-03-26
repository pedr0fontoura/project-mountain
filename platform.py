from PPlay.sprite import *

class Platform:
  SPRITE_PATH = 'assets/platform.png'

  COLLISION_Y_THRESHOLD = 10

  def __init__(self, game, x, y):
    self.game = game

    self.sprite = Sprite(Platform.SPRITE_PATH)

    self.x = x
    self.y = y

    self.sprite.x = self.x
    self.sprite.y = self.y

  def tick(self):
    self.sprite.draw()

