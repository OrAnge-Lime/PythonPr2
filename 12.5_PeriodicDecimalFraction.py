# Если m, n – взаимно простые натуральные числа, причем n взаимно просто с 10 и m < n, то в
# десятичном представлении дробь m/n является чисто периодической.
# Длина ее наименьшего периода – это такое наименьшее натуральное число r, что 10r – 1 кратно n.

# Десятичное представление дроби m/n, где m, n – натуральные числа, m < n,– периодическая
# дробь, длина наименьшего периода
# которой не превосходит n – 1.


a = int(input())
s = str(1/a).split(".")[1]

n = 0
while a % 2 == 0 or a % 5 == 0:
    if a % 2 == 0:
        a = a / 2
    if a % 5 == 0:
        a = a / 5
    n += 1


res = ""
for i in range(n, s.__len__()):
    res += s[i]
    c = ""
    for j in range(i + 1, i + res.__len__() + 1):
        c += s[j]
    if res == c:
        print(res)
        break

    if res.__len__() == int(s.__len__() / 2) - 1:
        print("too long period")
        break



