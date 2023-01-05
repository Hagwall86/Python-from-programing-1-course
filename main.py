import os
import sys
from deflist import menu, intro
clear = lambda: os.system('cls')

# The lists I use in the menus.
mainList = ["Dricka", "Godis", "Kaffe", "Kassa", "Avsluta"]
drinks = ["Fanta", "Pepsis", "Cola", "Vatten"] #, "Tillbaka"]
candy = ["Snickers", "Mars", "Chokladkaka", "Klubba"] #,"Tillbaka"]
coffee = ["Svart kaffe", "Svart kaffe med socker", "Latte", "Espresso"] #,"Tillbaka"]

# Shoppingcart list
cartItems = []
# Checks how much the user are shopping for.
cartTotal = 0

# This is the Welcome screen. This one runs first. (Men ville inte att den skulle funka på det sättet den gör. Den skulle vara själv och inte tillsammans med menyn.)
intro()
# Main function that's I run through another def to get the numbers in the beginning.
def mainMenu():
    menu(mainList)
mainMenu()

# adds the item thats given from the user and returns the price.
def addItem(itemName, itemPrice):
    cartItems.append(itemName)
    return (itemPrice)



# Mainmenu loop
while True:
    # Try/ except loop with if
    try:
        option = int(input("Gör ett val"))
        if option <= 5:
            if option == 1:
                clear()
                print("***Drickan kostar 10kr/st***")
                menu(drinks)
                # This one are collecting what the user are putting in the cart and convert it to uppercase to print.
                cartTotal += addItem(input("Skriv namnet på det du vill ha: ").upper(), 10)
                # Takes the prices and collect them and print out how much the user have shoppt for.
                cartSummary = dict((item, cartItems.count(item)) for item in cartItems)
                print("Belopp: ", cartSummary)
                print(cartTotal)
            elif option == 2:
                clear()
                print("***Godiset kostar 15kr/st***")
                menu(candy)
                cartTotal += addItem(input("Skriv namnet på det du vill ha: ").upper(), 15)
                cartSummary = dict((item, cartItems.count(item)) for item in cartItems)
                print("Belopp: ", cartSummary)
                print(cartTotal)
            elif option == 3:
                clear()
                print("***Kaffet kostar 20kr/st")
                menu(coffee)
                cartTotal += addItem(input("Skriv namnet på det du vill ha: ").upper(), 20)
                cartSummary = dict((item, cartItems.count(item)) for item in cartItems)
                print("Belopp: ", cartSummary)
                print(cartTotal)
            elif option == 4:
                print("****KASSA****")
                cartSummary = dict((item, cartItems.count(item)) for item in cartItems)
                print("Du har lagt till dessa varor : ", cartSummary)
                print("Och ditt totala belopp blev: ", cartTotal, " Kr ")
                print("Tack för du handlade hos oss på Kiosken ha en bra dag och välkommen åter")
                input()
                break
                exit()
            elif option == 5:
                break

            mainMenu()
        elif option >= 5:
            print("fel")
            print("här vill vi inte va")
# The except only takes up if the user have written letters instead of numbers.
    #
    except:
        print("Du ska bara använda siffror")

