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
    for i in range(self.num_rows-1, 0, -1): 
        if self.detect_collision(block, (i, column)) == True: #starting from the 3rd row. i is the row, e is the iterator 
            #we didnt collide with another block
            #print(i, column)
            for cellNumber in range(len(block.cells)):   #update the board with the new block placement
                self.rows[block.cells[cellNumber][0]+i][block.cells[cellNumber][1]+column] = True
            break
            


    # check the bottom of the placement and find the first row where collision is true


    
  """
    block - an instance of Block
    position - (row, column) where row and column are integer
    returns true if block has "collided" with another block and is unable to fall further.
  """
  def detect_collision(self, block, position):
    for i in block.cells: #check to make sure if a single block cell is "Collided"
        cell_row = i[0] + position[0] 
        cell_column = i[1] + position[1]
        block_position = ( cell_row , cell_column ) #cell position on board
        if block_position[0] == self.num_rows-1: #are we in the first row? if so, check if empty. if empty, return True as we colliding with the floor
            return not self.rows[block_position[0]][block_position[1]] 
        elif self.rows[block_position[0]+1][block_position[1]] == True: 
            #print(block_position, "collision detected")
            return True
    return False


newBoard = Board(20, 10)
for i in range(4):
    newBoard.rows[19][i] = True

newBlock = StraightBlock()
#print(newBoard.detect_collision(newBlock, (18,0)))
# newBoard.place_block(newBlock, 5)

rotatedBlock = StraightBlock().rotate_left()
print(rotatedBlock.get_cells())

newBoard.place_block(newBlock, 0)
newBoard.place_block(newBlock, 5)

viewableBoard = newBoard.rows


for i in viewableBoard:
  print( ''.join(['x' if j else 'o' for j in i]) )