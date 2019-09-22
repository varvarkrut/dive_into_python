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
        self.path = x.path

    def write(self, text_to_write):
        f = open(self.path, 'a')
        f.write(text_to_write)
        f.close()

    def read(self):
        f = open(self.path, 'r')
        b = f.read()
        f.close()
        return b
