#!/lsstenvi/bin/python

#kk
import tkinter as tk
tk.TkVersion
print("hello World!")
class User:
	def __init__(self,username,isOnline):
		self.username = username
		self.isOnline = isOnline

class Host(User):
	def __init__(self,name,isOnline):
		User.__init__(self,username,isOnline)


person = User()
person.username = "lsstenvi"
person.isOnline = True

print(person.username)
print(person.isOnline)

dude = Host()
dude.username = "hostDude"
dude.isOnline = True


top = tk.Tk()

top.title("First GUI")

top.mainloop()
