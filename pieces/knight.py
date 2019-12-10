from pieces.piece import Piece
class Knight(Piece):
    alliance = None
    pos = None
    def __init__(self,alliance,pos):
        self.alliance = alliance
        self.pos = pos

    def toString(self):
        return "N" if self.alliance == "Black" else "n"