class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230,200,250)

#ship settings#
        self.ship_speed = 1.5
#bullet settings#
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
#alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        #1 is right, -1 is left#
        