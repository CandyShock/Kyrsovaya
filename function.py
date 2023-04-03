

def dict_sort(dict):
    """функция получает словарь и сортирует его по пораметру executed
    затем сортирует по дате"""
    items = []
    for operate in dict:
        if operate.get('state') == 'EXECUTED':
            items.append(operate)
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items

def refactor_date(str_date):
    """функция меняет формат даты на более понятный"""
    d = str_date[:10].split('-')
    return d[2] + '.' + d[1] + '.' + d[0]



def format_data(item):
    """функция берет и выводит нужные данные, в нужнйо последовтельности и формате"""
    str_date = refactor_date(item.get('date'))
    description = item.get('description')
    from_ = blurring_card(item.get('from'))
    to = blurring_card(item.get('to'))
    summ = item.get('operationAmount').get('amount')
    curr = item.get('operationAmount').get('currency').get('name')

    if from_:
        from_ = from_ + ' -> '



    return f'{str_date} {description}\n{from_}{to}\n{summ} {curr}'


def blurring_card(card):
    """функция скрывает часть данных для карты или счета"""
    if not card:
        return ''
    card_data = card.split(' ')
    if card_data[0] == 'Счет':
        return card_data[0] + ' **' + card_data[1][-4:]
    card_number = card_data[-1][:4] + ' ' + card_data[-1][4:6] + '** **** ' + card_data[-1][-4:]
    return " ".join(card_data[:-1]) + ' ' + card_number

    return 'card_data'


