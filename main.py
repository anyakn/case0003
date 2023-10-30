'''
Кнопова Анна 70
Балан Каролина 45
Шилкова Ульяна 45
'''


from turtle import *
import ru_local as ru


def get_num_hexagons():
    n = input(ru.num_ans1)
    k = 0
    while k < 1:
        try:
            if 4 <= int(n) <= 20:
                k += 1
                return int(n)
            else:
                print(ru.num_ans2)
                n = input(ru.num_ans1)
        except ValueError:
            print(ru.num_ans2)
            n = input(ru.num_ans1)


num = get_num_hexagons()
d = 500 / (num + 0.5)
side = (3**0.5 / 3) * d


def get_color_choice():
    colors = [ru.color_1, ru.color_2, ru.color_3, ru.color_4,
              ru.color_5, ru.color_6]
    codes = [ru.code_1, ru.code_2, ru.code_3, ru.code_4, ru.code_5, ru.code_6]

    print(ru.color_ans1, ru.color_1, ru.color_2, ru.color_3, ru.color_4,
          ru.color_5, ru.color_6, sep='\n')

    first_one = ''
    chosen_one = input(ru.color_ans2).lower()

    while first_one == '':
        for idx in range(6):
            if chosen_one in colors:
                idx = colors.index(chosen_one)
                first_one = codes[idx]
            else:
                print(chosen_one, ru.color_ans3)
                chosen_one = input(ru.color_ans4).lower()

    second_one = ''
    chosen_two = input(ru.color_ans2).lower()

    while second_one == '':
        for idx in range(6):
            if chosen_two in colors:
                idx = colors.index(chosen_two)
                second_one = codes[idx]
            else:
                print(chosen_two, ru.color_ans3)
                chosen_two = input(ru.color_ans4).lower()

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
