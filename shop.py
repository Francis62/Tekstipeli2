def open_shop():
    print("Welcome to the shop!")
    buy = input("What would you like to buy?\nA.apple\nB.Gun\nC.Jerky\nCostumer: ").lower()
    if buy == "a":
        print('"An apple a day keeps the doctor away."')
    if buy == "b":
        print("Be careful of the bear.")
    if buy == "c":
        print("Now you have a snack for later.")
    else:
        print("See you again!")    