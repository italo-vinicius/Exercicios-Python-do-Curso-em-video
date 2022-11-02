import random

while True:
    computer = random.randint(1,5)
    ask = int(input('chuta ae: '))
    if computer == ask:
        print('parabens')
        break
    else:
        print('tente again')