"""
Задание 4. Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется
процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада. Каждый из трех банковских продуктов должен
быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и
значения процентной ставки для каждого срока. В функции необходимо
проверять принадлежность суммы вклада к одному из диапазонов и
выполнять расчет по нужной процентной ставке. Функция возвращает
сумму вклада на конец срока.

Примечание: используем функциональный подход (не ООП)
Вы можете сделать расчет без капитализации и с капитализацией

Пример без капитализации: 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11300

Пример с капитализацией (ежемесячной): 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11384.29
"""
MINIMAL_DEPOSIT = 'minimal_deposit'
MIDDLE_DEPOSIT = 'middle_deposit'
MAXIMUM_DEPOSIT = 'maximum_deposit'

DEPOSIT_PERCENTS = {
    'minimal_deposit': {
        6: 5,
        12: 6,
        24: 5,
    },
    'middle_deposit': {
        6: 6,
        12: 7,
        24: 6.5,
    },
    'maximum_deposit': {
        6: 7,
        12: 8,
        24: 7.5,
    },
}


def get_deposit_range(begin_sum):
    if 1000 < begin_sum < 10000:
        return MINIMAL_DEPOSIT
    elif 10000 <= begin_sum < 100000:
        return MIDDLE_DEPOSIT
    elif 100000 <= begin_sum < 1000000:
        return MAXIMUM_DEPOSIT


def get_deposit_persent(deposit_range, deposit_time):
    return DEPOSIT_PERCENTS[deposit_range][deposit_time]


def deposit(begin_sum, deposit_time, capitalize=False):
    deposit_range = get_deposit_range(begin_sum)
    deposit_persent = get_deposit_persent(deposit_range, deposit_time)
    if capitalize:
        end_sum = begin_sum * ((1 + (deposit_persent * 30) /
                               (100 * 365)) ** deposit_time)
    else:
        end_sum = begin_sum + \
                  ((begin_sum * deposit_persent * (deposit_time * 30) /
                    (365 * 100)))
    end_sum = round(end_sum, 2)

    return {'begin_sum': begin_sum,
            'end_sum': end_sum,
            deposit_time: deposit_persent}


if __name__ == '__main__':
    print(deposit(10000, 24))
    print(deposit(10000, 24, capitalize=True))
