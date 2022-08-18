import json
try:
    with open('file.txt', 'r+', encoding='utf-8') as file:
        stat = []
        profit = {}
        sred_profit = {}
        b = 0
        prof = 0
        i = 3
        for line in file:
            name, firm, viruchka, izderjki = line.split()
            total = int(viruchka) - int(izderjki)
            if total >= 0:
                prof = prof + total
            else:
                i -= 1
            profit[name] = total
        stat.append(profit)
        if i != 0:
            b = prof / i
            sred_profit['средняя прибыль'] = round(b)
            stat.append(sred_profit)
        else:
            print('Все компании работают в убыток')
        print(stat)
    with open('file.json', 'a+', encoding='utf-8') as json_file:
        json.dump(stat, json_file)
except FileNotFoundError:
    print('Файл данных не найден!')
