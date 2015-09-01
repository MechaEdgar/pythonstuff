shopping_list = []

def show_help():
    print("Que deberiamos comprar de la tienda?")
    print("Ingresa DONE para cerrar la lista")
    print("Ingresa SHOW para mostrar la lista")
    print("Ingresa HELP para mostrar esta pantalla.")

def add_to_list(item):
    shopping_list.append(item)
    print("Added! list has {} items.".format(len(shopping_list)))

def show_list():
    print("Aqui esta tu lista: ")
    for item in shopping_list:
        print(item)

show_help()

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        show_list()
        break
    elif new_item == 'HELP':
        show_help()
        continue
        
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)
    continue

show_list
