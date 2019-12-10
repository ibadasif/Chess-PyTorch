import pygame
from board.chessboard import Board

pygame.init()
Display = pygame.display.set_mode((500,500))
pygame.display.set_caption("ChessGame")
Clock = pygame.time.Clock()
QuiteGame = False
chessBoard= Board()
chessBoard.createBoard()
chessBoard.printB()
allTitles=[]
allPieces=[]
def square(x,y,width,height,color):
    pygame.draw.rect(Display,color,[x,y,width,height])
    allTitles.append([color, [x, y, width, height]])
def draw_chess_pieces():
    x_position = 0
    y_position = 0
    Width = 100
    Height = 100
    color = 0
    Black = (0,0,0)
    White = (255,255,255)
    number = 0
    for x in range(8):
        for y in range(8):
            if color % 2 == 0:
                square(x_position,y_position,Height,Width,White)
                if not chessBoard.gameTiles[number].pieceOnTile.toString == "-":
                    img = pygame.image.load("./chessart/"
                                            + chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                            + chessBoard.gameTiles[number].pieceOnTile.toString().upper()
                                            + ".png")
                    img = pygame.transform.scale(img,(100,100)) #reform the image
                    allPieces.append([img,[x_position,y_position],chessBoard.gameTiles[number].pieceOnTile])
                x_position += 100

            else:
                square(x_position, y_position, Height, Width, Black)
                if not chessBoard.gameTiles[number].pieceOnTile.toString == "-":
                    img = pygame.image.load("./chessart/"
                                            + chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                            + chessBoard.gameTiles[number].pieceOnTile.toString().upper() +
                                            ".png")
                    img = pygame.transform.scale(img,(100, 100))  # reform the image
                    allPieces.append([img, [x_position, y_position], chessBoard.gameTiles[number].pieceOnTile])
                x_position += 100
            color+=1
            number+=1
        color+=1
        x_position=0
        y_position+=100

draw_chess_pieces()

while not QuiteGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QuiteGame = True
            pygame.quit()
            quit()

    pygame.display.update()
    Clock.tick(60)