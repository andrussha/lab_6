'''
Робота світлофора для водіїв запрограмована таким чином: на початку кожної
години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини -
жовтий, протягом двох хвилин - червоний, протягом трьох хвилин - знову зелений і т. д.
Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що
минув з початку чергової години і визначає сигнал якого кольору горить для водіїв в цей
момент.
Постлович А.С. 122-В
'''
while True:
    while True:
        try:
            t = int(input('Input time: '))
            b = t % 6
            if b < 4:
                print('Green')
            elif b == 4:
                print('Yellow')
            else:
                print('Red')
            break
        except ValueError:
            print('Only numbers')
    key = input('Again? If yes - input 1, if no - 2: ')
    if key == '1':
        continue
    else:
        print('Bye')
        break