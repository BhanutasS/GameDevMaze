from src.states.entity.EntityIdleState import EntityIdleState
import pygame
import random

class PlayerIdleState(EntityIdleState):
    def __init__(self, player):
        super(PlayerIdleState, self).__init__(player)
        self.dice_roll = 0  # Initialize dice_roll

    def Enter(self, params):
        self.entity.offset_y = 15
        self.entity.offset_x = 0
        super().Enter(params)

    def Exit(self):
        pass
    
    def roll_dice(self):
        self.dice_roll = random.randint(1, 6)  # Assuming a 6-sided dice
        return self.dice_roll

    def update(self, dt, events):
        if self.entity.button_pressed:  # Check if button was pressed in MapState
            self.entity.ChangeState('walk')
            self.entity.button_pressed = False  # Reset the flag after changing state