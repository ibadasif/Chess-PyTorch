from pieces.piece import Piece
class Bishoop(Piece):
    alliance = None
    pos = None
    def __init__(self,alliance,pos):
        self.alliance=alliance
        self.pos=pos

    def toString(self):
        return "B" if self.alliance == "Black" else "b"
