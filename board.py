class Board:
    def __init__(self, table_row=5, table_col=5):
        self.table_row = table_row
        self.table_col = table_col
        self.boxes = [[None for x in range(table_row)] for y in range(table_col)]
        self.robo_map = {}

    def place(self, piece):
        x = piece.get_x()
        y = piece.get_y()
        if self.is_inbounds(x, y):
            self.boxes[x][y] = piece
            self.robo_map[piece.robo_id] = piece
        # else:
        #     print(f"Can't Place a robot there")

    def is_inbounds(self, x, y):
        if x < 0 or x >= self.table_row or y < 0 or y >= self.table_col:
            return False
        return True

    def get_robot(self, robo_id=1):
        return self.robo_map[robo_id]
