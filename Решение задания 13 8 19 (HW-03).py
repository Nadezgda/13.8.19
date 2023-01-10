
ticket_number = int(input("Введите количество билетов, которые Вы хотите приобрести на мероприятие: "))
total_ticket_price = 0 # счетчик стоимости билетов
for i in range(ticket_number): # переберем вводимые данные пользователя
    i = i + 1
    age_for_ticket = int(input("Для какого возраста билет № "))
    if age_for_ticket < 18: # условия для покупки билетов
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        total_ticket_price += 990
        print('Стоимость билета: 990 руб.')
    else:
        total_ticket_price += 1390
        print('Стоимость билета: 1390 руб.')
if ticket_number > 3: # условие скидки, по кол-ву купленных билетов
    total_ticket_price = total_ticket_price - (total_ticket_price / 100 * 10)
    print(f'Сумма к оплате {total_ticket_price} с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
else:
    print(f'Сумма к оплате {total_ticket_price} руб.')
