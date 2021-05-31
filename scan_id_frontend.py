from tkinter import *
root=Tk()
root.state('zoomed')
label=Label(root,text="Scan your ID (RFID card) ",bg="BROWN",fg="LIGHT GREEN",width=80,height=400,font="Times 24 bold italic")
label.pack()
root.after(3000,root.destroy)
root.mainloop()
