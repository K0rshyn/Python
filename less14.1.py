my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
def rec(n, st = 0):
    if st == len(n):
        print("Конец списка!")
        return
    print(n [st])
    rec( n, st + 1 )
print(rec(my_list))