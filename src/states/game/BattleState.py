from src.states.BaseState import BaseState
import pygame, sys, random
from src.Dependencies import *
from src.constants import *
from src.entity_defs import *

from src.entity_defs import EntityConf
from src.Player import Player

from src.states.entity.player.PlayerWalkState import PlayerWalkState
from src.states.entity.player.PlayerIdleState import PlayerIdleState
from src.states.entity.player.PlayerAttackState import PlayerAttackState
from src.StateMachine import StateMachine

from src.world.Dungeon import Dungeon

class MapState(BaseState):
    def __init__(self, state_machine):
        super(MapState, self).__init__(state_machine)

    def button(self, screen, position, text):
        font = pygame.font.Font(None, 50)
        text_render = font.render(text, 1, (255, 255, 255))
        x, y, w , h = text_render.get_rect(center=position)  # change this line to center the text
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), (x + w , y), 5)
        pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
        rect = pygame.Rect(x, y, w, h)
        return rect, screen.blit(text_render, (x, y))

    def Enter(self, params):
        entity_conf = ENTITY_DEFS['player']
        self.player = Player(entity_conf)
        self.dungeon = Dungeon(self.player)

        self.player.state_machine = StateMachine(pygame.display.get_surface())
        self.player.state_machine.SetStates({
            'walk': PlayerWalkState(self.player, self.dungeon),
            'idle': PlayerIdleState(self.player)
        })

        self.player.ChangeState('idle')

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            for event in events:
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:  # Left mouse button.
                       if self.my_button_rectangle.collidepoint(pygame.mouse.get_pos()):  # Check if mouse is over the button.
                           print("Button clicked!")
                           self.player.state_machine.current.roll_dice()  # Let's player roll the dice with a button click
                           self.player.button_pressed = True  # Flag that the button has been pressed

        self.dungeon.update(dt, events)

        if self.player.health == 0:
            self.state_machine.Change('game_over')

        #temp
        #self.room.update(dt, events)
    def render(self, screen):
        #dungen render
        self.dungeon.render(screen)

        health_left = self.player.health

        for i in range(3):
            if health_left > 1:
                heart_frame = 2
            elif health_left ==1:
                heart_frame = 1
            else:
                heart_frame = 0

            screen.blit(gHeart_image_list[heart_frame], (i * (TILE_SIZE+3), 6))
            health_left -=2

        self.my_button_rectangle, self.my_button_draw = self.button(screen, (WIDTH/2, HEIGHT-26), 'Roll Dice')

        screen.blit(gDice_image_list[0], (1000, 6))
        #temp
        #self.room.render(screen)


    def Exit(self):
        pass

