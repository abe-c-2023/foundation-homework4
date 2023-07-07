shopStock = {
    "Oak Tree": 500,
    "Cactus": 35,
    "Cress": 6,
}

customerMoney1 = 100
customerRequest1 = input("Welcome to my plant shop! Today we are selling: {}. Please tell me which plant you want to buy, or type 'Exit' to leave ".format(shopStock))
purchaseAttempts1 = 0




def tryNbuy(customerMoney, customerRequest, purchaseAttempts):
	assert customerRequest != "Exit", "Ok, bye for now!"
	try:
		itemCost = shopStock[customerRequest]
	except:
		raise ValueError("Sorry we aren't selling that at the moment")
	else:
		purchaseAttempts += 1
		try:
			assert (customerMoney >= itemCost)
			print("Thank you for shopping with us, here is your {}. Bye for now!".format(customerRequest))
		except:       
			print("Unfortunately you do not have enough money to buy that {}".format(customerRequest))
			try:
				assert purchaseAttempts <= 3
				moreMoney = input("Do you have any more money to add? (Yes/No) ")
				if moreMoney == "Yes":
					customerMoney += int(input("How much would you like to add to your balance? "))
					tryNbuy(customerMoney, customerRequest, purchaseAttempts)
				else:
					raise Exception("Unfortunately it looks like you can't afford to buy the {} at the moment. Please come back when you have more money!".format(customerRequest))
			except:
				raise Exception("Sorry, you have made too many purchase attempts and need to leave the shop now :(")
			
			


tryNbuy(customerMoney1, customerRequest1, purchaseAttempts1)

# comment