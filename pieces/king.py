from pieces.piece import Piece
class King(Piece):
    alliance = None
    pos = None
    def __init__(self,alliance,pos):
        self.alliance = alliance
        self.pos = pos

    def toString(self):
        return "K" if self.alliance == "Black" else "k"