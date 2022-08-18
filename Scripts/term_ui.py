import os

class Ui_grid:
    grid = []
    current_row = 0

    def add_row(self, row):
        self.grid.append(row)

    def append_row(self, row):

    def redraw(self):
        line = ""
        window_size = os.get_terminal_size()
        window_size_y = window_size[1]
        window_size_x = window_size[0]
        print(window_size_x)
        
        while window_size_x > 0:
            line += "_"
            window_size_x -= 1

        print(self.current_row)
     
        for i in self.grid:
            print(i)
        
        print(line)

    def select_row(self):
        self.redraw(self)

        current_row = self.current_row
        grid = self.grid
        key_press = input()

        if key_press == "w" and current_row > 0:
            current_row += -1
        elif key_press == "s" and current_row < len(grid):
            current_row += 1
        else:
            pass
    

# Creating Grid
my_grid = Ui_grid

# Creating rows
row_ammount = 7
num = 0
while row_ammount > 0:
    my_grid.add_row(Ui_grid, "Row {}".format(num))
    num += 1
    row_ammount -= 1


# Selecting rows
while True:
    my_grid.select_row(Ui_grid)

#    os.system("cls")
