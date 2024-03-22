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

    class Crazy():
        def __init__(self,screen):
            self.screen = screen

            self.x = ( 170 )
            self.x2 = ( 440 )

            self.y = ( 45 )

            self.crazy_image = pygame.image.load("assets/chess player crazy.png")
            self.crazy_image = pygame.transform.scale(self.crazy_image, (200, 100))
        def draw_crazy(self):
            self.screen.blit(self.crazy_image,(self.x,self.y))
            self.screen.blit(self.crazy_image,(self.x2,self.y))

    class Queen():
        def __init__(self,screen):
            self.screen = screen

            self.x = ( 345 )

            self.y = ( 40 )

            self.queen_image = pygame.image.load("assets/chess player queen.png")
            self.queen_image = pygame.transform.scale(self.queen_image,(210,110))
        def draw_queen(self):
            self.screen.blit(self.queen_image,(self.x,self.y))

    class King():
        def __init__(self,screen):
            self.screen = screen

            self.x = ( 250 )

            self.y = ( 30 )

            self.king_image = pygame.image.load("assets/chess player king.png")
            self.king_image = pygame.transform.scale(self.king_image,(210,110))
        def draw_king(self):
            self.screen.blit(self.king_image,(self.x,self.y))

class Player2():

    class Pions():
        def __init__(self,screen):
            self.screen = screen
            self.x = ( -45 )
            self.x2 = (45)
            self.x3 = (135)
            self.x4 = (225)
            self.x5 = (315)
            self.x6 = (405)
            self.x7 = (495)
            self.x8 = (585)

            self.y = ( 580 )

            self.pions2_image = pygame.image.load("assets/chess player pions.png").convert_alpha()
            self.pions2_image = pygame.transform.scale(self.pions2_image, (250, 125))
        def draw_pions2(self):
            self.screen.blit(self.pions2_image,(self.x,self.y))
            self.screen.blit(self.pions2_image, (self.x2, self.y))
            self.screen.blit(self.pions2_image, (self.x3, self.y))
            self.screen.blit(self.pions2_image, (self.x4, self.y))
            self.screen.blit(self.pions2_image, (self.x5, self.y))
            self.screen.blit(self.pions2_image, (self.x6, self.y))
            self.screen.blit(self.pions2_image, (self.x7, self.y))
            self.screen.blit(self.pions2_image, (self.x8, self.y))








