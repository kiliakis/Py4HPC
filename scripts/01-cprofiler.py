import numpy
from time import sleep


def cut_vegetables(useless):
    sleep(0.2)


def cook_vegetables(useless):
    sleep(0.5)


def prepare_salad():
    sauce = numpy.random.uniform(size=1000000).sum()
    cut_vegetables(sauce)
    cook_vegetables(sauce)
    return int(sauce)

if __name__ == '__main__':
    prepare_salad()