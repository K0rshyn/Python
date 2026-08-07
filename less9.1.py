n = int(input("Введите число N: "))
ch = list(map(int, input(f'Введите через пробел {n} числа(чисел): ').split()))
ch_list = set(ch)
print(len(ch_list))