a = input("Введите строку без пробелов: ")
if a[::1] == a[::-1]:
    print('Yes')
else:
    print("No")
