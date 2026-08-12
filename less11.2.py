import collections
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

def get_pet(ID):
    """Возвращает информацию о питомце по ID или False, если ID не существует."""
    return pets.get(ID, False)

def get_suffix(age):
    """Возвращает правильное окончание для возраста (год, года, лет)."""
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
        return "года"
    else:
        return "лет"

def pets_list():
    """Выводит список всех питомцев с их ID."""
    if not pets:
        print("Список питомцев пуст.")
        return
    for pid, pet_info in pets.items():
        for name, details in pet_info.items():
            print(f"ID: {pid}, Имя: {name}, Вид: {details['Вид питомца']}, "
                  f"Возраст: {details['Возраст питомца']}, Владелец: {details['Имя владельца']}")

def create():
    """Создаёт новую запись о питомце с автоматическим увеличением ID."""
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец добавлен с ID {new_id}")

def read(ID):
    """Выводит информацию о питомце в читаемом формате."""
    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден.")
        return

    name = list(pet.keys())[0]
    details = pet[name]
    species = details["Вид питомца"]
    age = details["Возраст питомца"]
    owner = details["Имя владельца"]
    suffix = get_suffix(age)

    print(f'Это {species} по кличке "{name}". Возраст питомца: {age} {suffix}. Имя владельца: {owner}')

def update(ID):
    """Обновляет информацию о питомце (можно изменить имя, вид, возраст, владельца или все сразу)."""
    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден.")
        return

    name = list(pet.keys())[0]
    details = pet[name]

    print("Текущие данные:")
    print(f"Имя: {name}")
    print(f"Вид: {details['Вид питомца']}")
    print(f"Возраст: {details['Возраст питомца']}")
    print(f"Владелец: {details['Имя владельца']}")

    choice = input("Что хотите обновить? (имя, вид, возраст, владелец, все): ").strip().lower()

    if choice == "имя":
        new_name = input("Введите новое имя: ")
        data = pet.pop(name)          # удаляем старый ключ, сохраняем данные
        pet[new_name] = data
    elif choice == "вид":
        new_species = input("Введите новый вид: ")
        details["Вид питомца"] = new_species
    elif choice == "возраст":
        new_age = int(input("Введите новый возраст: "))
        details["Возраст питомца"] = new_age
    elif choice == "владелец":
        new_owner = input("Введите новое имя владельца: ")
        details["Имя владельца"] = new_owner
    elif choice == "все":
        new_name = input("Введите новое имя: ")
        new_species = input("Введите новый вид: ")
        new_age = int(input("Введите новый возраст: "))
        new_owner = input("Введите новое имя владельца: ")
        pet.pop(name)                # удаляем старую запись
        pet[new_name] = {
            "Вид питомца": new_species,
            "Возраст питомца": new_age,
            "Имя владельца": new_owner
        }
    else:
        print("Неверный выбор.")
        return

    print("Данные обновлены.")

def delete(ID):
    """Удаляет запись о питомце по ID."""
    if ID in pets:
        del pets[ID]
        print(f"Питомец с ID {ID} удалён.")
    else:
        print("Питомец с таким ID не найден.")

# Основной цикл программы
while True:
    command = input("\nВведите команду (create, read, update, delete, list, stop): ").strip().lower()

    if command == "stop":
        break
    elif command == "create":
        create()
    elif command == "read":
        try:
            pid = int(input("Введите ID питомца: "))
        except ValueError:
            print("ID должно быть числом.")
            continue
        read(pid)
    elif command == "update":
        try:
            pid = int(input("Введите ID питомца: "))
        except ValueError:
            print("ID должно быть числом.")
            continue
        update(pid)
    elif command == "delete":
        try:
            pid = int(input("Введите ID питомца: "))
        except ValueError:
            print("ID должно быть числом.")
            continue
        delete(pid)
    elif command == "list":
        pets_list()
    else:
        print("Неизвестная команда. Попробуйте снова.")