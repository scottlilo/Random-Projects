from Tkinter import *

def beenClicked():
	radioValue = relStatus.get()

def changeLabel():
	name = "Thanks for the click " + yourName.get()
	labelText.set(name)
	yourName.delete(0, END)
	yourName.insert(0, "My name is Derek")

app = Tk()
app.title("GUI Example")
app.geometry('450x450+200+200')

labelText = StringVar()
labelText.set("Click Button")
label1 = Label(app, textvariable=labelText, height=4)
label1.pack()

checkBoxVal = IntVar()
checkBox1 = Checkbutton(app, variable=checkBoxVal, text="Happy?")
checkBox1.pack()

custName = StringVar(None)
yourName = Entry(app, textvariable=custName)
yourName.pack()

relStatus = StringVar()
relStatus.set(None)
radio1 = Radiobutton(app, text="single", value="single",variable = relStatus, command=beenClicked).pack()
radio2 = Radiobutton(app, text="Married", value="single",variable = relStatus, command=beenClicked).pack()

button1 = Button(app, text="Click here", width=20,command=changeLabel)
button1.pack(side='bottom',padx=15,pady=15)
app.mainloop()