class Tile:

    pieceOnTile = None
    tileCoordinate = None

    def __init__(self, Coordinate, piece):
        self.tileCoordinate = Coordinate
        self.pieceOnTile = piece
