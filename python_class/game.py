from python_class.player import Player
import pygame

class Game():

    def __init__(self,screen):
        self.pions = Player.Pions(screen)
        self.tower = Player.Tower(screen)
        self.horse = Player.Horse(screen)
        self.crazy = Player.Crazy(screen)
        self.queen = Player.Queen(screen)
    def draw(self):
        self.pions.draw_pions()
        self.tower.draw_tower()
        self.horse.draw_horse()
        self.crazy.draw_crazy()
        self.queen.draw_queen()


