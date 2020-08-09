"""
Задание 5*.Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции
реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего. Например, при сроке вклада в 6 месяцев
пополнение происходит в течение 4 месяцев. Вложенная функция возвращает
сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.

Примечание: используем функциональный подход (не ООП)
Пример: 10 тыс на 24 мес, пополнение - по 100
chargable_deposit(10000, 24, 100)
к концу срока: 13739.36
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


def chargable_deposit(begin_sum, deposit_time, refill_amount, capitalize=False):
    deposit_range = get_deposit_range(begin_sum)
    deposit_persent = get_deposit_persent(deposit_range, deposit_time)

    def get_refill_profit(current_sum, deposit_persent):
        return current_sum * deposit_persent * 30 / (365 * 100)

    current_sum = begin_sum
    profit = 0

    for month in range(deposit_time):
        profit += get_refill_profit(current_sum, deposit_persent)
        if month < deposit_time - 1:
            current_sum += refill_amount

    end_sum = current_sum + profit
    end_sum = round(end_sum, 2)

    return {'begin_sum': begin_sum,
            'end_sum': end_sum,
            deposit_time: deposit_persent}


if __name__ == '__main__':
    print(chargable_deposit(10000, 24, 100))
