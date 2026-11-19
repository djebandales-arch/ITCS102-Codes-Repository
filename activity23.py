shonen = []
korean = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input("Do you watch or read anime? yes/no ".lower())

    if ans == "yes":
        print("what kind of anime do you watch or read? ")
        print(" 1-Shonen \n 2-Korean \n 3-Isekai \n 4-adventure \nfantasy".upper())

        choice = int(input("Input --> "))

        if choice == 1:
            print("SHONEN")
            title = input("Please input the title of the anime: ")
            shonen.append(title)
            print("list of shonen")
            print(shonen)
            cont = input("DO YOU WANT TO CONTINUE? ")
            if cont == "yes":
                continue
            dele=input("Do you want to delete an anime title? ")
            if dele == "yes":
                delete = input("Enter the title you want to delete: " )
                korean.remove(delete)
                print(shonen)
        elif choice == 2:
            print("KOREAN")
            title = input("Please input the title of the anime: ")
            korean.append(title)
            print("list of korean")
            print(korean)
            cont = input("DO YOU WANT TO CONTINUE? ")
            if cont == "yes":
                        continue
            dele=input("Do you want to delete an anime title? ")
            if dele == "yes":
                delete = input("Enter the title you want to delete: " )
                korean.remove(delete)
                print(korean)
        elif choice == 3:
                    print("ISEKAI")
                    title = input("Please input the title of the anime: ")
                    isekai.append(title)
                    print("list of isekai")
                    print(isekai)
                    cont = input("DO YOU WANT TO CONTINUE? ")
                    if cont == "yes":
                                continue
                    dele=input("Do you want to delete an anime title? ")
                    if dele == "yes":
                        delete = input("Enter the title you want to delete: " )
                        isekai.remove(delete)
                        print(isekai)
        elif choice == 4:
                    print("ADVENTURE")
                    title = input("Please input the title of the anime: ")
                    adventure.append(title)
                    print("list of adventure")
                    print(adventure)
                    cont = input("DO YOU WANT TO CONTINUE? ")
                    if cont == "yes":
                                continue
                    dele=input("Do you want to delete an anime title: ")
                    if dele == "yes":
                        delete = input("Enter the title you want to delete: " )
                        adventure.remove(delete)
                        print(adventure)
        elif choice == 5:
                    print("FANTASY")
                    title = input("Please input the title of the anime: ")
                    fantasy.append(title)
                    print("list of fantasy")
                    print(fantasy)
                    cont = input("DO YOU WANT TO CONTINUE? ")
                    if cont == "yes":
                                continue
                    dele=input("Do you want to delete an anime title? ")
                    if dele == "yes":
                        delete = input("Enter the title you want to delete: " )
                        fantasy.remove(delete)
                        print(fantasy)
        else:
                break
    else:print("invalid")