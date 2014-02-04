import pygame
from pygame.locals import *
import math

class Sprite():
    def __init__(self):
        self.pawn_w = pygame.image.load("images\\pawn_w.png")
        self.pawn_b = pygame.image.load("images\\pawn_b.png")
        self.knight_w = pygame.image.load("images\\knight_w.png")
        self.knight_b = pygame.image.load("images\\knight_b.png")
        self.bishop_w = pygame.image.load("images\\bishop_w.png")
        self.bishop_b = pygame.image.load("images\\bishop_b.png")
        self.thief_w = pygame.image.load("images\\thief_w.png")
        self.thief_b = pygame.image.load("images\\thief_b.png")
        self.king_w = pygame.image.load("images\\king_w.png")
        self.king_b = pygame.image.load("images\\king_b.png")
        self.queen_w = pygame.image.load("images\\queen_w.png")
        self.queen_b = pygame.image.load("images\\queen_b.png")
        self.rook_w = pygame.image.load("images\\rook_w.png")
        self.rook_b = pygame.image.load("images\\rook_b.png")

class Player():
    def __init__(self, color, pieces):
        self.color = color
        self.pieces = pieces
        self.capturedPieces = []
        self.is_turn = False
        
    def toggle_turn(self):
        self.is_turn = not self.is_turn
        
        
class Piece():
    def __init__(self, image, color):  #color: 0 = white, 1 = black
        self.image = image
        #TODO, remove self posistion, rely on tile coordinates
        self.color = color
    
    def move(self, tile):
        self.tile = tile


class Pawn_White(Piece):
    def can_move(self, tile):
        if tile.X == self.tile.X:
            if tile.Y == self.tile.Y - 1 and tile.Z == self.tile.Z:
                return True
                
            if tile.Y == self.tile.Y and tile.Z == self.tile.Z+1:
                return True
        else:
            return False


class Rook_White(Piece):
    def can_move(self, tile):
        
        if tile.X == self.tile.X and tile.Y == self.tile.Y and tile.Z != self.tile.Z:
            return True
            
        elif tile.X == self.tile.X and tile.Y != self.tile.Y and tile.Z == self.tile.Z:
            return True
            
        elif tile.X != self.tile.X and tile.Y == self.tile.Y and tile.Z == self.tile.Z:
            return True
            
        else:
            return False

class Bishop_White(Piece):
    def can_move(self, tile):
    
        if tile.X != self.tile.X or tile.Y != self.tile.Y or tile.Z != self.tile.Z:
            if tile.Z == self.tile.Z:
                if math.fabs(tile.Y-self.tile.Y) == math.fabs(tile.X-self.tile.X):
                    return True    
                    
            elif tile.X == self.tile.X:
                if math.fabs(tile.Y-self.tile.Y) == math.fabs(tile.Z-self.tile.Z):
                    return True
                    
            elif tile.Y == self.tile.Y:
                if math.fabs(tile.X-self.tile.X) == math.fabs(tile.Z-self.tile.Z):
                    return True
                    
            else:
                return False
                
        else:
            return False

    
class Thief_White(Piece):
    def can_move(self, tile):
        if tile.X != self.tile.X or tile.Y != self.tile.Y or tile.Z != self.tile.Z:
            if math.fabs(tile.Y-self.tile.Y) == math.fabs(tile.X-self.tile.X) and math.fabs(tile.X-self.tile.X) == math.fabs(tile.Z - self.tile.Z):
                return True
                
            else:
                return False


class Queen_White(Piece):
    def can_move(self, tile):
    
        if tile.X != self.tile.X or tile.Y != self.tile.Y or tile.Z != self.tile.Z:
        
            if tile.Z == self.tile.Z:
                if math.fabs(tile.Y-self.tile.Y) == math.fabs(tile.X-self.tile.X):
                    return True
                    
                elif tile.X == self.tile.X or tile.Y == self.tile.Y:
                    return True
                    
            elif tile.X == self.tile.X:
                if math.fabs(tile.Y-self.tile.Y) == math.fabs(tile.Z-self.tile.Z):
                    return True
                    
                elif tile.Y == self.tile.Y or tile.Y == self.tile.Y:
                    return True
                    
            elif tile.Y == self.tile.Y:
                if math.fabs(tile.X-self.tile.X) == math.fabs(tile.Z-self.tile.Z):
                    return True
                    
                if tile.X == self.tile.X or tile.Z == self.tile.Z:
                    return True
                
            elif math.fabs(tile.Y-self.tile.Y) == math.fabs(tile.X-self.tile.X) and math.fabs(tile.X-self.tile.X) == math.fabs(tile.Z - self.tile.Z):
                return True
                
            else:
                return False
                
        else: return False

        
class King_White(Piece):
    def can_move(self, tile):
        if math.fabs(tile.X - self.tile.X) <= 1 and math.fabs(tile.Y - self.tile.Y) <= 1 and math.fabs(tile.Z - self.tile.Z) <= 1:
            return True
            
        else:
            return False
            
        
class Knight_White(Piece):
    def can_move(self, tile):
        if tile.Z == self.tile.Z:
            if math.fabs(tile.X-self.tile.X) == 2 and math.fabs(tile.Y-self.tile.Y) == 1:
                return True
                
            elif math.fabs(tile.X-self.tile.X) == 1 and math.fabs(tile.Y-self.tile.Y) == 2:
                return True
                
            else:
                return False
 
        elif tile.X == self.tile.X:
            if math.fabs(tile.Z-self.tile.Z) == 2 and math.fabs(tile.Y-self.tile.Y) == 1:
                return True
                
            elif math.fabs(tile.Z-self.tile.Z) == 1 and math.fabs(tile.Y-self.tile.Y) == 2:
                return True
                
            else:
                return False      
        
        elif tile.Y == self.tile.Y:
            if math.fabs(tile.Z-self.tile.Z) == 2 and math.fabs(tile.X-self.tile.X) == 1:
                return True
                
            elif math.fabs(tile.Z-self.tile.Z) == 1 and math.fabs(tile.X-self.tile.X) == 2:
                return True
                
            else:
                return False
                
        else:
            return False


class Pawn_Black(Piece):
    def can_move(self, tile):
        if tile.X == self.tile.X:
            if tile.Y == self.tile.Y + 1 and tile.Z == self.tile.Z:
                return True
                
            if tile.Y == self.tile.Y and tile.Z == self.tile.Z-1:
                return True
        else:
            return False


class Rook_Black(Rook_White):
    pass

class Bishop_Black(Bishop_White):
    pass

class Thief_Black(Thief_White):
    pass

class Queen_Black(Queen_White):
    pass

class King_Black(King_White):
    pass

class Knight_Black(Knight_White):
    pass


class Tile():
    def __init__(self, rank, file, board):
        self.X = rank
        self.Y = file
        self.Z = board
        
        self.X_coordinate = (240*(4-board) + 60) + 40*file
        self.Y_coordinate = (100*(4-board) + 80) + 40*rank
        self.pos = (self.X_coordinate, self.Y_coordinate)

class Board(list):
    def __init__(self, number, image):
        for n in range(5):
            self.append([Tile(i, n, number) for i in range(5)])
        self.image = image
        self.pos = (240*number + 60, 100*number + 80 )
        
            
class FullBoard(list):
    def __init__(self, images):
        for board in range(5):
            self.append(Board(board, images[board]))