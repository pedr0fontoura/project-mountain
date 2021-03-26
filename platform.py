from PPlay.sprite import *

class Platform:
  SPRITE_PATH = 'assets/platform.png'

  COLLISION_Y_THRESHOLD = 10

  def __init__(self, game):
    self.game = game

    self.sprite = Sprite(Platform.SPRITE_PATH)

    self.x = self.game.window.width / 2 - self.sprite.width / 2
    self.y = self.game.window.height - 128

    self.sprite.x = self.x
    self.sprite.y = self.y

  def handleCollision(self):
    ply = self.game.player

    plyAbovePlatform = (ply.y + ply.sprite.height) <= self.y and (self.y - ply.y) <= ply.sprite.height + Platform.COLLISION_Y_THRESHOLD
    plyBetweenPlatformBoundaries = (ply.x + ply.sprite.width) > self.x and ply.x < (self.x + self.sprite.width)

    if (plyAbovePlatform):
      if (plyBetweenPlatformBoundaries):
        if(ply.isFalling):
          ply.y = self.y - ply.sprite.height
          ply.dy = 0
          ply.isFalling = False
          
          if (ply.isJumping):
            ply.isJumping = False
      elif (not ply.isFalling):
        ply.isFalling = True


  def tick(self):
    self.handleCollision()

    self.sprite.draw()

