#!/usr/bin/python3
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #1.initialize pygame, settings and screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make the play button
    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game statistics
    stats = GameStats(ai_settings)
    
    sb = Scoreboard(ai_settings=ai_settings, screen=screen, stats=stats)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings=ai_settings, screen=screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    #make an alien 
    alien = Alien(ai_settings=ai_settings, screen=screen)

    #2.start mainloop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            gf.check_events(ai_settings=ai_settings, screen=screen, stats=stats, sb=sb, play_button=play_button, ship=ship, aliens=aliens, bullets=bullets)
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
