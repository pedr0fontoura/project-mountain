from PPlay.window import *
from player import Player

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720

  TITLE = 'Project Mountain v1.0.0-alpha'

  def __init__(self):
    self.window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
    self.window.set_title(Game.TITLE)

    self.keyboard = self.window.get_keyboard()
    self.mouse = self.window.get_mouse()

    self.player = Player(self)

  def tick(self):
    self.window.set_background_color((0, 0, 0))

    self.player.tick()

    self.window.update()