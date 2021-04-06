from PPlay.sprite import *
from PPlay.collision import Collision

class Player:
  SPEED = 450
  GRAVITY = SPEED * 2

  COLLISION_THRESHOLD = 10

  SPRITE_IDLE_LEFT_PATH = 'assets/hiker/idleLeft.png'
  SPRITE_IDLE_RIGHT_PATH = 'assets/hiker/idleRight.png'
  SPRITE_IDLE_FRAMES = 6
  SPRITE_IDLE_ANIM_DURATION = 1000

  SPRITE_MOVE_LEFT_PATH = 'assets/hiker/moveLeft.png'
  SPRITE_MOVE_RIGHT_PATH = 'assets/hiker/moveRight.png'
  SPRITE_MOVE_FRAMES = 8
  SPRITE_MOVE_ANIM_DURATION = 500

  SPRITE_JUMP_LEFT_PATH = 'assets/hiker/jumpLeft.png'
  SPRITE_JUMP_RIGHT_PATH = 'assets/hiker/jumpRight.png'
  SPRITE_JUMP_FRAMES = 3
  SPRITE_JUMP_ANIM_DURATION = 500

  SPRITE_STATE = {
    'idleLeft': 0,
    'idleRight': 1,
    'moveLeft': 2,
    'moveRight': 3,
    'jumpLeft': 4,
    'jumpRight': 5,
  }

  def __init__(self, game):
    self.game = game

    self.sprites = []
    self.loadSprites()

    self.spriteState = 'idleRight'

    self.sprite = self.getSprite()

    self.x = self.game.window.width / 2 - self.sprite.width / 2
    self.y = self.game.window.height - self.sprite.height

    self.dx = 0
    self.dy = 0
    
    self.isJumping = False
    self.isFalling = False

  def loadSprites(self):
    idleLeft = Sprite(Player.SPRITE_IDLE_LEFT_PATH, Player.SPRITE_IDLE_FRAMES)
    idleLeft.set_total_duration(Player.SPRITE_IDLE_ANIM_DURATION)

    idleRight = Sprite(Player.SPRITE_IDLE_RIGHT_PATH, Player.SPRITE_IDLE_FRAMES)
    idleRight.set_total_duration(Player.SPRITE_IDLE_ANIM_DURATION)

    moveLeft = Sprite(Player.SPRITE_MOVE_LEFT_PATH, Player.SPRITE_MOVE_FRAMES)
    moveLeft.set_total_duration(Player.SPRITE_MOVE_ANIM_DURATION)

    moveRight = Sprite(Player.SPRITE_MOVE_RIGHT_PATH, Player.SPRITE_MOVE_FRAMES)
    moveRight.set_total_duration(Player.SPRITE_MOVE_ANIM_DURATION)

    jumpLeft = Sprite(Player.SPRITE_JUMP_LEFT_PATH, Player.SPRITE_JUMP_FRAMES)
    jumpLeft.set_sequence(0, 3, False)
    jumpLeft.set_total_duration(Player.SPRITE_JUMP_ANIM_DURATION)

    jumpRight = Sprite(Player.SPRITE_JUMP_RIGHT_PATH, Player.SPRITE_JUMP_FRAMES)
    jumpRight.set_sequence(0, 3, False)
    jumpRight.set_total_duration(Player.SPRITE_JUMP_ANIM_DURATION)

    self.sprites.append(idleLeft)
    self.sprites.append(idleRight)
    self.sprites.append(moveLeft)
    self.sprites.append(moveRight)
    self.sprites.append(jumpLeft)
    self.sprites.append(jumpRight)

  def idle(self):
    self.dx = 0

    if self.isJumping:
      return

    if (self.spriteState == 'moveLeft' or self.spriteState == 'jumpLeft'):
      self.spriteState = 'idleLeft'
    elif (self.spriteState == 'moveRight' or self.spriteState == 'jumpRight'):
      self.spriteState = 'idleRight'

  def moveLeft(self):
    self.dx = -Player.SPEED

    if not self.isJumping:
      self.spriteState = 'moveLeft'
    else:
      self.spriteState = 'jumpLeft'

  def moveRight(self):
    self.dx = Player.SPEED

    if not self.isJumping:
      self.spriteState = 'moveRight'
    else:
      self.spriteState = 'jumpRight'

  def jump(self):
    if (not self.isJumping):
      self.isJumping = True
      self.isFalling = True
      self.lastJump = 0
      self.dy = -Player.SPEED

      if (self.spriteState == 'moveLeft' or self.spriteState == 'idleLeft'):
        self.spriteState = 'jumpLeft'
      elif (self.spriteState == 'moveRight' or self.spriteState == 'idleRight'):
        self.spriteState = 'jumpRight'

  def handleInputs(self):
    inputPressed = {
      'A': self.game.keyboard.key_pressed('A'),
      'LEFT': self.game.keyboard.key_pressed('LEFT'),
      'D': self.game.keyboard.key_pressed('D'),
      'RIGHT': self.game.keyboard.key_pressed('RIGHT'),
      'SPACE': self.game.keyboard.key_pressed('SPACE'),
      'UP': self.game.keyboard.key_pressed('UP'),
    }

    moveLeft = inputPressed['A'] or inputPressed['LEFT']
    moveRight = inputPressed['D'] or inputPressed['RIGHT']
    jump = inputPressed['SPACE'] or inputPressed['UP']

    if (moveLeft or moveRight or jump):
      if moveLeft:
        self.moveLeft()
      elif moveRight:
        self.moveRight()

      if jump:
        self.jump()
    else:
      self.idle()

  def getSprite(self):
    return self.sprites[Player.SPRITE_STATE[self.spriteState]]

  def draw(self):
    self.sprite = self.getSprite()

    self.sprite.x = self.x
    self.sprite.y = self.y

    self.sprite.draw()
    self.sprite.update()

  def handleCollision(self):
    for platform in self.game.platforms:
        if (self.sprite.collided(platform.sprite)):
          # Top
          if ((self.sprite.y + self.sprite.height - Player.COLLISION_THRESHOLD) <= platform.y):
            self.dy = 0
            self.y = platform.sprite.y - self.sprite.height

            if (self.isJumping):
              self.isJumping = False
          else:
            # Bottom
            if (self.dy < 0 and self.y >= platform.y + platform.sprite.height - Player.COLLISION_THRESHOLD):
              self.dy = 0
              self.y = platform.y + platform.sprite.height
            
            if (platform.y >= self.y and platform.y <= self.y + self.sprite.y or platform.y + platform.sprite.height >= self.y and platform.y + platform.sprite.height <= self.y + self.sprite.y):
              # Left
              if (self.dx > 0 and self.x <= platform.x):
                self.dx = 0
                self.x = platform.x - self.sprite.width
              
              # Right
              if (self.dx < 0 and self.x >= (platform.x + platform.sprite.width - Player.COLLISION_THRESHOLD)):
                self.dx = 0
                self.x = platform.x + platform.sprite.width

  def tick(self):
    self.dy += Player.GRAVITY * self.game.window.delta_time()

    self.x += self.dx * self.game.window.delta_time()
    self.y += self.dy * self.game.window.delta_time()

    self.handleCollision()

    if (self.y + self.sprite.height > self.game.window.height):
      self.y = self.game.window.height - self.sprite.height
      self.dy = 0
      self.isJumping = False
      self.idle()

    if (self.x >= self.game.window.width):
      self.x = 0

    if (self.x + self.sprite.width <= 0):
      self.x = self.game.window.width - self.sprite.width

    self.dx = 0

    self.handleInputs()
    self.draw()