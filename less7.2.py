a = input("Введите строку: ")
if len(a) <= 1000:
    print(' '.join(a.split()))
else:
    print("Слишком длинная строка.")