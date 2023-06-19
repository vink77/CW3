import json
import datetime

#количество последних операций
#number_of_lastoperation = 150


#Получаем данные из файла

def get_data():
    with open("operations.json", encoding='utf-8') as f:
        dataf = json.loads(f.read())
    return dataf

def last_executed_list(date, number):
    #Получение списка последних №number операций
    execut_list =[]
    for item in date:
        if item.get('state') == 'EXECUTED':
            execut_list.append(item)
    return execut_list[:number]

def sort_list(execut_list):
    # сортировка списка "EXECUTTED" по дате
    sorting = sorted(execut_list, key = lambda x: x["date"],reverse = True)
    return sorting

def mask_card(card):
    # Маскировка номера счета/карты
    if "Счет" in card:
        out_num = f"Счет **{card[-4:]}"
    else:
        space = card.rfind(' ')
        out_num = card[0:space+5]+' '+card[space+5:space+7]+'*'*2+' '+'*'*4+' '+card[-4:]
    return out_num


def output(list_execut):
    for item in list_execut:
# Преобразование строки в объект datetime
        date_string = datetime.datetime.strptime(item['date'],'%Y-%m-%dT%H:%M:%S.%f')

# Преобразование объекта datetime в строку
        print(f"{date_string.day}.{date_string.month}.{date_string.year}  {item['description']}")
        if 'from' in item.keys():
            print(f"{mask_card(item['from'])} -> {mask_card(item['to'])}")
        else:
            print(f"{mask_card(item['to'])}")
        print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']} \n")
    return True

