from python_class.player import Player
import pygame

class Game():

    def __init__(self,screen):
        self.pions = Player.Pions(screen)
        self.tower = Player.Tower(screen)
    def draw(self):
        self.pions.draw_pions()
        self.tower.draw_tower()
