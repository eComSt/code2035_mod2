#ПРОЕКТ-ИГРА "САПЁР"

from tkinter import *
from  random import choice
list = []; btn = []
gamefield = []
new_move = 0
danger=40

def play(n):
    global new_move, danger
    new_move += 1
    if new_move == 1:
        tk.title('Всего '+str(danger)+' мин!')
        i = 0
        while i<40:
            a = choice(range(0, 256))
            if a != n and gamefield[a] != -1:
                gamefield[a] = -1
                i += 1
        for i in range(0, 256):
            if gamefield[i] != -1:
                k = 0
                if i not in range(0, 256, 16):
                    if gamefield[i-1] == -1: k += 1
                    if i > 15:
                        if gamefield[i-17] == -1: k += 1
                    if i < 240:
                        if gamefield[i+15] == -1: k += 1
                if i not in range(-1, 256, 16):
                    if gamefield[i+1] == -1: k += 1
                    if i > 15:
                        if gamefield[i-15] == -1: k += 1
                    if i < 240:
                        if gamefield[i+17] == -1: k += 1
                if i > 15:
                    if gamefield[i-16] == -1: k += 1
                if i < 240:
                    if gamefield[i+16] == -1: k += 1
                gamefield[i] = k
                
    btn[n].config(text=gamefield[n], state=DISABLED)
    if gamefield[n] == 0:
        btn[n].config(text=' ', bg='#ccb')
    elif gamefield[n] == -1:
        btn[n].config(text='\u2620')
        if new_move <= (256 - 40):
            tk.title('Игра окончена.')
            new_move = 256
            one_by_one(0)
    if new_move == (256 - 40):
        tk.title('Вы выйграли!')
        win(0)

def one_by_one(a):
    for i in range(a, 256):
        if gamefield[i] == -1 and btn[i].cget('text') == ' ':
            btn[i].config(text='\u2620')
            btn[i].flash()
            tk.bell()
            tk.after(50, one_by_one, i + 1)
            break

def win(a):
    for i in range(a, 256):
        if gamefield[i] == 0:
            btn[i].config(state=NORMAL, text='☺')
            btn[i].flash()
            tk.bell()
            btn[i].config(text=' ', state=DISABLED)
            tk.after(50, win, i + 1)
            break

def show(n):
    if (btn[n].cget('state')) != 'disabled':
        if btn[n].cget('text') == '\u2661':
            btn[n].config(text=' ')
            danger += 1
        else:
            btn[n].config(text='\u2661')
            danger -= 1
        tk.title('Всего '+str(danger)+' мин!')

def start_new_game():
    global new_move, btn1, danger
    new_move = 0; danger = 40
    for i in range(0, 256):
        gamefield[i] = 0
        btn[i].config(text=' ', state=NORMAL, bg=btn1)

tk = Tk()

for i in range(0, 16):
    list.append(Frame())
    list[i].pack(expand=YES, fill=BOTH)
    for a in  range(0, 16):
        btn.append(Button(list[i], text=' ',
                          font=('mono', 16, 'bold'),
                          width=2, height=1,
                          command=lambda n=i*16+a: play(n)))
        btn[i*16+a].pack(side=LEFT, expand=NO, fill=Y)
        btn[i*16+a].bind('<Button-3>', lambda event, n=i*16+a: show(n))
        gamefield.append(0)

Button(tk, text='Начать сначала', font=(16),
       command=start_new_game).pack(side=LEFT, expand=YES, fill=Y)

btn1 = btn[0].cget('bg')

mainloop()