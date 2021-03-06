# pyinstaller gets mad if we use native modules names for files

from PPlay.sprite import *

class Platform:
  SPRITE_PATH = 'assets/platform.png'

  def __init__(self, game, id, x, y, isGround = False):
    self.id = id

    self.game = game

    self.sprite = Sprite(Platform.SPRITE_PATH)

    self.x = x
    self.y = y

    self.sprite.x = self.x
    self.sprite.y = self.y

    self.isGround = isGround
    
    if (not self.isGround):
      self.game.mapManager.platformCount += 1

  def draw(self):
    self.sprite.x = self.x
    self.sprite.y = self.y
    self.sprite.draw()

    if (self.game.DEBUG > 1):
      self.game.window.draw_text("{} , {}".format(self.x, self.y), self.x - 15, self.y, 12, (255, 0, 0), "Arial")

  def tick(self):
    # If platform is out of bounds, remove from pool
    if (self.y >= self.game.WINDOW_HEIGHT):
      if (not self.isGround):
        self.game.mapManager.platformCount -= 1

      for platform in self.game.mapManager.platforms:
        if (platform.id == self.id):
          self.game.mapManager.platforms.remove(platform)

      return

    self.draw()

