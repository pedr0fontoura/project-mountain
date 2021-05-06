from os import path

from PPlay.window import *
from PPlay.sprite import *

from player import Player
from platform import Platform
from mapmanager import MapManager

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720
  TITLE = 'Project Mountain v1.0.0-alpha'
  DEBUG = 0

  SAVE_PATH = 'save.txt'
  
  BACKGROUND_PATH = 'assets/bg.png'
  LOGO_PATH = 'assets/logo.png'
  FADE_PATH = 'assets/fade.png'
  ACTION_PATH = 'assets/action.png'

  GROUND_X = -10
  GROUND_Y = 710

  DESCENT_SPEED = 60

  def __init__(self):
    self.window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
    self.window.set_title(Game.TITLE)

    self.keyboard = self.window.get_keyboard()
    self.mouse = self.window.get_mouse()

    self.dir = path.dirname(__file__)

    self.background = Sprite(Game.BACKGROUND_PATH)
    self.logo = Sprite(Game.LOGO_PATH)
    self.fade = Sprite(Game.FADE_PATH)
    self.action = Sprite(Game.ACTION_PATH)

    self.logo.x = self.window.width / 2 - self.logo.width / 2
    self.logo.y = 100

    self.action.x = self.window.width / 2 - self.action.width / 2
    self.action.y = self.window.height / 2 + self.action.height

    self.isGameStarted = False

    self.mapManager = MapManager(self)
    self.mapManager.init()

    self.player = Player(self)

    self.highScore = self.readHighScore()
    self.score = 0

  def readHighScore(self):
    data = None

    try:
      file = open(path.join(self.dir, Game.SAVE_PATH), 'w')
      data = int(file.read())
      file.close()
    except:
      data = 0

    return data

  def writeHighScore(self):
    try:
      file = open(path.join(self.dir, Game.SAVE_PATH), 'w')
      file.write(str(self.highScore))
      file.close()
    except:
      return

  def stop(self):
    self.isGameStarted = False

    if (self.score > self.highScore):
      self.highScore = self.score
      self.writeHighScore()

    self.score = 0

    self.player = Player(self)
    self.mapManager = MapManager(self)
    self.mapManager.init()

  def tick(self):
    self.background.draw()
    
    self.mapManager.tick()
    self.player.tick()

    if (self.isGameStarted):

      if (self.score > 0):
        self.player.descend(Game.DESCENT_SPEED)
        self.mapManager.descend(Game.DESCENT_SPEED)

      if (self.keyboard.key_pressed('ESC')):
        self.stop()

    else:
      self.fade.draw()
      self.logo.draw()
      self.action.draw()

      if (self.keyboard.key_pressed('SPACE')):
        self.isGameStarted = True

    self.window.update()