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
        
        self.GAMEBOARD = FullBoard(self.board_pics)
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
                            self.player_white.pieces[tile_index].move(tile)
                            
                        elif rank_index == 4:
                            self.player_white.pieces[tile_index+5].move(tile)
                            
                    elif board_index == 1:
                        if rank_index == 3:
                            self.player_white.pieces[tile_index+10].move(tile)
                            
                        if rank_index == 4:
                            self.player_white.pieces[tile_index+15].move(tile)
                            
                    elif board_index == 3:
                        if rank_index == 0:
                            self.player_black.pieces[tile_index].move(tile)
                            
                        if rank_index == 1:
                            self.player_black.pieces[tile_index+5].move(tile)
                            
                    elif board_index == 4:
                        if rank_index == 0:
                            self.player_black.pieces[tile_index+10].move(tile)
                            
                        if rank_index == 1:
                            self.player_black.pieces[tile_index+15].move(tile)
                            
                    tile_index += 1
                
                rank_index += 1
                
            board_index += 1
        
    def run(self):
        self.setBaseImage()
        #TODO: change selected tile to selected piece
        selectedPiece = None
        hintTiles = []
        players = [self.player_white, self.player_black]
        activePlayer = self.player_white
        nonActivePlayer = self.player_black
        while True:
           
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()
                    if selectedPiece is None:
                        for player in players:
                            for piece in player.pieces:
                            
                                if piece.tile.X_coordinate <= mouse_position[0] and piece.tile.X_coordinate + 40 > mouse_position[0]:
                                    if piece.tile.Y_coordinate <= mouse_position[1] and piece.tile.Y_coordinate + 40 > mouse_position[1]:
                                    
                                        if selectedPiece is None:
                                            selectedPiece = piece
                                        
                                        elif piece == selectedPiece:
                                            selectedPiece = None
                                            hintTiles = []
                                   
                                            
                                        else:
                                            selectedPiece = piece
                    else:
                        for board in self.GAMEBOARD:
                            for rank in board:
                                for tile in rank:
                                    if tile.X_coordinate <= mouse_position[0] and tile.X_coordinate + 40 > mouse_position[0]:
                                        if tile.Y_coordinate <= mouse_position[1] and tile.Y_coordinate + 40 > mouse_position[1]:
                                            
                                            if tile == selectedPiece.tile:
                                                selectedPiece = None
                                                hintTiles = []
                                                
                                            elif selectedPiece is not None and selectedPiece in activePlayer.pieces:
                                                if selectedPiece.can_move(tile):
                                                    selectedPiece.move(tile)
                                                selectedPiece = None
                                                hintTiles = []
                                                tempPlayer = activePlayer
                                                activePlayer = nonActivePlayer
                                                nonActivePlayer = tempPlayer
                                                tempPlayer = None
                                            
                                                
                                            else:
                                                continue
                                            
                                        
            #Draw frame
            for board in self.GAMEBOARD:
                self.DISPLAY.blit(board.image, board.pos)
                
                
            if selectedPiece is not None:
                pygame.draw.rect(self.DISPLAY, (255, 0, 0), (selectedPiece.tile.X_coordinate, selectedPiece.tile.Y_coordinate, 40, 40), 0)
                for board in self.GAMEBOARD:
                    for rank in board:
                        for tile in rank:
                            if selectedPiece.can_move(tile):
                                hintTiles.append(tile)
                
            for hint_tile in hintTiles:
                pygame.draw.rect(self.DISPLAY, (255, 255, 0), (hint_tile.X_coordinate, hint_tile.Y_coordinate, 40, 40), 0)
            
            for piece in self.player_white.pieces:
                self.DISPLAY.blit(piece.image, (piece.tile.pos))
                
            for piece in self.player_black.pieces:
                self.DISPLAY.blit(piece.image, (piece.tile.pos))
            
            pygame.display.update()
            self.clock.tick(40)

    def populatePieces(self):
        self.white_pieces = [Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0),
                             Rook_White(self.sprite.rook_w, 0), Knight_White(self.sprite.knight_w, 0), King_White(self.sprite.king_w, 0), Knight_White(self.sprite.knight_w, 0), Rook_White(self.sprite.rook_w, 0),
                             Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0), Pawn_White(self.sprite.pawn_w, 0),
                             Thief_White(self.sprite.thief_w, 0),Bishop_White(self.sprite.bishop_w, 0), Queen_White(self.sprite.queen_w, 0), Thief_White(self.sprite.thief_w, 0), Bishop_White(self.sprite.bishop_w, 0)
                             ]
                      
        self.black_pieces = [
                             Bishop_Black(self.sprite.bishop_b, 1), Thief_Black(self.sprite.thief_b, 1), Queen_Black(self.sprite.queen_b, 1), Bishop_Black(self.sprite.bishop_b, 1), Thief_Black(self.sprite.thief_b, 1),
                             Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1),
                             Rook_Black(self.sprite.rook_b, 1), Knight_Black(self.sprite.knight_b, 1), King_Black(self.sprite.king_b, 1), Knight_Black(self.sprite.knight_b, 1), Rook_Black(self.sprite.rook_b, 1),
                             Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1), Pawn_Black(self.sprite.pawn_b, 1)
                              ]

    
    def setBaseImage(self):
        self.DISPLAY.blit(self.background, (0,0))           

    
    def setPictures(self):
        self.background = pygame.image.load("images\\Raumschach_bg.png")
        self.board_black = pygame.image.load("images\\Raumschach_board_black.png")
        self.board_white = pygame.image.load("images\\Raumschach_board_white.png")
     

        
        self.board_A = self.board_black
        self.board_B = self.board_white
        self.board_C = self.board_black
        self.board_D = self.board_white
        self.board_E = self.board_black
        self.board_pics = [self.board_A,
                           self.board_B,
                           self.board_C,
                           self.board_D,
                           self.board_E]


if __name__ == "__main__":
    myGame = Game()
    myGame.run()
