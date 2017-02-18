import tkinter as tk
from tkinter import ttk, Menu , messagebox as mBox
import random

class SgameGUI:
	def __init__(self, win):
		self.win = win
		win.title("Sgame")
		
		self.frmGame = tk.Frame(win)
		self.frmGame.grid(column=0, row=0)
		self.frmMsg = tk.Frame(win)
		self.frmMsg.grid(column=0, row=1)
		self.frmCtrl = tk.Frame(win)
		self.frmCtrl.grid(column=0, row=2)
		
		self.click_counts = 0
		self.control = [-1 for x in range(9)]
		for var in range(9):
			place = random.randint(0,8)
			while self.control[place] != -1:
				if place == 8:
					place = 0
				else:
					place +=1
			self.control[place] = var
			
		self.btnArr = []
		for cntr in range(9):
			self.btnArr.append(ttk.Button(self.frmGame,
									text=str(self.btn_label(cntr)), 
									command=lambda keynum=cntr:self.clickMe(keynum)))
			self.btnArr[cntr].height = 2111
			self.btnArr[cntr].grid(row=(cntr//3),column=(cntr%3))
	
		self.btnReset = ttk.Button(self.frmCtrl, text='Reset', command=self.game_reset)
		self.btnReset.grid(column=0, row=1)
		self.btnReset = ttk.Button(self.frmCtrl, text='Exit', command=self.game_exit)
		self.btnReset.grid(column=2, row=1)
		self.btnReset = ttk.Button(self.frmCtrl, text='About', command=self.game_about)
		self.btnReset.grid(column=1, row=1)
		
		self.lblStart = ttk.Label(self.frmMsg, text="")
		self.lblStart.grid(column=0, row=0)
		## Menus
		self.menuBar = Menu(win) 
		win.config(menu=self.menuBar)
		self.fileMenu = Menu(self.menuBar, tearoff=0) # 1
		self.fileMenu.add_command(label="Exit", command=self.game_exit)
		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.helpMenu = Menu(self.menuBar, tearoff=0) # 2
		self.helpMenu.add_command(label="Info",command=self.game_about)
		self.fileMenu.add_separator() 
		self.helpMenu.add_command(label="About",command=self.game_about)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
	
	def game_about(self):
		message = 'Sgame from Subodh' + '\n'
		message += 'isubodh@gmail.com'
		mBox.showinfo('Abt', message) 

	def clickMe(self,keynum):
		self.click_counter(1)
		self.move_key(keynum)
		self.btnReLabel()
		self.verify()
		
	def click_counter(self,count):
		if count == 0: self.click_counts =0
		else: self.click_counts += count
		self.lblStart.configure(text='Number of clicks : ' + str(self.click_counts), justify='center')
		
	def btn_label(self,x):
		if self.control[x] != 0 :
			return str(self.control[x])
		else:
			return str('')
			
	def btnReLabel(self):
		for var in range(9):
			if self.control[var] != 0:
				self.btnArr[var].configure(text=str(self.control[var]))
				self.btnArr[var].state = 'NORMAL'
			else:
				self.btnArr[var].configure(text=str(''))
				self.btnArr[var].state = 'DISABLED'

	def verify(self):
		#global click_counts
		for var in range(9):
			if var != self.control[var]:
				return
		mBox.showinfo('Winner','Hey !congrats U Won in '+self.click_counts+' cliks') 
		
	def game_reset(self):
		self.click_counter(0)
		#global control
		self.control = [-1 for x in range(9)]
		for var in range(9):
			place = random.randint(0,8)
			while self.control[place] != -1:
				if place == 8:
					place = 0
				else:
					place +=1
			self.control[place] = var
		self.btnReLabel()
		
	def move_key(self,key):
		#global control
		## Check Right
		if key%3 != 2:
			if self.control[key +1] == 0:
				self.control[key+1] = self.control[key]
				self.control[key]=0
				return
		## Check Left
		if key%3 != 0:
			if self.control[key -1] == 0:
				self.control[key-1] = self.control[key]
				self.control[key]=0
				return
		## check Down
		if key//3 != 2:
			if self.control[key + 3] == 0:
				self.control[key+3] = self.control[key]
				self.control[key]=0	
				return
		## check Up
		if key//3 != 0:
			if self.control[key - 3] == 0:
				self.control[key-3] = self.control[key]
				self.control[key]=0	
				return
					
	def game_exit(self):
		self.win.quit()
		self.win.destroy()
		exit()

win = tk.Tk()
mySgame = SgameGUI(win)
win.mainloop()
		


	





	






