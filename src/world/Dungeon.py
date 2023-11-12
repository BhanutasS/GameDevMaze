from src.world.Room import Room
from src.constants import *

class Dungeon:
    def __init__(self, player):
        self.player = player

        self.rooms = {}

        self.current_room = Room(self.player)

        self.next_room = None

        self.camera_x = 0
        self.camera_y = 0
        self.shifting = False



    def BeginShifting(self, shift_x, shift_y):
        self.shifting = True
        self.next_room = Room(self.player)

        #DOOR HANDLE

        player_x, player_y = self.player.x, self.player.y

        if shift_x > 0 :
            player_x = WIDTH + (MAP_RENDER_OFFSET_X + TILE_SIZE)
        elif shift_x <0:
            player_x = -WIDTH + (MAP_RENDER_OFFSET_X + (MAP_WIDTH * TILE_SIZE) - TILE_SIZE - self.player.width)
        elif shift_y >0:
            player_y = HEIGHT + (MAP_RENDER_OFFSET_Y+self.player.height/2)
        else:
            player_y = -HEIGHT + MAP_RENDER_OFFSET_Y + (MAP_HEIGHT * TILE_SIZE) - TILE_SIZE - self.player.height

        self.FinishShifting()

        #continue
        if shift_x < 0:
            self.player.ChangeCoord(x=MAP_RENDER_OFFSET_X + (MAP_WIDTH * TILE_SIZE) - TILE_SIZE - self.player.width)
            self.player.direction = 'left'
        elif shift_x > 0:
            self.player.ChangeCoord(x=MAP_RENDER_OFFSET_X+TILE_SIZE)
            self.player.direction = 'right'
        elif shift_y < 0:
            self.player.ChangeCoord(y=MAP_RENDER_OFFSET_Y + (MAP_HEIGHT * TILE_SIZE) - TILE_SIZE - self.player.height)
            self.player.direction = 'up'
        else:
            self.player.ChangeCoord(y=MAP_RENDER_OFFSET_Y + self.player.height / 2)

        #
        # -- close all doors in the current room
        # for k, doorway in pairs(self.currentRoom.doorways) do
        #     doorway.open = false
        # end
        #
        # gSounds['door']:play()

    def FinishShifting(self):
        self.camera_x = 0
        self.camera_y = 0
        self.shifting = False

        self.current_room = self.next_room
        self.next_room = None

        self.current_room.adjacent_offset_x = 0
        self.current_room.adjacent_offset_y = 0


    def update(self, dt, events):
        if not self.shifting:
            self.current_room.update(dt, events)
        else:
            #animation during shift not so sure I will do shifting
            self.player.curr_animation.update()


    def render(self, screen):
        if self.shifting:
            temp_surf = screen.copy
            screen.fill((0, 0, 0))
            screen.blit(temp_surf, (-math.floor(self.camera_x), -math.floor(self.camera_y)))

        self.current_room.render(screen)

        if self.next_room:
            self.next_room.render(screen)