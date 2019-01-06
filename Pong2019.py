from tkinter import *

fenetre = Tk()


# creation de la fenetre principale du jeu
canevas = Canvas(fenetre, bg = 'black', height = 500, width = 725)
label = Label(fenetre, text = 'PONG', fg = 'blue', bg = 'black')
canevas.create_line(362.5,0,362.5,500, fill = 'white', width = 5)
Bouton_Quitter=Button(fenetre, text ='Quitter', command = fenetre.destroy)

# creation de la balle au centre dans notre fenetre et deplacement

Pos_X = 35
Pos_Y = 240
dx = 0
dy = 5

ball = canevas.create_oval(Pos_X,Pos_Y,Pos_X+20,Pos_Y+20,fill='red')

def deplacement():
    global dx, dy
    if canevas.coords(ball)[3]>500:
        dy = -1*dy
    canevas.move(ball,dx,dy)

# creation de la premiere raquette du jeu
raquette1 = canevas.create_rectangle(710,499,724,430,fill='red')

# creation de la seconde raquette de jeu
raquette2 = canevas.create_rectangle(1,1,15,70,fill='red')

# creation de la direction de la raquette 1
def bas(event):
    canevas.move(raquette1,0,10)

canevas.bind_all('<Down>', bas)

def haut(event):
    canevas.move(raquette1,0,-10)

canevas.bind_all('<Up>', haut)

# creation de la direction de la raquette 2
def haut(event):
    canevas.move(raquette2,0,-10)

canevas.bind_all('<a>', haut)

def bas(event):
    canevas.move(raquette2,0,10)

canevas.bind_all('<w>', bas)


label.pack()
canevas.pack()
Bouton_Quitter.pack()
deplacement()


fenetre.mainloop()