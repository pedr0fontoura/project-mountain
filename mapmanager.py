import math
import random
import pygame
from platform import Platform

Vector2 = pygame.math.Vector2

class MapManager:
  PLATFORM_WIDTH = 196
  PLATFORM_HEIGHT = 32

  CHUNK_X_SIZE = PLATFORM_WIDTH
  CHUNK_Y_SIZE = PLATFORM_HEIGHT * 3

  DELTAS = [
    Vector2(1, 1),
    Vector2(-1, 1)
  ]

  DESCENT_SPEED = 5

  def __init__(self, game):
    self.game = game
    self.platforms = []

  def generateGround(self):
    self.platforms.append(Platform(self.game, self.game.GROUND_X, self.game.GROUND_Y))

    platformWidth = self.platforms[0].sprite.width - 20

    platformNumber = int(math.ceil(self.game.window.width / platformWidth))

    for i in range(1, platformNumber):
      self.platforms.append(Platform(self.game, self.game.GROUND_X + platformWidth * i, self.game.GROUND_Y))

  def descend(self, distance):
    deltaTime = self.game.window.delta_time()

    for platform in self.platforms:
      platform.y += distance * deltaTime

  def tick(self):
    for platform in self.platforms:
      platform.tick()

    if (self.game.DEBUG > 0):
      ply = self.game.player
      x = ply.x + ply.sprite.width / 2
      y = ply.y + ply.sprite.height / 2

      pygame.draw.rect(self.game.window.screen, (255, 0, 0), (ply.x, ply.y, ply.sprite.width, ply.sprite.height), True)
      pygame.draw.circle(self.game.window.screen, (255, 0, 0), (x, y), 128, True)