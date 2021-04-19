import math
import random
import pygame
from platform import Platform

Vector2 = pygame.math.Vector2

class MapManager:

  def __init__(self, game):
    self.game = game
    self.platforms = []

  def generateGround(self):
    self.platforms.append(Platform(self.game, self.game.GROUND_X, self.game.GROUND_Y))

    platformWidth = self.platforms[0].sprite.width - 20

    platformNumber = int(math.ceil(self.game.window.width / platformWidth))

    for i in range(1, platformNumber):
      self.platforms.append(Platform(self.game, self.game.GROUND_X + platformWidth * i, self.game.GROUND_Y))

  def points(self, number, center, radius):
    pointList = []
    for i in range(number):
      angle = random.randint(45, 135)

      base = center

      if (i > 1):
        base = pointList[i - 1]
      
      vec = base + Vector2(128, 0).rotate(-angle)

      if (vec.x <= base.x):
        vec.x -= 192

      pointList.append(Vector2(int(vec.x), int(vec.y)))
    return pointList

  def createPlatforms(self):
    ply = self.game.player
    x = ply.x + ply.sprite.width / 2
    y = ply.y + ply.sprite.height / 2
    
    pcoords = self.points(5, Vector2(x, y), 64)
    
    for coords in pcoords:
      platform = Platform(self.game, coords.x, coords.y)

      self.platforms.append(platform)

  def tick(self):
    for platform in self.platforms:
      platform.tick()

    if (self.game.DEBUG):
      ply = self.game.player
      x = ply.x + ply.sprite.width / 2
      y = ply.y + ply.sprite.height / 2

      pygame.draw.rect(self.game.window.screen, (255, 0, 0), (ply.x, ply.y, ply.sprite.width, ply.sprite.height))
      pygame.draw.circle(self.game.window.screen, (255, 0, 0), (x, y), 128, True)