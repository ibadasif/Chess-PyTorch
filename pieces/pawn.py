from pieces.piece import Piece
class Pawn(Piece):
    alliance = None
    pos = None
    def __init__(self,alliance,pos):
        self.alliance=alliance
        self.pos=pos

    def toString(self):
        return "P" if self.alliance == "Black" else "p"