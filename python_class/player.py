import pygame

class Player():

    class Pions():
        def __init__(self,screen):
            self.screen = screen
            self.x = ( -45 )
            self.x2 = ( 45 )
            self.x3 = ( 135 )
            self.x4 = ( 225 )
            self.x5 = ( 315 )
            self.x6 = ( 405 )
            self.x7 = ( 495 )
            self.x8 = ( 585 )

            self.y = ( 130 )

            self.pions_image = pygame.image.load("assets/chess player pions.png").convert_alpha()
            self.pions_image = pygame.transform.scale(self.pions_image,(250,125))
        def draw_pions(self):
            self.screen.blit(self.pions_image,(self.x,self.y))
            self.screen.blit(self.pions_image,(self.x2,self.y))
            self.screen.blit(self.pions_image, (self.x3, self.y))
            self.screen.blit(self.pions_image, (self.x4, self.y))
            self.screen.blit(self.pions_image, (self.x5, self.y))
            self.screen.blit(self.pions_image, (self.x6, self.y))
            self.screen.blit(self.pions_image, (self.x7, self.y))
            self.screen.blit(self.pions_image, (self.x8, self.y))


    class Tower():
        def __init__(self,screen):
            self.screen = screen
            self.x = ( -10 )
            self.x2 = ( 620 )

            self.y = ( 40 )

            self.tower_image = pygame.image.load("assets/chess player tour.png").convert_alpha()
            self.tower_image = pygame.transform.scale(self.tower_image,(200,100))
        def draw_tower(self):
            self.screen.blit(self.tower_image,(self.x,self.y))
            self.screen.blit(self.tower_image,(self.x2,self.y))

    class Horse():
        def __init__(self,screen):
            self.screen = screen
            self.x = ( 80 )
            self.x2 = ( 530 )

            self.y = ( 45 )

            self.horse_image = pygame.image.load("assets/chess player horse.png")
            self.horse_image = pygame.transform.scale(self.horse_image,(200,100))
        def draw_horse(self):
            self.screen.blit(self.horse_image,(self.x,self.y))
            self.screen.blit(self.horse_image, (self.x2, self.y))


