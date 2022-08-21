import os
import keyboard

def quit_program():
    exit()

class Ui_grid:

    class Row:
        name = "row name"


    grid = []
    current_row = 0
    window_size = os.get_terminal_size()
    window_size_y = window_size[1]
    window_size_x = window_size[0]


    def add_row(self, row):
        name = "row name"
        name.capitalize
        self.grid.append(row)

    def append_row(self, row):
        pass

    def redraw(self):
        os.system("cls")

        window_size = os.get_terminal_size()
        window_size_y = window_size[1]
        window_size_x = window_size[0]
        line = ""
        dotted_line = ""
        
        while window_size_x > 0:
            line += "_"
            if window_size_x <= self.window_size_x/2:
                dotted_line += "-"
            else:
                pass
            window_size_x -= 1
        
        print(line)
        print("-PYTHON CONSOLE GUI-")
        print(line)

        for x, i in enumerate(self.grid):
            if x == self.current_row:
                print(dotted_line)
                print(">" + str(i))
                print(dotted_line)
            else:
                print(i)
                
        print(line)

    def change_row(self, updown: str):
        grid = self.grid

        if updown == "up" and self.current_row > 0:
            self.current_row += -1
        if updown == "down" and self.current_row < len(grid)-1:
            self.current_row += 1
        else:
            pass

        self.redraw(self)


# Creating Grid
my_grid = Ui_grid

# Creating rows
row_ammount = 19
num = 0
while row_ammount >= 0:
    my_row = my_grid.add_row(Ui_grid, "{})".format(num) + "data block")
    my_row.name = "great"
    num += 1
    row_ammount -= 1

my_grid.add_row(Ui_grid, "new row")


w = False
s = False
esc = False

# While running
while True:

    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        my_grid.change_row(Ui_grid, "up")

    if event.event_type == keyboard.KEY_DOWN and event.name == 's':
        my_grid.change_row(Ui_grid, "down")

"""while True:
    #my_grid.change_row(Ui_grid)
    try:
        if keyboard.KEY_DOWN("w"):
            my_grid.change_row(Ui_grid, "up")
            print("moving up a row")
        if keyboard.on_press("s"):
            my_grid.change_row(Ui_grid, "down")
            print("moving down a row")
        if keyboard.on_press("esc"):
            print("quitting program")
    except:
        pass"""
