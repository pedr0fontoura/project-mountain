import math
import random
import pygame
from platform import Platform
from highscore import HighScoreMarker

class MapManager:
  PLATFORM_WIDTH = 196
  PLATFORM_HEIGHT = 32

  DISTANCE_Y = 72

  def __init__(self, game):
    self.game = game

    self.platformIdx = 0
    self.platformCount = 0
    self.platforms = []

    self.highScoreMarker = None

  def generateGround(self):
    self.platforms.append(Platform(self.game, 0, self.game.GROUND_X, self.game.GROUND_Y, True))

    platformWidth = self.platforms[0].sprite.width - 20

    platformNumber = int(math.ceil(self.game.window.width / platformWidth))

    for i in range(1, platformNumber):
      self.platforms.append(Platform(self.game, 0, self.game.GROUND_X + platformWidth * i, self.game.GROUND_Y, True))

  def createPlatform(self):
    nPlatforms = len(self.platforms) - 1
    
    x = random.randrange(0, self.game.WINDOW_WIDTH - MapManager.PLATFORM_WIDTH)
    y = self.game.GROUND_Y

    if (nPlatforms >= 0):
      lastPlatform = self.platforms[nPlatforms]

      options = []

      if (lastPlatform.x - MapManager.PLATFORM_WIDTH > 0):
        options.append(random.randrange(0, lastPlatform.x - MapManager.PLATFORM_WIDTH))

      if (self.game.WINDOW_WIDTH - MapManager.PLATFORM_WIDTH > lastPlatform.x + MapManager.PLATFORM_WIDTH):
        options.append(random.randrange(lastPlatform.x + MapManager.PLATFORM_WIDTH, self.game.WINDOW_WIDTH - MapManager.PLATFORM_WIDTH))

      x = random.choice(options)

      y = lastPlatform.y - (MapManager.DISTANCE_Y + MapManager.PLATFORM_HEIGHT)

    self.platformIdx += 1

    if (self.platformIdx == self.game.highScore):
      self.highScoreMarker = HighScoreMarker(self.game, x + MapManager.PLATFORM_WIDTH / 2, y)

    self.platforms.append(Platform(self.game, self.platformIdx, x, y))

  def generateMap(self):
    while (self.platformCount < int(self.game.WINDOW_HEIGHT / (MapManager.DISTANCE_Y + MapManager.PLATFORM_HEIGHT))):
      self.createPlatform()

  def init(self):
    self.generateGround()
    self.generateMap()

  def descend(self, distance):
    deltaTime = self.game.window.delta_time()

    for platform in self.platforms:
      platform.y += distance * deltaTime

    if (self.highScoreMarker):
      self.highScoreMarker.y += distance * deltaTime

  def tick(self):
    if (self.game.isGameStarted):
      if (self.platformCount < int(self.game.WINDOW_HEIGHT / (MapManager.DISTANCE_Y + MapManager.PLATFORM_HEIGHT)) + 1):
        self.createPlatform()

    if (self.highScoreMarker):
      self.highScoreMarker.tick()

    for platform in self.platforms:
      platform.tick()

    if (self.game.DEBUG > 0):
      ply = self.game.player
      x = ply.x + ply.sprite.width / 2
      y = ply.y + ply.sprite.height / 2

      pygame.draw.rect(self.game.window.screen, (255, 0, 0), (ply.x, ply.y, ply.sprite.width, ply.sprite.height), True)
      pygame.draw.circle(self.game.window.screen, (255, 0, 0), (x, y), 128, True)