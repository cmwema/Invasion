class GameStats:
    """Track statistics for the alien invasion"""

    def __init__(self, ai_settings):
        """initialize the stats"""

        self.ai_settings = ai_settings
        self.high_score = 0
        self.reset_stats()
        self.level = 1

    def reset_stats(self):
        """initialize the variable statistics of the game"""

        self.ships_left = self.ai_settings.ship_limit
        self.game_active = False
        self.score = 0