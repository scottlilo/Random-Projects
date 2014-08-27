import shelve
import sqlite3

def addCust(database):
	customer = {}

	print "Add a new customer to the database\n"

	custNum = raw_input('Enter a customer number: ')
	customer['firstName'] = raw_input('Customer First Name: ')
	customer['lastName'] = raw_input('Customer last name: ')
	customer['streetAdd'] = raw_input('Customer street name: ')
	customer['city'] = raw_input('Customer city: ')
	customer['state'] = raw_input('Customer state: ')
	customer['zip'] = raw_input('Customer zip code: ')

	database[custNum] = customer
	return

def main():
	database = shelve.open('customers.dat', writeback = True)

	addCust(database)

	lookForCust = 1

	while (lookForCust != '0'):
		lookForCust = raw_input("Enter customer Number (0 to exit )")

		if lookForCust == '0':
			break
		else:
			try:
				for i in database[lookForCust]:
					print i + " " + database[lookForCust]
					break
				else:
					print "\n"
				database.close()			
if __name=='__main__': main()