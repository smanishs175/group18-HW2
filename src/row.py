from src.utils import copy

class Row:
  def __init__(self, t):
    self.cell = t
    self.cooked = copy(t)
    self.isEvaled = False