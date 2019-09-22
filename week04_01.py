'''В этом задании вам нужно создать интерфейс для работы с файлами. Класс File должен поддерживать несколько необычных операций.

Класс инициализируется полным путем.

obj = File('/tmp/file.txt')

Класс должен поддерживать метод write.

obj.write('line\n')

Объекты типа File должны поддерживать сложение.

first = File('/tmp/first')
second = File('/tmp/second')
new_obj = first + second


В этом случае создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.

Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.

for line in File('/tmp/file.txt'):
  ...
  
 
И наконец, при выводе файла с помощью функции print должен печататься его полный путь, переданный при инициализации.

obj = File('/tmp/file.txt')

print(obj)
'/tmp/file.txt'


Опишите свой класс в скрипте и загрузите на платформу.'''




import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        f = open(self.path, 'r')
        b = f.read()
        b=b.split('\n')
        print(f'b={b}')
        f.close()
        b=iter(b)
        return b
    def __str__(self):
        return(self.path)
    def __add__(self, obj):
        x = File(os.path.join(tempfile.gettempdir(), 'example.txt'))
        x.write(self.read())
        x.write(obj.read())
        return x

    def write(self, text_to_write):
        f = open(self.path, 'a')
        f.write(text_to_write)
        f.close()

    def read(self):
        f = open(self.path, 'r')
        b = f.read()
        f.close()
        return b
