while True:
    choice = input("Choose: ").lower()

    if(choice == "1"):
        enter_forest()
    elif(choice == "2"):
        open_shop()
    elif choice == "q":
        print("Goodbye!")
        break
