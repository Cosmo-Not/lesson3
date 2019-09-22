import csv

spisok =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('my_spisok.csv', 'w', encoding='utf-8', newline='') as my_file:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(my_file, fields, delimiter=';')
    writer.writeheader()
    for user in spisok:
        writer.writerow(user)