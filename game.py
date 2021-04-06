import math
import random
from PPlay.window import *
from PPlay.sprite import *
from player import Player
from platform import Platform

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720
  TITLE = 'Project Mountain v1.0.0-alpha'
  BACKGROUND_PATH = 'assets/bg.png'
  LOGO_PATH = 'assets/logo.png'

  GROUND_X = -10
  GROUND_Y = 710

  PLATFORMS = [
    {'x': 348, 'y': 600},
    {'x': 448, 'y': 300},
    {'x': 448, 'y': 50},
    {'x': 848, 'y': 230},
    {'x': 120, 'y': 230},
    {'x': 640, 'y': 560},
    {'x': 820, 'y': 432},
  ]

  def __init__(self):
    self.window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
    self.window.set_title(Game.TITLE)

    self.keyboard = self.window.get_keyboard()
    self.mouse = self.window.get_mouse()

    self.background = Sprite(Game.BACKGROUND_PATH)
    self.logo = Sprite(Game.LOGO_PATH)

    self.logo.x = self.window.width / 2 - self.logo.width / 2
    self.logo.y = 100

    self.player = Player(self)
    self.platforms = []

    self.generateGround()
    self.generateMap()

    """ for platform in Game.PLATFORMS:
      self.platforms.append(Platform(self, platform['x'], platform['y'])) """

  def generateGround(self):
    self.platforms.append(Platform(self, Game.GROUND_X, Game.GROUND_Y))

    platformWidth = self.platforms[0].sprite.width - 20

    platformNumber = int(math.ceil(self.window.width / platformWidth))

    for i in range(1, platformNumber):
      self.platforms.append(Platform(self, Game.GROUND_X + platformWidth * i, Game.GROUND_Y))

  def generateMap(self):
    platformNumber = 5
    currentY = Game.GROUND_Y - self.player.sprite.height + 20

    for i in range(platformNumber):
      self.platforms.append(Platform(self, random.randrange(0 , self.window.width - 192), currentY))
      currentY -= self.player.sprite.height - 20

  def tick(self):
    self.background.draw()
    
    self.player.tick()
    
    for platform in self.platforms:
      platform.tick()

    #self.logo.draw()
    self.window.update()