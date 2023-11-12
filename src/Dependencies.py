import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine

sprite_collection = SpriteManager().spriteCollection



gPlayer_animation_list = {"down": sprite_collection["character_walk_down"].animation,
                         "right": sprite_collection["character_walk_right"].animation,
                         "up": sprite_collection["character_walk_up"].animation,
                         "left": sprite_collection["character_walk_left"].animation,
                        "attack_down": sprite_collection["character_attack_down"].animation,
                        "attack_right": sprite_collection["character_attack_right"].animation,
                        "attack_up": sprite_collection["character_attack_up"].animation,
                        "attack_left": sprite_collection["character_attack_left"].animation
}

gSkeleton_animation_list = {"down": sprite_collection["skeleton_walk_down"].animation,
                         "right": sprite_collection["skeleton_walk_right"].animation,
                         "up": sprite_collection["skeleton_walk_up"].animation,
                         "left": sprite_collection["skeleton_walk_left"].animation,
}



# gPlayer_idle_image_list = {
#     "up": sprite_collection["character_up"].image, "down": sprite_collection["character_down"].image,
#     "right": sprite_collection["character_right"].image, "left": sprite_collection["character_left"].image,
# }

gHeart_image_list = [sprite_collection["heart_0"].image,sprite_collection["heart_2"].image,
                    sprite_collection["heart_4"].image]

gDice_image_list = [sprite_collection["dice_0"].image,sprite_collection["dice_1"].image,
                    sprite_collection["dice_2"].image,sprite_collection["dice_3"].image,
                    sprite_collection["dice_4"].image]

gRoom_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16)
gDoor_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16, colorkey=(13, 7, 17, 255))
gSwitch_image_list = Util.GenerateTiles("./graphics/switches.png", 16, 18)

gSounds = {
    'music': pygame.mixer.Sound('sounds/music.mp3'),
    'sword':  pygame.mixer.Sound('sounds/sword.wav'),
    'hit_enemy':  pygame.mixer.Sound('sounds/hit_enemy.wav'),
    'hit_player':  pygame.mixer.Sound('sounds/hit_player.wav'),
    'door':  pygame.mixer.Sound('sounds/door.wav')
}

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 192),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 140),

}

from src.states.game.MapState import MapState
from src.states.game.HomeState import HomeState
from src.states.game.LoserState import LoserState
from src.StateMachine import StateMachine




