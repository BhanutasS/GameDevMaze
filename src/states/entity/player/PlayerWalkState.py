from src.constants import *
from src.states.entity.EntityWalkState import EntityWalkState
import random
import pygame, time

class PlayerWalkState(EntityWalkState):
    def __init__(self, player, dungeon):
        super(PlayerWalkState, self).__init__(player, dungeon)
        self.entity.ChangeAnimation('down')
        self.dungeon = dungeon
        self.dice_roll = 0

    def Exit(self):
        pass

    def roll_dice(self):
        self.dice_roll = random.randint(1, 6)  # Assuming a 6-sided dice
        return self.dice_roll

    def Enter(self, params):
        self.entity.offset_y = 15
        self.entity.offset_x = 0
    
    def CheckPath(self):
        if not hasattr(self, 'directions'):  
            self.directions = ['right','up','down']
        if self.bumped:
            self.bumped = False
            if not self.directions:
                # If all directions have been tried and resulted in a bump
                # Reset the direction list and exit the function
                self.directions = ['right','up','down']
                return
            self.entity.direction = random.choice(self.directions)  
            self.directions.remove(self.entity.direction)  
            self.entity.x = self.entity.x + 16
            # Check if new direction causes a bump
            # Code to determine if bumped should go here. If bumped is True, function will recursively call itself.
        else:
            return

    def update(self, dt, events):
        if self.entity.button_pressed:
               self.entity.direction = 'right'  # Set direction here
               self.entity.ChangeAnimation('right')  # Set animation here

        else:
            self.entity.ChangeState('idle')

        super().update(dt, events) 


        if self.bumped:
            if self.entity.direction == 'right':
                self.entity.x = self.entity.x + PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.y + 24
                        self.dungeon.BeginShifting(WIDTH, 0)
                        self.bumped = False

                self.entity.x = self.entity.x - PLAYER_WALK_SPEED * dt
                self.CheckPath()

            elif self.entity.direction == 'up':
                self.entity.y = self.entity.y - PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.x + 24
                        self.dungeon.BeginShifting(0,  -HEIGHT)
                        self.bumped = False

                self.entity.y = self.entity.y + PLAYER_WALK_SPEED * dt
                self.CheckPath()

            else:
                self.entity.y = self.entity.y + PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.x + 24
                        self.dungeon.BeginShifting(0,  HEIGHT)
                        self.bumped = False

                self.entity.y = self.entity.y - PLAYER_WALK_SPEED * dt
                self.CheckPath()