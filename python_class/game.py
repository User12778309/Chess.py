from python_class.player import Player
from python_class.player import Player2
import pygame

class Game():

    def __init__(self,screen):
        self.pions = Player.Pions(screen)
        self.tower = Player.Tower(screen)
        self.horse = Player.Horse(screen)
        self.crazy = Player.Crazy(screen)
        self.queen = Player.Queen(screen)
        self.king = Player.King(screen)

        self.pions2 =  Player2.Pions(screen)
        self.tower2 = Player2.Tower2(screen)
    def draw(self):
        self.pions.draw_pions()
        self.tower.draw_tower()
        self.horse.draw_horse()
        self.crazy.draw_crazy()
        self.queen.draw_queen()
        self.king.draw_king()

        self.pions2.draw_pions2()
        self.tower2.draw_tower2()


