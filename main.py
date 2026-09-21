
from shop import open_shop
from forest import enter_forest

print("Welcome to play bear game")
choice = input("Choose: ")
if(choice == "1"):
    enter_forest()
elif(choice == "2"):
    open_shop()
elif choice == "q":
    print("Goodbye!")
    