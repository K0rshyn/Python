N = int(input("Введите число N:"))
kol = 0
i = 0
while i < N :
    x = int(input("Введите целое число:"))
    i += 1
    if x == 0:
        kol += 1
print("Количество чисел, равных нулю:", kol)