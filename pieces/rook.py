from pieces.piece import Piece
class Rook(Piece):
    alliance = None
    pos = None
    def __init__(self,alliance,pos):
        self.alliance = alliance
        self.pos = pos

    def toString(self):
        return "R" if self.alliance == "Black" else "r"
