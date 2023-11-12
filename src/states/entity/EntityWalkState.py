import random

from src.states.BaseState import BaseState
from src.constants import *

class EntityWalkState(BaseState):
    def __init__(self, entity, dungeon=None):
        self.entity = entity
        self.entity.ChangeAnimation('down')
        self.dungeon = dungeon

        #AI control
        self.move_duration = 0
        self.movement_timer = 0

        #hit wall?
        self.bumped = False
        self.step_count = 0

    def update(self, dt, events):
        self.bumped = False
        steps_to_walk =  48  # Set total distance to walk based on dice roll

        while steps_to_walk > 0:  # Continue moving as long as we have distance left
            if self.entity.direction == "right":
                self.entity.MoveX(48)  # Move entity
                steps_to_walk -= 48  # Subtract the moved distance from remaining distance
                if self.entity.rect.x + self.entity.width >= WIDTH - TILE_SIZE * 2:
                    self.entity.ChangeCoord(x=WIDTH - TILE_SIZE * 2 - self.entity.width)
                    self.bumped = True

            elif self.entity.direction == 'up':
                self.entity.MoveY(-48)
                steps_to_walk -= 48
                if self.entity.rect.y <= MAP_RENDER_OFFSET_Y + TILE_SIZE - self.entity.height / 2:
                    self.entity.ChangeCoord(y=MAP_RENDER_OFFSET_Y + TILE_SIZE - self.entity.height / 2)
                    self.bumped = True

            elif self.entity.direction == 'down':
                self.entity.MoveY(48)
                steps_to_walk -= 48
                bottom_edge = HEIGHT - (HEIGHT - MAP_HEIGHT * TILE_SIZE) + MAP_RENDER_OFFSET_Y - TILE_SIZE
                if self.entity.rect.y + self.entity.height >= bottom_edge:
                    self.entity.ChangeCoord(y=bottom_edge - self.entity.height)
                    self.bumped = True
        
        # If we've done walking or hit an obstacle, reset dice_roll and change state to idle
        if steps_to_walk <= 0 or self.bumped:
            self.entity.dice_roll = 0
            self.entity.ChangeState('idle')

    def Enter(self, params):
        pass
    def Exit(self):
        pass

    def ProcessAI(self, params, dt):
        room = params['room']
        directions = ['left', 'right', 'up', 'down']

        if self.move_duration == 0 or self.bumped:
            self.move_duration = random.randint(0, 5)
            self.entity.direction = random.choice(directions)
            self.entity.ChangeAnimation(self.entity.direction)

        elif self.movement_timer > self.move_duration:
            self.movement_timer = 0
            if random.randint(0, 3) == 1:
                self.entity.ChangeState('idle')
            else:
                self.move_duration = random.randint(0, 5)
                self.entity.direction = random.choice(directions)
                self.entity.ChangeAnimation(self.entity.direction)

        self.movement_timer = self.movement_timer+dt


    def render(self, screen):
        animation = self.entity.curr_animation.image

        screen.blit(animation, (math.floor(self.entity.rect.x - self.entity.offset_x),
                    math.floor(self.entity.rect.y - self.entity.offset_y)))