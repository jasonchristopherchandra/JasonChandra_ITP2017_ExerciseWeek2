ingredients_added = []
import time
while True:

    ingredients_names = [
    "bun",
    "patty",
    "cheese",
    "tomato",
    "onion",
    "pickles",
    "mayo",
    "tomato sauce"
    ]

    ingredients_stock = {
    "bun" : 50,
    "patty" : 100,
    "cheese" : 50,
    "tomato" : 50,
    "onion" : 50,
    "pickles" : 50,
    "mayo" : 50,
    "tomato sauce" :50
    }

    ingredients_price = {
    "bun" : 2 ,
    "patty" : 5,
    "cheese" : 3,
    "tomato" : 2,
    "onion" : 2,
    "pickles" : 1,
    "mayo" : 1,
    "tomato sauce" : 1
    }

    print("Welcome! Here is a list of ingredients!:")
    for ingredients,price in ingredients_price.items():
        print(ingredients.title() + ": $" + str(price))

    shop_state = input("Is the shop open?(Y/N)")
    burger_number = int(input("How many burgers?"))

    if ingredients_stock["bun"] - burger_number < 0:
        print("Your order exceeds our stock!")
        break

    if shop_state.lower() == "n":
        print("Sorry we are closed!")
        break

    if ingredients_stock["bun"] == 0:
        print("Sorry we are out of stock!")

    ingredients_stock["bun"] = ingredients_stock["bun"] - burger_number
    ingredients_stock["patty"] = ingredients_stock["patty"] - burger_number
    order_price = burger_number*7
    while True:
        Q_additional = str(input("Additional Topping?(Y/N)"))
        if Q_additional.lower() == "y":
            toppings_addedtemp = str(input("What topping would you like?"))
            if toppings_addedtemp.lower() in ingredients_price:
                ingredients_added.append(toppings_addedtemp.title())
                order_price = order_price + (burger_number * ingredients_price[toppings_addedtemp.lower()])
                ingredients_stock[toppings_addedtemp.lower()] = ingredients_stock[toppings_addedtemp.lower()] - burger_number
            else:
                print("Error, ingredient not found!")
        else:
            break

    print("The final cost is: $" + str(order_price))
    print("Here is your order: ")
    if ingredients_added == []:
        print(print(str(burger_number) + " Burgers"))
    else:
        print(str(burger_number) + " Burgers with" + str(ingredients_added))
    print("Ingredients left: " + str(ingredients_stock))
    time.sleep(5)
