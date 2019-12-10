class Tile:

    pieceOnTile = None
    tileCoordinate = None

    def __init__(self, Coordinate, piece):
        self.pieceOnTile = piece
        self.tileCoordinate = Coordinate