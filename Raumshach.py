# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Joseph"
__date__ ="$Feb 1, 2014 2:21:32 PM$"

import sys

import pygame
from pygame.locals import *
import math

from objects import *

            

class Game():
    def __init__(self):
        pygame.init()
        self.DISPLAY = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.setPictures()
        self.sprite = Sprite()
        self.pieces = self.populatePieces()
        
        self.player_white = Player("white", self.white_pieces)
        self.player_black = Player("black", self.black_pieces)
        self.player_white.toggle_turn()
        
        self.GAMEBOARD = FullBoard()
        self.resetPieces()
        
    def resetPieces(self):
    
        board_index = 0
        for board in self.GAMEBOARD:
            rank_index = 0
            
            for rank in board:
                tile_index = 0
                
                for tile in rank:
                
                    if board_index == 0:
                        if rank_index == 3:
                            tile.setPiece(self.white_pieces[tile_index])
                            
                        elif rank_index == 4:
                            tile.setPiece(self.white_pieces[tile_index+5])
                            
                    elif board_index == 1:
                        if rank_index == 3:
                            tile.setPiece(self.white_pieces[tile_index+10])
                            
                        if rank_index == 4:
                            tile.setPiece(self.white_pieces[tile_index+15])
                            
                    elif board_index == 3:
                        if rank_index == 0:
                            tile.setPiece(self.black_pieces[tile_index])
                            
                        if rank_index == 1:
                            tile.setPiece(self.black_pieces[tile_index+5])
                            
                    elif board_index == 4:
                        if rank_index == 0:
                            tile.setPiece(self.black_pieces[tile_index+10])
                            
                        if rank_index == 1:
                            tile.setPiece(self.black_pieces[tile_index+15])
                            
                    tile_index += 1
                
                rank_index += 1
                
            board_index += 1
        
    def run(self):
        self.setBaseImage()
        selectedTiles = []
        activePlayer = self.player_white
        nonActivePlayer = self.player_black
        while True:
           
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()
                    for board in self.GAMEBOARD:
                        for rank in board:
                            for tile in rank:
                                if tile.X_coordinate <= mouse_position[0] and tile.X_coordinate + 40 > mouse_position[0]:
                                    if tile.Y_coordinate <= mouse_position[1] and tile.Y_coordinate + 40 > mouse_position[1]:
                                        tile.select()
                                        if selectedTiles == []:
                                            selectedTiles = [tile]
                                        
                                        elif tile in selectedTiles:
                                            selectedTiles = []
                                            
                                        elif selectedTiles[0].piece is not None and selectedTiles[0].piece in activePlayer.pieces:
                                            if selectedTiles[0].piece.can_move(tile):
                                                selectedTiles[0].piece.move(selectedTiles[0], tile)
                                            selectedTiles = []
                                            tempPlayer = activePlayer
                                            activePlayer = nonActivePlayer
                                            nonActivePlayer = tempPlayer
                                            tempPlayer = None
                                        
                                            
                                        else:
                                            selectedTiles = [tile]
                                            
                                        
            
            self.drawBoards()
            for tile in selectedTiles:
                pygame.draw.rect(self.DISPLAY, (255, 0, 0), (tile.X_coordinate, tile.Y_coordinate, 40, 40), 0)
            self.drawPieces()
                
            
            pygame.display.update()
            self.clock.tick(40)

    def populatePieces(self):
        self.white_pieces = [Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w),
                             Rook_White(self.sprite.rook_w), Knight_White(self.sprite.knight_w), King_White(self.sprite.king_w), Knight_White(self.sprite.knight_w), Rook_White(self.sprite.rook_w),
                             Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w), Pawn_White(self.sprite.pawn_w),
                             Thief_White(self.sprite.thief_w),Bishop_White(self.sprite.bishop_w), Queen_White(self.sprite.queen_w), Thief_White(self.sprite.thief_w), Bishop_White(self.sprite.bishop_w)
                             ]
                      
        self.black_pieces = [
                             Bishop_Black(self.sprite.bishop_b), Thief_Black(self.sprite.thief_b), Queen_Black(self.sprite.queen_b), Bishop_Black(self.sprite.bishop_b), Thief_Black(self.sprite.thief_b),
                             Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b),
                             Rook_Black(self.sprite.rook_b), Knight_Black(self.sprite.knight_b), King_Black(self.sprite.king_b), Knight_Black(self.sprite.knight_b), Rook_Black(self.sprite.rook_b),
                             Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b), Pawn_Black(self.sprite.pawn_b)
                              ]

    def drawBoards(self):
        self.DISPLAY.blit(self.board_A, (60, 80))
        self.DISPLAY.blit(self.board_B, (300,180))
        self.DISPLAY.blit(self.board_C, (540,280))
        self.DISPLAY.blit(self.board_D, (780,380))
        self.DISPLAY.blit(self.board_E, (1020,480))

    def drawPieces(self):
    
        for board in self.GAMEBOARD:
            for rank in board:
                for tile in rank:
                    if tile.piece is not None:
                        self.DISPLAY.blit(tile.piece.image, (tile.X_coordinate, tile.Y_coordinate))
    

    
    def setBaseImage(self):
        self.DISPLAY.blit(self.background, (0,0))
        self.DISPLAY.blit(self.board_A, (60, 80))
        self.DISPLAY.blit(self.board_B, (300,180))
        self.DISPLAY.blit(self.board_C, (540,280))
        self.DISPLAY.blit(self.board_D, (780,380))
        self.DISPLAY.blit(self.board_E, (1020,480))            

    
    def setPictures(self):
        self.background = pygame.image.load("images\\Raumschach_bg.png")
        self.board_black = pygame.image.load("images\\Raumschach_board_black.png")
        self.board_white = pygame.image.load("images\\Raumschach_board_white.png")
     


        self.board_A = self.board_black
        self.board_B = self.board_white
        self.board_C = self.board_black
        self.board_D = self.board_white
        self.board_E = self.board_black



if __name__ == "__main__":
    myGame = Game()
    myGame.run()
