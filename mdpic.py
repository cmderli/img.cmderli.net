import os
URL = 'https://img.cmderli.net/流浪地球2/'
f = open('out.md', 'w+', encoding='utf-8')
filedir = input('file:>')
for root,dir,files in os.walk(filedir):
    for file in files:
        if file[len(file)-4::] == '.jpg':
            name = file
            print(name)
            md = f'![{file[:-4:]}]({URL}{file})'
            print(md)
            f.write(md + '\n')
