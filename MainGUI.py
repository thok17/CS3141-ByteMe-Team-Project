from tkinter import Tk, Label, Button

class HomeGUI:
	def __init__(self, master):
		self.master = master
		master.title("Byte-Me")

		self.label = Label(master, text="Now Playing:")
		self.label = Label(master, text="Song Name")
		self.label = Label(master, text="Artist Name")
		self.label = Label(master, text="Album Name")
		self.label.pack()

		self.greet_button = Button(master, text="Vote Change Song", command=self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

		canvas = Canvas(root, width=300, height = 300)
		canvas.pack()
		img = PhotoImage(file="SongPicture.png")
		canvas.create_image(20,20, anchor=NW, image=img)
		

	def greet(self):
		print("Greetings!")

root = Tk()
my_gui = HomeGUI(root)
root.mainloop()