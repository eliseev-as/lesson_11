import collections

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        }
}

pet_age = 'Возраст питомца'


def get_pet_id():
    return int(input("Введите идентификатор питомца: "))


def get_name(pet):
    return [key for key in pet.keys()][0]


def get_info(pet):
    name = get_name(pet)
    age = pet[name][pet_age]
    print(
        f'Это {pet[name]["Вид питомца"]} по кличке "{name}". '
        f'Возраст питомца: {age} {get_suffix(age)}. '
        f'Имя владельца: {pet[name]['Имя владельца']}.'
    )


def get_pet(pet_id):
    return pets.get(pet_id, False)


def get_suffix(age):
    if age % 10 == 1 and age != 11 and age % 100 != 11:
        return "год"
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
        return "года"
    return "лет"


def pets_list():
    for k, v in pets.items():
        print(f'{k}: ', end='')
        get_info(v)


def create():
    name = input("Введите имя питомца: ")
    kind = input('Введите вид питомца: ')
    age = int(input('Введите возраст питомца: '))
    owner_name = input('Введите имя владельца: ')

    pet = {name: {'Вид питомца': kind, pet_age: age, 'Имя владельца': owner_name}}

    last = collections.deque(pets, maxlen=1)[0]

    pets[last + 1] = pet

    print(f'Новый питомец {name} успешно добавлен')


def read():
    pet_id = get_pet_id()

    pet = get_pet(pet_id)

    if pet is False:
        print(f'Питомец с идентификатором {pet_id} не найден')
    else:
        get_info(pet)


def update():
    pet_id = get_pet_id()

    pet = get_pet(pet_id)

    if pet is False:
        print(f'Питомец с идентификатором {pet_id} не найден')
    else:
        name = get_name(pet)

        updated_pet = dict()

        for k, v in pet[name].items():
            new_value = input(f'{k}: ')
            if new_value:
                updated_pet[k] = int(new_value) if k == pet_age else new_value
        pet[name].update(updated_pet)

        print(f'Питомец с идентификатором {pet_id} успешно обновлен')
        get_info(pet)


def delete():
    pet_id = get_pet_id()

    if pets.pop(pet_id, None) is None:
        print(f'Питомец с идентификатором {pet_id} не найден')
    else:
        print(f'Питомец с идентификатором {pet_id} успешно удален')


while True:
    command = input("Введите команду: ")

    if command == "stop":
        break

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    else:
        print("Неизвестная команда")

pets_list()
