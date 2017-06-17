from tkinter import *



LARGEUR = 228
HAUTEUR = 228

CELLS = 3

players = ['x', 'O']
player = 'X'

def NouvellePartie():
    MonCanevas.delete(ALL)
    grid()
    Xwins.set('0')
    Owins.set('0')
    

def Click(event):
    global player
    x = 76 * (event.x//76) +18
    y = 76 * (event.y//76) +18
    print(x, y)
    if player == 'O':
        player = 'X'
        cercle(x, y)
    else:
        player = 'O'
        croix(x, y)
        

def cercle(x, y):
    "Animate cercle"
    r = 40
    c = x+20, y+20
    xy = x, y, x+r, y+r
    for s in range(0, 361, 10):
        MonCanevas.create_arc(xy, start=90, extent=s, outline='#FFF3E0', style=ARC , width=4)
        MonCanevas.update()
        MonCanevas.after(6)
    MonCanevas.create_arc(xy, start=82, extent=8, outline='#FFF3E0', style=ARC , width=4)
    

def croix(x, y):
    "Animate cross"
    r = 40
    croix = MonCanevas.create_line(x, y, x+2, y+2, fill='#424242', width=4)
    for d in range(4, 41, 2):
        MonCanevas.coords(croix, x, y, x+d, y+d)
        MonCanevas.update()
        MonCanevas.after(6)
    MonCanevas.create_line(x+r, y, x, y+r, fill='#424242', width=4)



def grid():
    topHor1 = MonCanevas.create_line(114, 76, 114, 76, fill='#26A69A', width=3)
    topHor2 = MonCanevas.create_line(114, 76, 114, 76, fill='#26A69A', width=3)

    topVer1 = MonCanevas.create_line(114, 76, 114, 76, fill='#26A69A', width=3)
    topVer2 = MonCanevas.create_line(114, 76, 114, 76, fill='#26A69A', width=3)
    for x in range(2, 108, 2):
        MonCanevas.coords(topHor1, 114-x, 76, 114+x, 76)
        MonCanevas.coords(topHor2, 114-x, 152, 114+x, 152)
        MonCanevas.coords(topVer1,76, 114-x, 76, 114+x )
        MonCanevas.coords(topVer2, 152, 114-x, 152, 114+x)
        MonCanevas.update()
        MonCanevas.after(12)
        
        

# ROOT
root = Tk()
root.title()
root.geometry('650x410')
root.resizable(0,0)

# STRING VARIBLE
Xwins = StringVar()
Xwins.set('0')

Owins = StringVar()
Owins.set('0')

tour = StringVar()
tour.set("Démarrez lz jeu ou sélectionnez un joueur.")

# TOP
topFrame = Frame(root, bg='#FAFAFA', height=130)

Xlabel = Label(topFrame, bg='white', textvariable=Xwins, width=20, font=18)
Xlabel.grid(row=1, column=1, ipady=5, ipadx=5, padx=10, pady=10)

Olabel = Label(topFrame, bg='white', textvariable=Owins, width=20, font=18)
Olabel.grid(row=1, column=2,  ipady=5, ipadx=5, padx=10, pady=10)

Label(topFrame, textvariable=tour, bg='#FAFAFA', fg="#777777").grid(row=2, column=0, columnspan=4, ipady=10)

topFrame.pack(side=TOP, padx=0, pady=0, fill=BOTH, expand=1)


# CANVAS
CanvasFrame = Frame(root, bg='#00BFA5', height=290)

MonCanevas = Canvas(CanvasFrame, width = LARGEUR, height = HAUTEUR, bg ='#00BFA5', bd=0, highlightthickness=0, relief='ridge')
MonCanevas.pack()

CanvasFrame.pack(padx=0, pady=0, fill=BOTH)



# BOTTOM
ButtomFrame = Frame(root, bg='#FAFAFA', height=40)

Button(ButtomFrame, text='REJOUER', bg='#FAFAFA', fg='#00BFA5', font=('Ariel', 11, 'bold'), relief=RAISED, bd=0, command=NouvellePartie).pack(fill=BOTH, expand=1, ipady=10)

ButtomFrame.pack(side=BOTTOM, padx=0, pady=0, fill=BOTH, expand=1)



NouvellePartie()
MonCanevas.bind('<1>', Click)
root.mainloop()

