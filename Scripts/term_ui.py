import os

class Ui_grid:
    grid = []
    current_row = 0
    window_size = os.get_terminal_size()
    window_size_y = window_size[1]
    window_size_x = window_size[0]


    def add_row(self, row):
        self.grid.append(row)

    def append_row(self, row):
        pass

    def redraw(self):
        self.current_row
        self.window_size
        self.window_size_y
        self.window_size_x = self.window_size_x
        line = ""

        self.window_size_y = self.window_size[1]
        self.window_size_x = self.window_size[0]

        
        while self.window_size_x > 0:
            line += "_"
            self.window_size_x -= 1
     
        for x, i in enumerate(self.grid):
            if x == self.current_row:
                print(">" + str(i))
            else:
                print(i)
        
        #print("Current row: (" + str(self.current_row))
        
        print(line)

    def change_row(self):

        self.current_row
        grid = self.grid
        key_press = input()

        if key_press == "w" and self.current_row > 0:
            self.current_row += -1
        elif key_press == "s" and self.current_row < len(grid):
            self.current_row += 1
        else:
            pass

        self.redraw(self)


# Creating Grid
my_grid = Ui_grid

# Creating rows
row_ammount = 20
num = 0
while row_ammount > 0:
    my_grid.add_row(Ui_grid, "{})".format(num))
    num += 1
    row_ammount -= 1


# While running
while True:
    my_grid.change_row(Ui_grid)

#    os.system("cls")
