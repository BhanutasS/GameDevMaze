import pygame
import random

# Initialize Pygame
pygame.init()

win_height, win_width = 600, 600
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

snake_ladders = {4:14, 9:31, 17: 7, 20:38, 28:84, 40:59, 51:67, 54:34, 62:19, 64:60, 71:91, 87:24, 93:73, 95:75, 99:78}  # dictionary storing the snakes and ladders

player_pos = 1

def draw_board():
    # As a placeholder, draw a red rectangle to represent the board.
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(50, 50, 500, 500))
    # And a smaller green rectangle to represent the player piece.
    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(50, 50, 20, 20))

def roll_dice():
    return random.randint(1, 6)

def game():
    global player_pos
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # Add a keyboard event to roll the dice and move the player
                if event.key == pygame.K_SPACE:
                    dice = roll_dice()
                    player_pos += dice
                    if player_pos > 100:
                        player_pos -= dice
                    if player_pos in snake_ladders:
                        player_pos = snake_ladders[player_pos]

        win.fill((0, 0, 0))  # Clear the screen
        draw_board()
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    game()