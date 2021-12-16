
"""
defining class customer, which will be taking our customers name and id. I have also defined appropriate getter
and setter functions
"""
class Customer:
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def getName(self):
		return self.name

	def getId(self):
		return self.id
	
	def get_discount(self, price):
		pass

"""
defining retail customer class which inherits from customer. It contains
an attribute to set rate of discount, which is 10 by default.
"""
class RetailCustomer(Customer):
	rate = 10
	def __init__(self, id, name):
		super().__init__(id, name)

		#the super() function here enables retail customer class to use id an name from class customer.
	
		self.rate = RetailCustomer.rate # in percentage

	def get_discount(self, price):
		return (self.rate/100)*price

	def getRate(self):
		return self.rate

#This function is used to print the details of the customer.
	def displayCustomer(self):
		print(f'Discount Rate: {self.rate}% \n Name: {self.name} \nID: {self.id}')

#Static function to adjust rate of discount.
	def setRate(self, newRate):
		RetailCustomer.rate = newRate

"""
Defining Wholesale customer class, with 2 rates of discounts depending on 
whether or not the buy value crosses the threshold of $1000.
"""
class WholesaleCustomer(Customer):
	rate1 = 10
	rate2 = rate1 + 5
	def __init__(self, id, name):
		super().__init__(id, name)
		self.rate1 = WholesaleCustomer.rate1 # in percentage
		self.rate2 = WholesaleCustomer.rate2

	def get_discount(self, price):
		if(price > 1000):
			return (self.rate2/100)*price
		else:
			return (self.rate1/100)*price

	def getRate1(self):
		return self.rate1

	def getRate2(self):
		return self.rate2

	def setRate(self, rate1):
		if(self.rate1 == 10 and self.rate2 == 15):
			return

		RetailCustomer.rate1 = rate1
		RetailCustomer.rate2 = rate1 + 5


""" the below class helps keep track of all products we have in our
inventory. Every product has a unique identifier.
"""
class Product:
	def __init__(self, id, name, price, stock):
		self.ID = id
		self.Name = name
		self.Price = price
		self.Stock = stock

"""
Class to keep track of customer orders
"""
class Order(RetailCustomer):
	def __init__(self, customerId, customerName, productId, quantity):
		Customer.__init__(self,customerId, customerName)
		self.quantity = quantity
		self.productId = productId

"""
The below class primary helps display all information pertaining to customers,
products etc. It also helps to find products and customers, for the operations that follow.
"""
class Records:

	#Function to display customers.

	def readCustomers(self):
		with open('customers.txt') as f:
			text = f.read()
			perCustomer = text.split('\n')
			format = ['ID', "Name", "Type", "Discount Rate", "Total"]
			for data in perCustomer:
				info = data.split(',')
				for i in range(len(info)):
					print(f'{format[i]}: {info[i]}', end='\t')
				print('\n')

	#Function to display products.

	def readProducts(self):
		with open('products.txt') as f:
			text = f.read()
			perProduct = text.split('\n')
			format = ['ID', "Name", "Price Per Unit", "Instock"]
			for data in perProduct:
				info = data.split(',')
				for i in range(len(info)):
					if(info[i][0][0] == 'C'):
						break
					print(f'{format[i]}: {info[i]}', end='\t')
				print('\n')

	#Function to find customer.

	def findCustomer(self, id):
		with open('customers.txt') as f:
			text = f.read()
			perCustomer = text.split('\n')
			for data in perCustomer:
				info = data.split(',')
				if(info[0] == str(id)):
					print("\nCustomer Exists !!!\n")
				else:
					print("\nCustomer does not exist\n")
					
				

	def findProduct(self, id):
		with open('products.txt') as f:
			text = f.read()
			perProduct = text.split('\n')
			for data in perProduct:
				info = data.split(',')
				if(info[0] == str(id)):
					return info

	def listCustomers(self):
		with open('customers.txt') as f:
			text = f.read()
			print(text)

	def listProducts(self):
		with open('products.txt') as f:
			text = f.read()
			print(text)

#r here helps access the components of class Records.
r = Records()

#Class Combo inherits from classs records
class Combo(Records):
	def __init__(self, combo, quantity):
		self.combo = combo
		self.totalPrice = 0
		self.quantity = quantity

	#The below method helps calculate total price of an order.

	def calculatePrice(self):

		for data in self.combo:
			productId = data.replace(' ', '')
			if(productId[0] == 'P'):
				product = self.findProduct(productId)
				self.totalPrice += float(product[2])

		self.totalPrice = (self.totalPrice*(90/100)) * self.quantity
		return self.totalPrice

#Child class operations inherits from records.
class Operations(Records):
	def __init__(self):
		self.customersList = []
		self.productsList = []
		self.orderList = []

	def loadFiles(self):
		customersData = None
		productsData = None
		with open('customers.txt') as f:
			customersData = f.read()
			self.customersList = customersData.split('\n')

		with open('products.txt') as f:
			productsData = f.read()
			self.productsList = productsData.split('/')



	"""
	Beginning of the menu, this is the main function of the program.
	The menu makes it easier for the user to access various functionalities in the program.
	it is run using a while loop and will keep running until exit option is triggered.
	"""

	def main(self):

		self.loadFiles()
		
		while True:

			print("\n*********************\n")
			print("       Welcome \n")
			print("\n*********************\n")
			print('1. Display All Customers: \n')
			print('2. Display All Products: \n')
			print('3. Create an Order: \n')
			print('4. Create a combo order \n')
			print('5. Find Customer \n')
		
			print('99. Exit: \n')
			option = int(input('Select Choice: '))

			if(option == 1):
				self.readCustomers()
				a.main()
				break

			if(option == 2):
				self.readProducts()
				a.main()
				break                                 

			if(option == 3):
				existingCustomer = False
				customerId = input('Enter Customer Id: ')
				custonerName = input('Enter Customer Name: ')
				rw = input('\n retail or wholesale? (r/w) \n')
				productId = input('Enter Product Id: ')
				product = self.findProduct(productId)
				if(product):
					print('Unit Price: ',product[2])
					quantity = input('Enter quantity: ')
					order = Order(customerId, custonerName, productId, quantity)
					totalPrice = (float(product[2].replace(' ', '')))*float(quantity)
					confirmation = input('Order confirmation[yes/no]: ')
					if(confirmation == 'yes' or 'YES'):
						self.orderList.append(order)
						with open('products.txt', 'r') as f:
							data = f.read()
						with open('products.txt', 'w') as f:
							stock = int(product[3].replace(' ', ''))
							stockLeft = stock-int(quantity)
							f.write(data.replace(str(stock), str(stockLeft)))
						
						with open('customers.txt', 'r') as f:
							myCustomersData = f.read()
							customersData = myCustomersData.split('\n')
							for customerData in customersData:
								customerData = customerData.split(',')
								if(customerData[0] == customerId):
									existingCustomer = True
									a.main()

						if(existingCustomer):
							with open('customers.txt', 'w') as f:
								prevTotalPrice = customerData[len(customerData)-1]
								totalPrice = float(order.get_discount(totalPrice))
								newTotal =  totalPrice + float(prevTotalPrice)
								f.write(myCustomersData.replace(prevTotalPrice, f' {newTotal}'))

		
						else:
							with open('customers.txt', 'a+') as f:			
								f.write(f'\n{customerId}, {custonerName}, {rw}, 10, {totalPrice}')
						

						print('Your Order has been created')
						print('Bill Amount : ',totalPrice, end='\n\n')
					a.main()
				else:
					print('Product is not found')
					a.main()

			if(option == 4):
				comboId = input('Enter ComboId: ')
				combo = self.findProduct(comboId)
				if(combo):
					quantity = input('Enter quantity: ')
					myCombo = Combo(combo, int(quantity))
					print('Total Price: ',myCombo.calculatePrice())
					confirmation = input('Order confirmation[yes/no]: ')
					if(confirmation == 'yes' or 'YES'):
						self.orderList.append(combo)
						with open('products.txt', 'r') as f:
							data = f.read()
						with open('products.txt', 'w') as f:
							stock = int(combo[len(combo)-1].replace(' ', ''))
							stockLeft = stock-int(quantity)
							f.write(data.replace(str(stock), str(stockLeft)))
						print('Your Combo Order has been created')
						print('Bill Amount : ',myCombo.totalPrice, end='\n\n')
					a.main()
				else:
					print('Combo is not found')
					a.main()
			
			if(option == 5):
				cus = input("\n Enter Customer id: \n")
				r.findCustomer(cus)
				a.main()
			

			if(option == 99):
				exit()


a = Operations()
a.main()


"""
Shortcomings:

Given more experience I would like to implement the file management functionality a bit better, I will admit in my program 
the editing of the txt files is very crude, working but crude nonetheless.

Futurescope: I believe this assignment can become so much more, we could use sql to store our data (customers, products, orders etc.)
we can also use a GUI to make it all more user friendly.
"""