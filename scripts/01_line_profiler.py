import numpy
from time import sleep

@profile
def cut_vegetables(useless):
    sleep(0.2)

@profile
def cook_vegetables(useless):
    sleep(0.5)

@profile
def prepare_salad():
    sauce = numpy.random.uniform(size=1000000).sum()
    cut_vegetables(sauce)
    cook_vegetables(sauce)
    return int(sauce)


if __name__ == '__main__':
    prepare_salad()
