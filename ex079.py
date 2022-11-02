num = []
for c in range(1, 6):
    n = int(input('digite um número: '))
    if n in num:
        num.remove(n)
    num.append(n)
num.sort()
print(num)