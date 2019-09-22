with open('referat.txt', 'r', encoding='utf-8') as new_file:
    volume = new_file.read()
    print(f'Всего букв в файле: {len(volume)}')
    print(f'Всего слов в файле: {len(volume.split())}')
    new_volume = volume.replace('.', '!')
    new_volume = new_volume.replace('\n', '')

with open('referat2.txt', 'w', encoding='utf-8') as my_new_file:
    my_new_file.write(new_volume)