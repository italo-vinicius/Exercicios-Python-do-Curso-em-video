def fatorial(num= 1, show=False):
        f = 1
        for c in range(num, 0, -1):
            if show:
                print(f'{c}', end='')
                if c > 1:
                    print(' X ', end='')
                else:
                    print(' = ', end='')
            f *= c
        return f

print(fatorial(10, True))