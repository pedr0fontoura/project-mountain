from PPlay.window import *
from PPlay.sprite import *
from player import Player
from platform import Platform

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720

  TITLE = 'Project Mountain v1.0.0-alpha'

  BACKGROUND_PATH = 'assets/bg.png'

  def __init__(self):
    self.window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
    self.window.set_title(Game.TITLE)

    self.keyboard = self.window.get_keyboard()
    self.mouse = self.window.get_mouse()

    self.background = Sprite(Game.BACKGROUND_PATH)

    self.player = Player(self)
    self.platform = Platform(self)

  def tick(self):
    self.background.draw()

    self.player.tick()
    self.platform.tick()

    self.window.update()