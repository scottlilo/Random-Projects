import urbandict
from Tkinter import *
index = 0
word = '  '
LoopEnd = False

def urbandefine():
	word = userword.get()
	data = urbandict.define(word)
	word = data[index]['word']
	definition =  data[index]['def']
	example = data[index]['example']	
	labelText.set(definition) 
	widgetLabelResult.pack(fill=y,padx=15,pady=8)


def changeLabel():
	name = "Thanks for the click " + yourName.get()
	labelText.set(name)
	yourName.delete(0, END)
	yourName.insert(0, "My name is Derek")






app = Tk()
app.title("GUI Example")
app.geometry('600x525+200+200')
app.configure(background = 'black')


labelGreeting = StringVar(None)
labelGreeting.set("Enter a Word")
widgetgreet = Label(app, textvariable=labelGreeting, height=2,bg="red")
widgetgreet.pack(padx=15,pady=10)

userword = StringVar(None)
widgetwordprompt = Entry(app, textvariable=userword,bg="grey")
widgetwordprompt.pack(padx=15,pady=10)

labelText = StringVar(None)
labelText.set("Your definition will go here.")
widgetLabelResult = Label(app, textvariable=labelText, height=20, width = 50, bg="red",)
widgetLabelResult.pack(padx=15,pady=8)

widgetbutton1 = Button(app, text="Look up Definition", width=20,command=urbandefine,bg="red")
widgetbutton1.pack(side='bottom',padx=15,pady=8)

app.mainloop()
