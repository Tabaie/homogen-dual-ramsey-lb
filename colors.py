from z3 import BitVecSort, BitVecVal

class ColorInfo:
    def __init__(self, colorNum):
        self.size = (colorNum-1).bit_length()
        self.sort = BitVecSort(max(1, self.size))
        self.max = BitVecVal(colorNum-1, max(1,self.size))
