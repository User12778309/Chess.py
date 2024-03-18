from python_class.game import Game
import pygame
import sys

ligne = ( 8 )
colonne = ( 8 )
cellule = ( 100 )

pygame.init()

screen = pygame.display.set_mode((ligne * cellule,colonne * cellule))
pygame.display.set_caption("Chess")

FPS = pygame.time.Clock()

background_image = pygame.image.load("assets/chess board.png")
background = pygame.transform.scale(background_image,(900,900))

game = Game(screen)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background,(-50,-50))

    game.draw()

    pygame.display.flip()
    FPS.tick(60
             )