pets = dict()
name = input('Введите имя питомца: ')
view = input(f'Введите вид {name}: ')
age = int(input(f'Введите возраст {name}: '))
owner = input('Введите имя хозяина: ')
if age % 10 == 1 and age %100 != 11:
    age_suffix = "год"
elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
    age_suffix = "года"
else:
    age_suffix = "лет"
info = {
    'Вид питомца': view,
    'Возраст питомца': f"{age} {age_suffix}", # придумайте каким образом сюда внести информацию,
    'Имя владельца': owner,
}
pets[name] = info
for key in pets.keys():
    print(f'Это {info['Вид питомца']} по кличке {key}. Его возраст : {info["Возраст питомца"]}. Имя владельца: {info["Имя владельца"]}')