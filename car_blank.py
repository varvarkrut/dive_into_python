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


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


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
    car_type = 'specmachine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


class MakeInstance:
    @classmethod
    def getting1_instance(cls, row):
        if row[0] == 'car':
            return(Car(row[1], 2, 3, 4))
        elif row[0] == 'truck':
            return(Truck(row[1],1,2,'8x3x2.5'))


def get_car_list(csv_filename):
    with open('C:\\test.csv') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                a = MakeInstance.getting1_instance(row)
                print(a.brand)
            except Exception as a:
                print(a)
    car_list = []
    return car_list


get_car_list('hi')
