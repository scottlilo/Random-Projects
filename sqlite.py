import sqlite3

createDb = sqlite3.connect('sample.db')

queryCurs = createDb.cursor()

def createTable():
	queryCurs.execute('''CREATE TABLE customers
	(id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT, balance REAL)''')

def addCust(name,street,city,state,balance):
	queryCurs.execute('''INSERT INTO Customers (name,street,city,state,balance)
values (?,?,?,?,?)''',(name,street,city,state,balance))		

def main():
	createTable()

	addCust('Derek Banas','5708 highqay ave', 'verona', 'ny', 10.76)
	addCust('Scott Lilo','1210 central ave' ,'Aberdeen', 'PA', 150.6)
	addCust('Jenna Cohen','86 North Main Street', 'Marlboro', 'NJ', 150.7)
	addCust('Nick Sclafani','23 graversham rd', 'coltzneck', 'Nj', 0.76)

	createDb.commit()

	queryCurs.execute('SELECT * FROM customers ORDER BY balance')

	listTitle = ['Id Num','Name ','Street','City','State','Balance']
	k = 0

	for i in queryCurs:
		print "\n"
		for j in i:
			print j
			if k < 5: k+=1
		else: k = 0
	queryCurs.close()
	
if __name__ == '__main__':main()

