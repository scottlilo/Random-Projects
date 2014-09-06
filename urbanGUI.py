import urbandict
from Tkinter import *
index = 0
word = ''

def urbandefine():
	#Store the word in a variable
	word = userword.get()

	#Use Urban Dict API to grab dictionary data
	data = urbandict.define(word)

	#Store data for each word depending on user word
	word = data[index]['word']
	definition =  data[index]['def']
	example = data[index]['example']	

	#Set the DEFINITION widget
	labelText.set(definition) 
	widgetLabelResult.pack(padx=15,pady=8)

	#Set the WORD widget
	labelwordText.set(word) 
	widgetLabelword.pack(padx=15,pady=8)

#Create widget
app = Tk()
app.title("Urban Dictionary API")
#Set dimensions
app.geometry('600x525+200+200')
#confifugre attributes
app.configure(background = 'black')

#Greeting widget
#Greeting variable
labelGreeting = StringVar(None)
labelGreeting.set("Enter a Word")
#Create Greeting Widget
widgetgreet = Label(app, textvariable=labelGreeting, height=2,bg="red")
#Pack and finalize the widget
widgetgreet.pack(padx=15,pady=10)

#The word prompt
#User word variable
userword = StringVar(None)
#Create Word entry prompt
widgetwordprompt = Entry(app, textvariable=userword,bg="grey")
#Pack and finalize the widget
widgetwordprompt.pack(padx=15,pady=10)

#The text box which cointains the Word
#create label for word
labelwordText = StringVar(None)
labelwordText.set("wordddd")
#Create text box for word variable
widgetLabelword = Label(app, textvariable=labelwordText, height=5, width = 50, bg="red",)
#Word label widget creation
widgetLabelword.pack(padx=0,pady=5)

#The text box which contains the Defintion
#text box ( defintiion ) variable
labelText = StringVar(None)
labelText.set("Your definition will go here.")
#Create widget label for result
widgetLabelResult = Label(app, textvariable=labelText, height=12, width = 50, bg="red",)
#finalize widget and pack
widgetLabelResult.pack(padx=0,pady=5)

#The defintinon button widget
#Create Button widget
widgetbutton1 = Button(app, text="Look up Definition", width=20,command=urbandefine,bg="red")
#Finalize and pack widget
widgetbutton1.pack(side='bottom',padx=15,pady=8)

#app Loop
app.mainloop()
