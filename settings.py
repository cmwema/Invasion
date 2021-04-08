class Settings:
    """A class to store all the game's settings"""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        
        self.bg_color = (223, 223, 223)

        #ship settings
        self.ship_speeed_factor = 10
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 4
        self.bullet_height = 13
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        
        #alien settings
        self.fleet_drop_speed = 1
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Scoring
        self.alien_points = 50
        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 9
        self.bullet_speed_factor = 9
        self.alien_speed_factor = 0.5

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)