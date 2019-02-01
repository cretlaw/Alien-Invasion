import pygame


class Ship():
    def __init__(self, ai_setttings, screen):
        '''Initialize the ship and starting position'''
        self.screen = screen
        self.ai_setttings = ai_setttings

        # load the ship imnage and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new  ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on the movement flag.'''
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_setttings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setttings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center the ship on the screen'''
        self.center = self.screen_rect.centerx
