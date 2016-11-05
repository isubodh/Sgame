import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import random
import sgameDll as dll

win = tk.Tk()
win.title("Sgame")
frmGame = tk.Frame(win)
frmGame.grid(column=0, row=0)
frmCtrl = tk.Frame(win)
frmCtrl.grid(column=0, row=1)

		
click_counts = 0
control = [-1 for x in range(9)]
for var in range(9):
	place = random.randint(0,8)
	while control[place] != -1:
		if place == 8:
			place = 0
		else:
			place +=1
	control[place] = var
print('After Start',control)
	
def clickMe(keynum):
	print('In clickMe', keynum, control)
	click_counter(1)
	move_key(keynum)
	btnReLabel()
	verify()

def click_counter(count):
	global click_counts
	if count == 0: click_counts =0
	else: click_counts += count
	lblStart.configure(text='Number of clicks :' + str(click_counts))
	
def btn_label(x):
	print('In btn_label', control)
	if control[x] != 0 :
		return str(control[x])
	else:
		return str('')

def btnReLabel():
	print('In btnReLabel', control)
	for var in range(9):
		if control[var] != 0:
			btnArr[var].configure(text=str(control[var]))
			btnArr[var].state = 'NORMAL'
		else:
			btnArr[var].configure(text=str(''))
			btnArr[var].state = 'DISABLED'

def verify():
	global click_counts
	print('In verify', control)
	for var in range(9):
		if var != control[var]:
			return
	mBox.showinfo('Winner','Hey !congrats U Won in '+click_counts+' cliks') 

def game_reset():
	click_counter(0)
	print('In game_reset', control)
	global control
	control = [-1 for x in range(9)]
	for var in range(9):
		place = random.randint(0,8)
		while control[place] != -1:
			if place == 8:
				place = 0
			else:
				place +=1
		control[place] = var
	btnReLabel()

def move_key(key):
	global control
	print('In move_key', key, control)
	## Check Right
	if key%3 != 2:
		if control[key +1] == 0:
			control[key+1] = control[key]
			control[key]=0
			print('Right move', key, control)
			return
	## Check Left
	if key%3 != 0:
		if control[key -1] == 0:
			control[key-1] = control[key]
			control[key]=0
			print('Left move', key, control)
			return
	## check Down
	if key//3 != 2:
		if control[key + 3] == 0:
			control[key+3] = control[key]
			control[key]=0	
			print('Down move', key, control)
			return
	## check Up
	if key//3 != 0:
		if control[key - 3] == 0:
			control[key-3] = control[key]
			control[key]=0	
			print('Up move', key, control)
			return
			
def game_exit():
	exit()

def game_about():
	message = 'Sgame from Subodh' + '\n'
	message += 'isubodh@gmail.com'
	mBox.showinfo('Abt', message) 
	
btnArr = []
for cntr in range(9):
	btnArr.append(ttk.Button(frmGame, text=str(btn_label(cntr)), command=lambda keynum=cntr:clickMe(keynum)))
	btnArr[cntr].grid(row=(cntr//3),column=(cntr%3))


btnReset = ttk.Button(frmCtrl, text='Reset', command=game_reset)
btnReset.grid(column=0, row=1)
btnReset = ttk.Button(frmCtrl, text='Exit', command=game_exit)
btnReset.grid(column=2, row=1)
btnReset = ttk.Button(frmCtrl, text='About', command=game_about)
btnReset.grid(column=1, row=1)

lblStart = ttk.Label(frmCtrl, text="")
lblStart.grid(column=0, row=0)

win.mainloop()

