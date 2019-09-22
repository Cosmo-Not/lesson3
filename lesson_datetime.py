from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "russian")

d = datetime.now()
delta = timedelta(days=1)
delta_month = timedelta(days=30)

stroka = "01/01/17 12:10:03.234567"
dt = datetime.strptime(stroka, "%d/%m/%y %H:%M:%S.%f")

print(f'Вчера было: {(d - delta).strftime("%d %b %Y")}')
print(f'Завтра будет: {(d + delta).strftime("%d %b %Y")}')
print(f'Сегодня: {d.strftime("%d %b %Y")}')
print(f'Месяц назад было : {(d - delta_month).strftime("%d %b %Y")}')

print(dt)