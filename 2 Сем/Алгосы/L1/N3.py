from random import shuffle
data = [[('6', '♠'), ('7', '♠'), ('8', '♠'), ('9', '♠'), ('10', '♠'), ('J', '♠'), ('Q', '♠'), ('K', '♠'), ('T', '♠')],
        [('6', '♣'), ('7', '♣'), ('8', '♣'), ('9', '♣'), ('10', '♣'), ('J', '♣'), ('Q', '♣'), ('K', '♣'), ('T', '♣')],
        [('6', '♥'), ('7', '♥'), ('8', '♥'), ('9', '♥'), ('10', '♥'), ('J', '♥'), ('Q', '♥'), ('K', '♥'), ('T', '♥')],
        [('6', '♦'), ('7', '♦'), ('8', '♦'), ('9', '♦'), ('10', '♦'), ('J', '♦'), ('Q', '♦'), ('K', '♦'), ('T', '♦')]]
vivod = [[('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*')],
        [('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*')],
        [('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*')],
        [('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*'), ('*', '*')]]
all_cards, all_close_cards, close_cards, all_cards_find, cards_find = [],  [], [('*', '*')]*9, [], [('X','X')]
for i in data:
    a = i
    shuffle(a)
    all_cards.append(a)
all_cards_find.append([cards_find*9, cards_find*9, cards_find*9, cards_find*9])
all_close_cards.append([close_cards, close_cards, close_cards, close_cards])
all_close_cards = all_close_cards[0]
all_cards_find = all_cards_find[0]
final = all_close_cards
all_close_cards = all_cards

print(all_cards)
for i in range(4):
    for j in range(9):
        print(all_cards[i][j], i, j)
for i in all_cards:
            print(i)

while all_close_cards != final:
    str_x_1 = int(input('Введите номер первой строки: '))
    str_y_1 = int(input('Введите номер первой карты: '))
    str_x_2 = int(input('Введите номер второй строки: ')) 
    str_y_2 = int(input('Введите номер второй карты: ')) 
    print(all_cards[str_x_1][str_y_1])
    print(all_cards[str_x_2][str_y_2])
    if (all_cards[str_x_1][str_y_1][0]) == (all_cards[str_x_2][str_y_2][0]):
        (all_cards[str_x_1][str_y_1]) = [('X','X')]
        (all_cards[str_x_2][str_y_2]) = [('X','X')]
        (vivod[str_x_1][str_y_1]) = [('X','X')]
        (vivod[str_x_2][str_y_2]) = [('X','X')]
        for i in vivod:
            print(i)
    else:
        for i in vivod:
            print(i)
        
