class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        self.bullets_allowed = 3