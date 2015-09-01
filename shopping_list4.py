shopping_list = []

def remove_item(idx):
    index = idx -1
    item = shopping_list.pop(index)
    print("Item borrado {}.".format(item))

def show_help():
    print("\nSepara cada item con una coma")
    print("\nEscribe DONE para cerrar la lista,SHOW para ver la lista actual, REMOVE para borrar un item y HELP para ver este mensaje")

def show_list():
    count = 1
    print("\nEsta es tu lista:")
    for item in shopping_list:
        print("{}: {}".format(count,item))
        count += 1

print("Dame una lista de cosas que quieras comprar.")
show_help()

while True:
    new_stuff = input("> ")

    if new_stuff == "DONE":
        print("Aqui esta tu lista: ")
        show_list()
        break

    elif new_stuff == "HELP":
        show_help()
        continue

    elif new_stuff == "SHOW":
        show_list()
        continue

    elif new_stuff == "REMOVE":
        show_list()
        idx = input("¿Que item quieres remover?")
        remove_item(int(idx))
        continue

    else:
        new_list = new_stuff.split(",")
        index = input("Agregar esto en algun lugar en especifico? "
        " o dame un numero, actualmente hay {} en la lista".format(len(shopping_list)))
        if index:
            spot= int(index) - 1
            for item in new_list:
                shopping_list.insert(spot,item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
