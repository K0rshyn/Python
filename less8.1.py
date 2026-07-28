n = int(input("Введите число N: "))
pos = []
if n >= 1 and n<=10000:
    for i in range(n):
        x = int(input("Введите число: "))
        pos.append(x)
    pos.reverse()
    print (pos)
else:
    print("Введите число N менее 10000.")