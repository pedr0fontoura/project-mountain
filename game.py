from PPlay.window import *
from PPlay.sprite import *
import math
from player import Player
from platform import Platform

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720

  TITLE = 'Project Mountain v1.0.0-alpha'

  BACKGROUND_PATH = 'assets/bg.png'

  GROUND_X = -10
  GROUND_Y = 710

  def __init__(self):
    self.window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
    self.window.set_title(Game.TITLE)

    self.keyboard = self.window.get_keyboard()
    self.mouse = self.window.get_mouse()

    self.background = Sprite(Game.BACKGROUND_PATH)

    self.player = Player(self)
    self.platforms = []

    self.generateGround()

  def generateGround(self):
    self.platforms.append(Platform(self, Game.GROUND_X, Game.GROUND_Y))

    platformWidth = self.platforms[0].sprite.width - 20

    platformNumber = int(math.ceil(self.window.width / platformWidth))

    for i in range(1, platformNumber):
      self.platforms.append(Platform(self, Game.GROUND_X + platformWidth * i, Game.GROUND_Y))

  def tick(self):
    self.background.draw()

    self.player.tick()
    
    for platform in self.platforms:
      platform.tick()

    self.window.update()