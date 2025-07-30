heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']
def heroMenu():
    while True:
        print("Hero Menu")
        print("1. Display Heroes\n2. Add Hero\n3. Insert Hero\n4. Remove Hero\n5. Sort Heroes")
        choice = input("Choose (1-5): ")
        match choice:
            case '1':
                print("Heroes:", heroes)
            case '2':
                heroes.append(input("Enter hero to add: "))
                print("Hero added.")
            case '3':
                name = input("Enter hero to insert: ")
                pos = int(input("Enter position: "))
                heroes.insert(pos, name) if 0 <= pos <= len(heroes) else print("Invalid position.")
                print("Hero inserted.")
            case '4':
                name = input("Hero to remove: ")
                heroes.remove(name) if name in heroes else print("Not found.")
                print("Hero removed.")
            case '5':
                heroes.sort()
                print("Sorted heroes:", heroes)
            case _:
                print("Invalid option.")        
        if input("Go next? (y to continue): ").lower() != 'y':
            print("Program ended")
            break
heroMenu()
