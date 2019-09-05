# Ctrl + SHift + P, then select interpreter
# choose interpreter that works

import pygame
from hero import Hero
from fleet import Fleet


# game settings
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3
#Colors
BLACK = 0, 0, 0,
WHITE = 255, 255, 255
# Game border
GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH

# Media files
pygame.init()
player_image = pygame.image.load('media/si-player.gif')
bullet_image = pygame.image.load('media/si-bullet.gif')
enemy_image = pygame.image.load('media/si-enemy.gif')
laser_sound = pygame.mixer.Sound('media/si-laser.wav')
explosion_sound = pygame.mixer.Sound('media/si-explode.wav')


clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score_font = pygame.font.SysFont('Arial', 22, True)
title_font = pygame.font.SysFont('Arial', 26, True)
pygame.display.set_caption('SPACE INVADERS!')


def handle_events():#this method does not belong to a class    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hero.is_alive = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_right()
            elif event.key == pygame.K_SPACE:
                laser_sound.play()
                hero.shoot(bullet_image)
            elif event.key == pygame.K_p:
                pause_game()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.set_direction_none()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_none()

def show_background():
    game_display.blit(game_display, (0, 0))
    game_display.fill((0, 0, 255))
    pygame.draw.rect(game_display, (4, 40, 70), \
            (GAME_SIDE_MARGIN, GAME_TOP_MARGIN, \
            WINDOW_WIDTH - GAME_SIDE_MARGIN * 2, \
            WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))
    pygame.draw.rect(game_display, (BLACK), \
            (GAME_LEFT_WALL, GAME_TOP_WALL, \
            WINDOW_WIDTH - GAME_LEFT_WALL - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH,\
            WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))

def pause_game():
    game_is_paused = True
    while game_is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_paused = False
                hero.is_alive = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_is_paused = False
        clock.tick(30)

 

hero = Hero(player_image, 200, GAME_BOTTOM_WALL - player_image.get_height())

fleet = Fleet(10, 7, 4, enemy_image, GAME_LEFT_WALL + 1, GAME_TOP_WALL + 1)

fleet.show(game_display)

#main game loop
 
while hero.is_alive:

    handle_events()

    fleet.handle_wall_collision(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    hero.handle_wall_collision_for_bullets(GAME_TOP_WALL)

    for bullet in hero.bullets_fired:
        for ship in fleet.ships:
            if bullet.has_collided_with(ship):
                explosion_sound.play()
                bullet.is_alive = False
                ship.is_alive = False

    fleet.remove_dead_ships()
    
    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    fleet.move_over()
    hero.move_all_bullets()

    show_background()      
    hero.show(game_display)
    fleet.show(game_display)
    hero.show_all_bullets(game_display)
    

    

    #score_text = score_font.render(str(snake.score), False, (255, 255, 255))
    #game_display.blit(score_text, (0, 0))  
    

    pygame.display.update()

    clock.tick(30)

pygame.quit()