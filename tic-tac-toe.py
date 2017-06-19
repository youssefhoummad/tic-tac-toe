"Tic Toc Toe Game powerd by tkinter and python"

import tkinter as tk

# COLORs
CB = '#00BFA5'  # canvas background
RB = '#FAFAFA'  # root bacKground
LB = 'white'    # label background
GC = '#26A69A'  # grid color
OC = '#FFF3E0'  # cercle color
XC = '#424242'  # cross color
AC = '#777777'  # astus color

# fonts
FONT = ('Trebuchet MS', 11, 'bold')

# canvas dimensions
WIDTH = 228
HEIGHT = 228

R = 40          # O and X rayon




class iLabel(tk.Frame):
    "special label widget"
    def __init__(self, master, text, textvariable):
        tk.Frame.__init__(self, master)
        self.config(bg=LB, width=200, height=30, borderwidth=1, relief=tk.GROOVE)
        self.pack_propagate(0)

        self.text = text
        self.textvariable = textvariable

        self.create_labels()
        self.create_bottom_border()

        self.active = False

    def create_labels(self):
        "create two labels juxtapose"
        frame = tk.Frame(self, bg=LB)
        tk.Label(frame, text=self.text, bg=LB, font=FONT).pack(side=tk.LEFT, ipadx=5)
        tk.Label(frame, textvariable=self.textvariable, bg=LB,\
                 font=FONT).pack(side=tk.RIGHT, ipadx=5)
        frame.pack(fill=tk.X)

    def create_bottom_border(self):
        "Border display under iLabel"
        self.border = tk.Frame(self, height=2, bg=CB)

    def activate(self):
        "show border"
        self.border.pack(side=tk.BOTTOM, fill=tk.X)
        self.active = True

    def desactivate(self):
        "hide border"
        self.border.pack_forget()
        self.active = False

    def toggle_active(self):
        "hide or show border"
        if self.active:
            self.desactivate()
        else:
            self.activate()

#
class iCanvas(tk.Canvas):
    "special canvas has grid"
    def __init__(self, master):
        tk.Canvas.__init__(self, master)
        self.config(bg=CB, width=WIDTH, height=HEIGHT, bd=0, \
                    highlightthickness=0, relief=tk.RIDGE)

    def create_grid(self):
        "grid line with animation"
        line_1 = self.create_line(114, 76, 114, 76, fill=GC, width=3)
        line_2 = self.create_line(114, 76, 114, 76, fill=GC, width=3)

        line_3 = self.create_line(114, 76, 114, 76, fill=GC, width=3)
        line_4 = self.create_line(114, 76, 114, 76, fill=GC, width=3)
        for x in range(2, 108, 2):
            self.coords(line_1, 114-x, 76, 114+x, 76)
            self.coords(line_2, 114-x, 152, 114+x, 152)
            self.coords(line_3, 76, 114-x, 76, 114+x)
            self.coords(line_4, 152, 114-x, 152, 114+x)
            self.update()
            self.after(8)

    def create_cercle(self, x, y):
        "create cercle with animation"
        xy = x, y-5, x+R, y+R+5
        for s in range(0, 361, 10):
            self.create_arc(xy, start=90, extent=s, outline=OC, style=tk.ARC, width=4)
            self.update()
            self.after(6)
        self.create_arc(xy, start=82, extent=8, outline=OC, style=tk.ARC, width=4)

    def create_cross(self, x, y):
        "create X cross with animation"
        line = self.create_line(x, y, x+2, y+2, fill=XC, width=4)
        for d in range(4, 41, 2):
            self.coords(line, x, y, x+d, y+d)
            self.update()
            self.after(6)
        self.create_line(x+R, y, x, y+R, fill=XC, width=4)

    def create_trace(self, x1, y1, x2, y2, winner):
        "line dahed"
        color = OC if winner == 'O' else XC
        xy = x1 * 76 + R, y1 * 76 + R, x2 * 76 + R, y2 * 76 + R
        self.create_line(xy, width=4, fill=color, dash=(2, 4))
    
    def board_X(self):
        "when X win popup this board"
        self.delete(tk.ALL)
        self.create_line(70, 60, 158, 168, fill=XC, width=10)
        self.create_line(158, 60, 70, 168, fill=XC, width=10)
        self.update()
        self.after(50)
        self.create_text(114, 210, text="WINNER!", fill=XC, font=('Trebuchet MS', 20, 'bold'))

    def board_O(self):
        "when O win popup this board"
        self.delete(tk.ALL)
        xy = 70, 60, 158, 168
        self.create_oval(xy, outline=OC, width=10)
        self.update()
        self.after(50)
        self.create_text(114, 210, text="WINNER!", fill=XC, font=('Trebuchet MS', 20, 'bold'))

    def board_XO(self):
        "when X & O drew popup this board"
        self.delete(tk.ALL)
        self.create_line(50, 60, 118, 158, fill=XC, width=10)
        self.create_line(118, 50, 60, 158, fill=XC, width=10)
        xy = 120, 60, 188, 158
        self.create_oval(xy, outline=OC, width=10)
        self.update()
        self.after(50)
        self.create_text(114, 210, text="DRAW!", fill=XC, font=('Trebuchet MS', 20, 'bold'))


#
class iButton(tk.Button):
    "special button"
    def __init__(self, master, text, command):
        tk.Button.__init__(self, master=master)
        self.config(bg=RB, fg=CB, font=FONT, relief=tk.RAISED,\
            bd=0, command=command, text=text)

#
class Game(tk.Tk):
    "Game tic toc toe"
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Tic-Tac-Toe')
        self.geometry('650x410')
        self.resizable(0, 0)
        self.config(bg=RB)

        # variable
        self.PLAYER, self.MOVE, self.CELLS, self.WINNER = '', 0, [], None

        # stringvar
        self.wins_X = tk.StringVar()
        self.wins_O = tk.StringVar()
        self.wins_X.set('-')
        self.wins_O.set('-')

        self.create_widgets()
        self.canvas.bind('<1>', self.click)
        self.start()

    def create_widgets(self):
        "interface"
        # header frame
        header = tk.Frame(self, bg=RB, height=100)
        self.player_X = iLabel(header, 'X', self.wins_X)
        self.player_X.pack(side=tk.LEFT, padx=60)
        self.player_O = iLabel(header, 'O', self.wins_O)
        self.player_O.pack(side=tk.RIGHT, padx=60)
        header.pack_propagate(0)
        header.pack(fill=tk.X, ipady=10)
        # canvas frame
        frame = tk.Frame(self, bg=CB, height=HEIGHT)
        self.canvas = iCanvas(frame)
        self.canvas.pack()
        frame.pack(fill=tk.BOTH)
        # footer frame
        footer = tk.Frame(self, bg=RB, height=HEIGHT)
        iButton(footer, text='RESTART GAME', command=self.start).pack(fill=tk.BOTH, expand=1, ipady=10)
        footer.pack(side=tk.BOTTOM, padx=0, pady=0, fill=tk.BOTH, expand=1)

    def initials(self):
        "default values"
        self.PLAYER = 'X'
        self.MOVE = 0
        self.CELLS = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.WINNER = None

    def start(self):
        "start game"
        self.initials()

        self.canvas.delete(tk.ALL)
        self.canvas.create_grid()

        self.player_X.activate()
        self.player_O.desactivate()


    def click(self, event):
        "event click inside canvas"
        # find the cell
        row = 3 * event.y // HEIGHT
        col = 3 * event.x // WIDTH

        # If the cell is checked previously do nothing
        if self.CELLS[row][col] != 0 or self.WINNER:
            return

        # find coords cell to draw
        x, y = 76 * col + 18, 76 * row + 18

        # show or hide border
        self.player_X.toggle_active()
        self.player_O.toggle_active()

        if self.PLAYER == 'O':
            self.canvas.create_cercle(x, y)
        else:
            self.canvas.create_cross(x, y)

        # check the winner
        self.CELLS[row][col] = self.PLAYER
        self.MOVE += 1
        self.verifier()
        # toggle player
        self.PLAYER = 'X' if self.PLAYER == 'O' else 'O'

    def verifier(self):
        "verifier"
        self.WINNER, x1, y1, x2, y2 = self.is_winner()
        if self.WINNER:
            self.canvas.create_trace(x1, y1, x2, y2, self.WINNER)
            self.canvas.update()
            self.canvas.after(500)
            self.showinfo()
            if self.WINNER == 'X':
                try:
                    self.wins_X.set(str(int(self.wins_X.get())+1))
                except ValueError:
                    self.wins_X.set('1')
            else:
                try:
                    self.wins_O.set(str(int(self.wins_O.get())+1))
                except ValueError:
                    self.wins_O.set('1')

        if self.MOVE == 9:
            self.showinfo()

    def is_winner(self):
        "all case"
        if self.MOVE < 5:
            return None, None, None, None, None
        # horizontal
        if self.CELLS[0][0] == self.CELLS[0][1] == self.CELLS[0][2] != 0:
            return self.PLAYER, 0, 0, 2, 0
        if self.CELLS[1][0] == self.CELLS[1][1] == self.CELLS[1][2] != 0:
            return self.PLAYER, 0, 1, 2, 1
        if self.CELLS[2][0] == self.CELLS[2][1] == self.CELLS[2][2] != 0:
            return self.PLAYER, 0, 2, 2, 2
        # vertival
        if self.CELLS[0][0] == self.CELLS[1][0] == self.CELLS[2][0] != 0:
            return self.PLAYER, 0, 0, 0, 2
        elif self.CELLS[0][1] == self.CELLS[1][1] == self.CELLS[2][1] != 0:
            return self.PLAYER, 1, 0, 1, 2
        elif self.CELLS[0][2] == self.CELLS[1][2] == self.CELLS[2][2] != 0:
            return self.PLAYER, 2, 0, 2, 2
        # diagonal
        elif self.CELLS[0][0] == self.CELLS[1][1] == self.CELLS[2][2] != 0:
            return self.PLAYER, 2, 2, 0, 0
        elif self.CELLS[0][2] == self.CELLS[1][1] == self.CELLS[2][0] != 0:
            return self.PLAYER, 2, 0, 0, 2

        return None, None, None, None, None

    def showinfo(self):
        "POPUP MESSAGE"
        if self.WINNER == 'X':
            self.canvas.board_X()
        elif self.WINNER == 'O':
            self.canvas.board_O()
        else:
            self.canvas.board_XO()



# 


if __name__ == '__main__':
