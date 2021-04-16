from PPlay.sprite import *

class Platform:
  SPRITE_PATH = 'assets/platform.png'

  idx = 0

  def __init__(self, game, x, y):
    self.id = Platform.idx
    Platform.idx += 1

    self.game = game

    self.sprite = Sprite(Platform.SPRITE_PATH)

    self.x = x
    self.y = y

    self.sprite.x = self.x
    self.sprite.y = self.y

  def draw(self):
    self.sprite.x = self.x
    self.sprite.y = self.y
    self.sprite.draw()

  def tick(self):
    # If platform is out of bounds, remove from pool
    if (self.y >= self.game.WINDOW_HEIGHT):
      for platform in self.game.platforms:
        if (platform.id == self.id):
          self.game.platforms.remove(platform)
      return

    self.draw()

