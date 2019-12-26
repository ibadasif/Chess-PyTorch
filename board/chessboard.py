from pieces.nopiece import Nopiece
from board.tile import Tile
from pieces.bishop import Bishop
from pieces.king import King
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.knight import Knight

class Board:
    gameTiles = {}
    enPassPawn = None
    enPassPawnBehind = None
    currentPlayer = "White"

    def __init__(self):
        pass

    def calculateActivePieces(self, alliance):

        activeP = []
        for tile in range(len(self.gameTiles)):
            if not self.gameTiles[tile].pieceOnTile.toString() == "-":
                if self.gameTiles[tile].pieceOnTile.alliance == alliance:
                    activeP.append(self.gameTiles[tile].pieceOnTile)

        return activeP

    def calculateLegalMoves(self, pieces, board):
        allLegals = []
        for piece in pieces:
            pieceMoves = piece.calculateLegalMoves(board)
            for move in pieceMoves:
                allLegals.append([move, piece])
        return allLegals
    def createBoard(self):
        for x in range (64):
            self.gameTiles[x] = Tile(x,Nopiece())
        self.gameTiles[0] = Tile(0, Rook("Black", 0))
        self.gameTiles[1] = Tile(1, Knight("Black", 1))
        self.gameTiles[2] = Tile(2, Bishop("Black", 2))
        self.gameTiles[3] = Tile(3, Queen("Black", 3))
        self.gameTiles[4] = Tile(4, King("Black", 4))
        self.gameTiles[5] = Tile(5, Bishop("Black", 5))
        self.gameTiles[6] = Tile(6, Knight("Black", 6))
        self.gameTiles[7] = Tile(7, Rook("Black", 7))
        self.gameTiles[8] = Tile(8, Pawn("Black", 8))
        self.gameTiles[9] = Tile(9, Pawn("Black", 9))
        self.gameTiles[10] = Tile(10, Pawn("Black", 10))
        self.gameTiles[11] = Tile(11, Pawn("Black", 11))
        self.gameTiles[12] = Tile(12, Pawn("Black", 12))
        self.gameTiles[13] = Tile(13, Pawn("Black", 13))
        self.gameTiles[14] = Tile(14, Pawn("Black", 14))
        self.gameTiles[15] = Tile(15, Pawn("Black", 15))

        self.gameTiles[48] = Tile(48, Pawn("White", 48))
        self.gameTiles[49] = Tile(49, Pawn("White", 49))
        self.gameTiles[50] = Tile(50, Pawn("White", 50))
        self.gameTiles[51] = Tile(51, Pawn("White", 51))
        self.gameTiles[52] = Tile(52, Pawn("White", 52))
        self.gameTiles[53] = Tile(53, Pawn("White", 53))
        self.gameTiles[54] = Tile(54, Pawn("White", 54))
        self.gameTiles[55] = Tile(55, Pawn("White", 55))
        self.gameTiles[56] = Tile(56, Rook("White", 56))
        self.gameTiles[57] = Tile(57, Knight("White", 57))
        self.gameTiles[58] = Tile(58, Bishop("White", 58))
        self.gameTiles[59] = Tile(59, Queen("White", 59))
        self.gameTiles[60] = Tile(60, King("White", 60))
        self.gameTiles[61] = Tile(61, Bishop("White", 61))
        self.gameTiles[62] = Tile(62, Knight("White", 62))
        self.gameTiles[63] = Tile(63, Rook("White", 63))

    def printB(self):
        count=0
        for x in range(64):
            print("|", end=self.gameTiles[x].pieceOnTile.toString())
            count+=1
            if count==8:
                print("|",end="\n")
                count=0

    def getBoardArr(self):
        boardArr = []
        for tiles in range(len(self.gameTiles)):
            if (self.gameTiles[tiles].pieceOnTile.toString() == "-"):
                boardArr.append(0)
            else:
                if (self.currentPlayer == "White"):
                    boardArr.append(self.gameTiles[tiles].pieceOnTile.value)
                else:
                    boardArr.append(-self.gameTiles[tiles].pieceOnTile.value)
        return boardArr

    def getBoardArrSide(self):
        boardArr = []
        for tiles in range(len(self.gameTiles)):
            if (self.gameTiles[tiles].pieceOnTile.toString() == "-"):
                boardArr.append(0)
            else:
                if (self.gameTiles[tiles].pieceOnTile.alliance == "White"):
                    boardArr.append(self.gameTiles[tiles].pieceOnTile.value)
                else:
                    boardArr.append(-self.gameTiles[tiles].pieceOnTile.value)
        return boardArr