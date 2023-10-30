from turtle import *


def get_num_hexagons():
    n = input('Введите количество шестиугольников, располагаемых в ряд, в диапазоне от 4 до 20: ')
    k = 0
    while k < 1:
        try:
            if 4 <= int(n) <= 20:
                k += 1
                return int(n)
            else:
                print('Введено некорректное значение. Повторите попытку: ')
                n = input('Введите количество шестиугольников, располагаемых в ряд, в диапазоне от 4 до 20: ')
        except ValueError:
            print('Введено некорректное значение. Повторите попытку: ')
            n = input('Введите количество шестиугольников, располагаемых в ряд, в диапазоне от 4 до 20: ')


num = get_num_hexagons()
d = 500 / (num + 0.5)
side = (3**0.5 / 3) * d

def get_color_choice():
    colors = ['оранжево-красный', 'кораловый', 'кадетский-синий', 'тёмно-аспидный синий',
              'бледно-зелёный', 'светло-коричневый']
    codes = ['orangered', 'coral', 'cadetblue', 'darkslategray', 'powderblue', 'moccasin']

    print('Допустимые цвета заливки:', 'оранжево-красный', 'кораловый', 'кадетский-синий', 'тёмно-аспидный синий',
          'бледно-зелёный', 'светло-коричневый', sep='\n')

    first_one = ''
    chosen_one = input('Пожалуйста, выберете цвет: ').lower()

    while first_one == '':
        for idx in range(6):
            if chosen_one in colors:
                idx = colors.index(chosen_one)
                first_one = codes[idx]
            else:
                print(chosen_one, 'не является верным значением')
                chosen_one = input('Пожалуйста, повторите попытку: ').lower()

    second_one = ''
    chosen_two = input('Пожалуйста, выберете цвет: ').lower()

    while second_one == '':
        for idx in range(6):
            if chosen_two in colors:
                idx = colors.index(chosen_two)
                second_one = codes[idx]
            else:
                print(chosen_two, 'не является верным значением')
                chosen_two = input('Пожалуйста, повторите попытку: ').lower()

    return first_one, second_one


first_color, second_color = get_color_choice()


def draw_hexagon(x, y, side_len, colour):
    speed(-1)
    pu()
    goto(x, y)
    pd()
    fillcolor(colour)
    begin_fill()
    rt(30)

    for i in range(6):
        fd(side_len)
        rt(60)


    end_fill()
    pu()
    lt(30)



wdth = 250

for k in range(num):
    if k % 2 == 0:
        lngth = -250 + d
    else:
        lngth = -250 + d/2

    for l in range(num):
        if k % 4 == 0 or k % 4 == 1:
            if l % 2 == 0:
                draw_hexagon(lngth, wdth, side, first_color)
            else:
                draw_hexagon(lngth, wdth, side, second_color)
        else:
            if l % 2 == 0:
                draw_hexagon(lngth, wdth, side, second_color)
            else:
                draw_hexagon(lngth, wdth, side, first_color)

        lngth += d
    wdth -= 1.5 * side



hideturtle()
done()
