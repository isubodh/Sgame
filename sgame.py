import tkinter as tk
from tkinter import ttk, Menu , messagebox as mBox
import random

class SgameGUI:
	def __init__(self, win):
		self.win = win
		win.title("Sgame")
		
		#===========================================================================
		# Set up the Frame
		#===========================================================================
		self.frmGame = tk.Frame(win)
		self.frmGame.grid(column=0, row=0)
		self.frmMsg = tk.Frame(win)
		self.frmMsg.grid(column=0, row=1)
		self.frmCtrl = tk.Frame(win)
		self.frmCtrl.grid(column=0, row=2)
		
		#===========================================================================
		# Set up the control variables & Click counts
		#===========================================================================		
		self.game_start()
		
		#===========================================================================
		# Set up the Button Array and position them
		#===========================================================================		
		self.btnArr = []
		for cntr in range(9):
			self.btnArr.append(ttk.Button(self.frmGame,
									text=str(self.btn_label(cntr)), 
									command=lambda keynum=cntr:self.clickMe(keynum)))
			self.btnArr[cntr].height = 2111
			self.btnArr[cntr].grid(row=(cntr//3),column=(cntr%3))

		#===========================================================================
		# Set up the Button for Reset, Exit and About
		#===========================================================================			
		self.btnReset = ttk.Button(self.frmCtrl, text='Reset', command=self.game_reset)
		self.btnReset.grid(column=0, row=1)
		self.btnReset = ttk.Button(self.frmCtrl, text='Exit', command=self.game_exit)
		self.btnReset.grid(column=2, row=1)
		self.btnReset = ttk.Button(self.frmCtrl, text='About', command=self.game_about)
		self.btnReset.grid(column=1, row=1)
		
		self.lblStart = ttk.Label(self.frmMsg, text="")
		self.lblStart.grid(column=0, row=0)
		
		#===========================================================================
		# Lets have menus too
		#===========================================================================
		self.menuBar = Menu(win) 
		win.config(menu=self.menuBar)
		self.fileMenu = Menu(self.menuBar, tearoff=0) # 1
		self.menuBar.add_cascade(label="File", menu=self.fileMenu)
		self.fileMenu.add_command(label="Reset", command=self.game_reset)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label="Exit", command=self.game_exit)

		self.helpMenu = Menu(self.menuBar, tearoff=0) # 2
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
		self.helpMenu.add_command(label="Info",command=self.game_info)
		self.fileMenu.add_separator()
		self.helpMenu.add_command(label="About",command=self.game_about)
		
		
#===========================================================================
# Function to Start the Game and randomize the key labels
#===========================================================================		
	def game_start(self):
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

#===========================================================================
# Function to reset the game when not able to play it anymore
#===========================================================================			
	def game_reset(self):
		self.game_start()
		self.btnReLabel()
		self.click_counter(0)

#===========================================================================
# Let me give my contact details 
#===========================================================================		
	def game_about(self):
		message = 'Sgame from Subodh' + '\n'
		message += 'isubodh@gmail.com'
		mBox.showinfo('Abt', message)

#===========================================================================
# Function to give the player some basic instructions
#===========================================================================
	def game_info(self):
		message = 'The idea is to arrange' + '\n'
		message += 'numbers 1 - 8 ' + '\n'
		message += 'and last box as empty' + '\n'
		mBox.showinfo('Abt', message)

#===========================================================================
# Function that runs when use clicks the game keys
#===========================================================================
	def clickMe(self,keynum):
		self.click_counter(1)
		self.move_key(keynum)
		self.btnReLabel()
		self.verify()

#===========================================================================
# Function to keep count of key-strokes to make player serious
#===========================================================================		
	def click_counter(self,count):
		if count == 0: 
			self.click_counts =0
		else: 
			self.click_counts += count
		self.lblStart.configure(text='Number of clicks : ' + str(self.click_counts), justify='center')

#===========================================================================
# Function to relabel the keys
#===========================================================================		
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

#===========================================================================
# Function verify that the player has won, if so display a popup
#===========================================================================	
	def verify(self):
		for var in range(9):
			if var != self.control[var]:
				return
		mBox.showinfo('Winner','Hey !congrats U Won in '+self.click_counts+' cliks') 

#===========================================================================
# Function to show that user clicks are moving the numbers around
#===========================================================================		
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
				
#===========================================================================
# Exit funtion and cleanup code too.
#===========================================================================				
	def game_exit(self):
		self.win.quit()
		self.win.destroy()
		exit()

#===========================================================================
# Main where the action starts.
#===========================================================================	
win = tk.Tk()
SgameGUI(win)
win.mainloop()
		


	





	






