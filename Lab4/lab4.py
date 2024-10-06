

import math


def square_root(num):
    return math.sqrt(num)


import datetime


def current_time():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")




import my_module


def duck_foo_wrapper():
    return my_module.create_duck()





from Invoker import *


def invoke_Duck():
    my_little_honey = Duck.Duck()
    print(my_little_honey)
    my_little_honey.make_infernal()



def invoke_Capybara():
    my_another_little_honey = Capybara.Capybara()
    print(my_another_little_honey)
    my_another_little_honey.make_infernal()


def invoke_Hamster():
    litlle_ahh_warrior = Hamster.Hamster()
    print(litlle_ahh_warrior)
    litlle_ahh_warrior.make_criminal()
    litlle_ahh_warrior.inflation()

invoke_Hamster()