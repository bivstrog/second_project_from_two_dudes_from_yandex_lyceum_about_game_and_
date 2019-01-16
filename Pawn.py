field =  [[None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None]]
class Pawn: # �����
 
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.step = 0
 
    def set_position(self, row, col):
        self.row = row
        self.col = col
 
    def char(self):
        return 'P'
 
    def get_color(self):
        return self.color
 
    def can_move(self, row, col):
        if self.col != col:
            return False
 
        # ����� ����� ������� �� ���������� ��������� ��� �� 2 ������
        # �����, ������� �������� ������ ���������� ���� � start_row.
        if self.color == WHITE:
            direction = 1
        else:
            direction = -1
 
        # ��� �� 1 ������
        if self.row + direction == row:
            return True
 
        # ��� �� 2 ������ �� ���������� ���������
        if self.row == start_row and self.row + 2 * direction == row:
            return True
 
        return False
    def can_eat(self, row, col):
        if self.row == row and (self.col + 1 == col or self.col - 1 == col):
            return True
        return False
    def check_Q(self, row, col):
        if direction == 1 and len(field[col]) == row + 1:
            return True
        if direction == -1 and row == 0:
            return True
        return False