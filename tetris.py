from enum import Enum

class Rotation(Enum):
  ZERO = 0
  ONE = 1
  TWO = 2
  THREE = 3

class Block:
  def __init__(self):
    self.cells = []
    self.rotation = Rotation.ZERO
    self._num_rotations = 4

  def rotate_right(self):
    new_rotation_value = (self.rotation.value + 1) % self._num_rotations
    self.rotation = Rotation(new_rotation_value)
    return self

  def rotate_left(self):
    new_rotation_value = (self.rotation.value - 1) % self._num_rotations
    self.rotation = Rotation(new_rotation_value)
    return self

  def get_cells(self):
    return [self._rotated_cell(cell) for cell in self.cells]

  def _rotated_cell(self, cell):
    num_rotations = self.rotation.value
    (r, c) = cell
    for i in range(num_rotations):
      (r, c) = self._rotate_cell(r, c)
    return (r, c)

  def _rotate_cell(self, r, c):
    # rotate clockwise by 90 degrees
    return (c, -r)

class StraightBlock(Block):
  def __init__(self):
    super().__init__()
    self.cells = [(0,0), (0, 1), (0,2), (0,3)] # (row, column)

class Board:
  def __init__(self, num_rows, num_cols):
    self.num_rows = num_rows # Y-AXIS
    self.num_cols = num_cols # X-AXIS
    self.rows = [self.generate_empty_row() for i in range(num_rows)]

    #5 rows, 6 columns
    #[[ False, False, False, False, False, False ],
    # [ False, False, False, False, False, False ],
    # [ False, False, False, False, False, False ],
    # [ False, False, False, False, False, False ],
    # [ False, False, False, False, False, False ]]




  def generate_empty_row(self):
    return [False for i in range(self.num_cols)]


  def place_block(self, block, column):

    highest_row_blocked = 0
    for i in range(self.num_rows):
      if self.rows[i][column] == True:
        highest_row_blocked = i
        break
    print("highest blocked row", highest_row_blocked)

    for i in range(highest_row_blocked - 1, self.num_rows):
      if self.detect_collision( block, (i, column)):
        print("collided at", i, column)
        for c in block.cells:
          self.rows[c[0] + i][c[1] + column] = True
        print
        break
      else:
        pass



    
  """
    block - an instance of Block
    position - (row, column) where row and column are integer
    returns true if block has "collided" with another block and is unable to fall further.
  """
  def detect_collision(self, block, position):
    print("detecting collision", position)
    for i in block.cells:
      cell_row = i[0] + position[0]
      cell_column = i[1] + position[1]
      if cell_row < 0:
        # hit ceiling, GG
        pass
      elif cell_row + 1 >= self.num_rows:
        return True
      elif cell_column > self.num_cols:
        #colliding with side, collission of some sorts
        return True
      else:
        block_position = ( cell_row , cell_column)
        if self.rows[block_position[0]+1][block_position[1]] == True:
          return True
    return False

newBoard = Board(20, 10)
newBlock = StraightBlock()
newBoard.place_block(newBlock, 5)
print(newBlock.get_cells())

newBlock = StraightBlock().rotate_left()
print(newBlock.get_cells())
newBoard.place_block(newBlock, 5)
newBoard.place_block(newBlock, 6)


viewableBoard = newBoard.rows

for i in viewableBoard:
  print( ''.join(['x' if j else 'o' for j in i]) )