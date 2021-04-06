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
  FADE_PATH = 'assets/fade.png'
  ACTION_PATH = 'assets/action.png'

  GROUND_X = -10
  GROUND_Y = 710

  PLATFORM_SPAWN_AREA = WINDOW_WIDTH / 4

  def __init__(self):
    self.window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
    self.window.set_title(Game.TITLE)

    self.keyboard = self.window.get_keyboard()
    self.mouse = self.window.get_mouse()

    self.background = Sprite(Game.BACKGROUND_PATH)
    self.logo = Sprite(Game.LOGO_PATH)
    self.fade = Sprite(Game.FADE_PATH)
    self.action = Sprite(Game.ACTION_PATH)

    self.logo.x = self.window.width / 2 - self.logo.width / 2
    self.logo.y = 100

    self.action.x = self.window.width / 2 - self.action.width / 2
    self.action.y = self.window.height / 2 + self.action.height

    self.isGameStarted = False

    self.player = Player(self)
    self.platforms = []

    self.generateGround()

  def generateGround(self):
    self.platforms.append(Platform(self, Game.GROUND_X, Game.GROUND_Y))

    platformWidth = self.platforms[0].sprite.width - 20

    platformNumber = int(math.ceil(self.window.width / platformWidth))

    for i in range(1, platformNumber):
      self.platforms.append(Platform(self, Game.GROUND_X + platformWidth * i, Game.GROUND_Y))

  def generateMap(self):
    platformNumber = 8

    sprite = Platform(self, 0, 0).sprite

    x = Game.WINDOW_WIDTH / 2 - Game.PLATFORM_SPAWN_AREA
    y = Game.GROUND_Y - int(self.player.sprite.height * 1.2)

    leftRight = False
    for i in range(platformNumber):
      self.platforms.append(Platform(self, x, y))

      leftRight = not leftRight
      if (leftRight):
        x += sprite.width + self.player.sprite.width * 2
      else:
        x -= sprite.width + self.player.sprite.width * 2

      y -= int(self.player.sprite.height * 1.2)
      

  def tick(self):
    self.background.draw()
    
    self.player.tick()
    
    for platform in self.platforms:
      platform.tick()

    if (not self.isGameStarted):
      self.fade.draw()
      self.logo.draw()
      self.action.draw()

      if (self.keyboard.key_pressed('SPACE')):
        self.isGameStarted = True
        self.generateMap()

    self.window.update()