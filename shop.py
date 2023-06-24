shopStock = {
    "Oak Tree": 500,
    "Cactus": 35,
    "Cress": 6,
    "c": 5
}

customerMoney = 100
customerRequest = input("Welcome to my plant shop! Today we are selling: {}. Please tell me which plant you want to buy, or type 'Exit' to leave ".format(shopStock))
purchaseAttempts = 0
assert customerRequest != "Exit", "Ok, bye for now!"
try:
    itemCost = shopStock[customerRequest]
except:
    raise ValueError("Sorry we aren't selling that at the moment")



def tryNbuy():
    global purchaseAttempts
    global customerMoney
    try:
         assert purchaseAttempts < 2
    except:
       raise Exception("Sorry, you have made too many purchase attempts and need to leave the shop now :(")
    else:
       purchaseAttempts += 1
       try:
              assert (customerMoney >= itemCost)
              print("Thank you for shopping with us, here is your {}. Bye for now!".format(customerRequest))
       except:       
                     print("Unfortunately you do not have enough money to buy that {}".format(customerRequest))
                     moreMoney = input("Do you have any more money to add? (Yes/No) ")
                     if moreMoney == "Yes":
                            customerMoney += int(input("How much would you like to add to your balance? "))
                            tryNbuy()
                     else:
                           raise Exception("Unfortunately it looks like you can't afford to buy the {} at the moment. Please come back when you have more money!".format(customerRequest))

                           
         


tryNbuy()
