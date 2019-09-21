'''Классы и наследование
Как правило задачи про классы носят не вычислительный характер. Обычно нужно написать классы, которые отвечают определенным интерфейсам. Насколько удобны эти интерфейсы и как сильно связаны классы между собой, определит легкость их использования в будущих программах.

Предположим есть данные о разных автомобилях и спецтехнике. Данные представлены в виде таблицы с характеристиками. Обратите внимание на то, что некоторые колонки присущи только легковым автомобилям, например, кол-во пассажирских мест. В свою очередь только у грузовых автомобилей есть длина, ширина и высота кузова.'''


import os
import csv


class CarBase:
    car_type = 1
    photo_file_name = 1
    brand = 1
    carrying = 1

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext[1]
import os
import csv


class CarBase:
    car_type = 1
    photo_file_name = 1
    brand = 1
    carrying = 1

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            length, width, height = (float(c) for c in body_whl.split('x', 2))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


class MakeInstance:
    @classmethod
    def getting1_instance(cls, row):
        if row[0] == 'car':
            return(Car(row[1],row[3], row[5], row[2]))
        elif row[0] == 'truck':
            return(Truck(row[1],row[3],row[5],row[4]))
        elif row[0] == 'spec_machine':
            return(SpecMachine(row[1],row[3],row[5],row[6]))
        else:
            return


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                a = MakeInstance.getting1_instance(row)
                if isinstance(a,CarBase):
                    car_list.append(a)
                else:
                    a=None
            except Exception as a:
                pass
    return car_list




