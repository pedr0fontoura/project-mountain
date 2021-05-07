from PPlay.sprite import *

class HighScoreMarker:
  
  SPRITE_PATH = 'assets/woodsign.png'
  SPRITE_FRAMES = 7
  ANIM_DURATION = 1000

  OFFSET_Y = 12

  def __init__(self, game, x, y):
    self.game = game

    self.sprite = Sprite(HighScoreMarker.SPRITE_PATH, HighScoreMarker.SPRITE_FRAMES)
    self.sprite.set_sequence(0, HighScoreMarker.SPRITE_FRAMES, False)
    self.sprite.set_total_duration(HighScoreMarker.ANIM_DURATION)
    self.sprite.stop()

    self.x = x - self.sprite.width / 2
    self.y = y - self.sprite.height + HighScoreMarker.OFFSET_Y

    self.sprite.x = self.x
    self.sprite.y = self.y

    self.animationPlayed = False

  def draw(self):
    self.sprite.x = self.x
    self.sprite.y = self.y
    self.sprite.draw()
    self.sprite.update()

    textX = self.x + self.sprite.width / 2
    textY = (self.y + self.sprite.height / 2) - 6
    self.game.window.draw_text(str(self.game.highScore), textX, textY, 12, (255, 255, 255), "Arial")

  def tick(self):
    if (not self.animationPlayed and self.game.score > self.game.highScore):
      self.animationPlayed = True
      self.sprite.set_curr_frame(0)
      self.sprite.play()

    if (self.y >= self.game.WINDOW_HEIGHT):
      self.game.mapManager.highScoreMarker = None

    if (self.sprite.get_curr_frame() != HighScoreMarker.SPRITE_FRAMES - 1):
      self.draw()
    