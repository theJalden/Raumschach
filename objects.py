import pygame
from pygame.locals import *
import math

class Sprite():
    def __init__(self):
        self.pawn_w = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\pawn_w.png")
        self.pawn_b = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\pawn_b.png")
        self.knight_w = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\knight_w.png")
        self.knight_b = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\knight_b.png")
        self.bishop_w = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\bishop_w.png")
        self.bishop_b = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\bishop_b.png")
        self.thief_w = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\thief_w.png")
        self.thief_b = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\thief_b.png")
        self.king_w = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\king_w.png")
        self.king_b = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\king_b.png")
        self.queen_w = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\queen_w.png")
        self.queen_b = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\queen_b.png")
        self.rook_w = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\rook_w.png")
        self.rook_b = pygame.image.load("C:\\Users\\Joseph\\Documents\\Raumschach\\images\\rook_b.png")


class Piece():
    def __init__(self, image):
        self.image = image
        self.X = 0
        self.Y = 0
        self.Z = 0
    
    def move(self, tile1, tile2):
        tile2.setPiece(self)
        tile1.removePiece()
    
    def moveForward(self, n):
        self.Y += n
        if self.Y > 4:
            self.Y = 4
        elif self.Y < 0:
            self.Y = 0
            
    def moveUp(self, n):
        self.Z += n        
        if self.Z > 4:
            self.Z = 4
        elif self.Z < 0:
            self.Z = 0
            
    def moveRight(self, n):
        self.X += n        
        if self.X > 4:
            self.X = 4
        elif self.X < 0:
            self.X = 0
            
    def _setColor(self):
        self.color = None
        
    def setTile(self, tile):
        self.tile = tile

class Pawn_White(Piece):
    def can_move(self, tile):
        if tile.X == self.X:
            if tile.Y == self.Y - 1 and tile.Z == self.Z:
                return True
                
            if tile.Y == self.Y and tile.Z == self.Z+1:
                return True
        else:
            return False
            
    def _setColor(self):
        self.color = "White"

class Rook_White(Piece):
    def can_move(self, tile):
            if tile.X == self.X and tile.Y == self.Y and tile.Z != self.Z:
                return True
                
            elif tile.X == self.X and tile.Y != self.Y and tile.Z == self.Z:
                return True
                
            elif tile.X != self.X and tile.Y == self.Y and tile.Z == self.Z:
                return True
                
            else:
                return False
    
    def _setColor(self):
        self.color = "White"

class Bishop_White(Piece):
    def can_move(self, tile):
    
        if tile.X != self.X or tile.Y != self.Y or tile.Z != self.Z:
            if tile.Z == self.Z:
                if math.fabs(tile.Y-self.Y) == math.fabs(tile.X-self.X):
                    return True    
                    
            elif tile.X == self.X:
                if math.fabs(tile.Y-self.Y) == math.fabs(tile.Z-self.Z):
                    return True
                    
            elif tile.Y == self.Y:
                if math.fabs(tile.X-self.X) == math.fabs(tile.Z-self.Z):
                    return True
                    
            else:
                return False
                
        else:
            return False
            
    def _setColor(self):
        self.color = "White"
    
class Thief_White(Piece):
    def can_move(self, tile):
    
            if math.fabs(tile.Y-self.Y) == math.fabs(tile.X-self.X) and math.fabs(tile.X-self.X) == math.fabs(tile.Z - self.Z):
                return True
                
            else:
                return False
                
    def _setColor(self):
        self.color = "White"

class Queen_White(Piece):
    def can_move(self, tile):
    
        if tile.X != self.X or tile.Y != self.Y or tile.Z != self.Z:
        
            if tile.Z == self.Z:
                if math.fabs(tile.Y-self.Y) == math.fabs(tile.X-self.X):
                    return True
                    
                elif tile.X == self.X or tile.Y == self.Y:
                    return True
                    
            elif tile.X == self.X:
                if math.fabs(tile.Y-self.Y) == math.fabs(tile.Z-self.Z):
                    return True
                    
                elif tile.Y == self.Y or tile.Y == self.Y:
                    return True
                    
            elif tile.Y == self.Y:
                if math.fabs(tile.X-self.X) == math.fabs(tile.Z-self.Z):
                    return True
                    
                if tile.X == self.X or tile.Z == self.Z:
                    return True
                
            elif math.fabs(tile.Y-self.Y) == math.fabs(tile.X-self.X) and math.fabs(tile.X-self.X) == math.fabs(tile.Z - self.Z):
                return True
                
            else:
                return False
                
        else: return False
        
    def _setColor(self):
        self.color = "White"
        
class King_White(Piece):
    def can_move(self, tile):
        if math.fabs(tile.X - self.X) <= 1 and math.fabs(tile.Y - self.Y) <= 1 and math.fabs(tile.Z - self.Z) <= 1:
            return True
            
        else:
            return False
            
    def _setColor(self):
        self.color = "White"
        
class Knight_White(Piece):
    def can_move(self, tile):
        if tile.Z == self.Z:
            if math.fabs(tile.X-self.X) == 2 and math.fabs(tile.Y-self.Y) == 1:
                return True
                
            elif math.fabs(tile.X-self.X) == 1 and math.fabs(tile.Y-self.Y) == 2:
                return True
                
            else:
                return False
 
        elif tile.X == self.X:
            if math.fabs(tile.Z-self.Z) == 2 and math.fabs(tile.Y-self.Y) == 1:
                return True
                
            elif math.fabs(tile.Z-self.Z) == 1 and math.fabs(tile.Y-self.Y) == 2:
                return True
                
            else:
                return False      
        
        elif tile.Y == self.Y:
            if math.fabs(tile.Z-self.Z) == 2 and math.fabs(tile.X-self.X) == 1:
                return True
                
            elif math.fabs(tile.Z-self.Z) == 1 and math.fabs(tile.X-self.X) == 2:
                return True
                
            else:
                return False
                
        else:
            return False
            
    def _setColor(self):
        self.color = "White"

class Pawn_Black(Piece):
    def can_move(self, tile):
        if tile.X == self.X:
            if tile.Y == self.Y + 1 and tile.Z == self.Z:
                return True
                
            if tile.Y == self.Y and tile.Z == self.Z-1:
                return True
        else:
            return False
            
    def _setColor(self):
        self.color = "Black"

class Rook_Black(Rook_White):
    def _setColor(self):
        self.color = "Black"

class Bishop_Black(Bishop_White):
    def _setColor(self):
        self.color = "Black"

class Thief_Black(Thief_White):
    def _setColor(self):
        self.color = "Black"

class Queen_Black(Queen_White):
    def _setColor(self):
        self.color = "Black"

class King_Black(King_White):
    def _setColor(self):
        self.color = "Black"

class Knight_Black(Knight_White):
    def _setColor(self):
        self.color = "Black"


class Tile():
    def __init__(self, rank, file, board):
        self.piece = None
        self.active = False
        self.selected = False
        self.X = rank
        self.Y = file
        self.Z = board
        
        self.X_coordinate = (240*(4-board) + 60) + 40*file
        self.Y_coordinate = (100*(4-board) + 80) + 40*rank
        
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
        
    def select(self):
        self.selected = True
        
    def deselect(self):
        self.selected = False
        
    def setPiece(self, piece):
        self.piece = piece
        piece.setTile = self
        piece.X = self.X
        piece.Y = self.Y
        piece.Z = self.Z
        
    def removePiece(self):
        self.piece = None

class Board(list):
    def __init__(self, number):
        for n in range(5):
            self.append([Tile(i, n, number) for i in range(5)])
            
class FullBoard(list):
    def __init__(self):
        for board in range(5):
            self.append(Board(board))