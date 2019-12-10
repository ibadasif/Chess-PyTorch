from pieces.piece import Piece
class Queen(Piece):
    alliance = None
    pos = None
    def __init__(self,alliance,pos):
        self.alliance = alliance
        self.pos = pos
    def toString(self):
        return "Q" if self.alliance == "Black" else "q"
