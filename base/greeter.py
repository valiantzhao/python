# -*- coding:utf-8 -*-
def get_formatted_name(firt_name, lanst_name):
    """fefe"""
    full_name = firt_name+' '+lanst_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    f_name = input("Firt name:")
    if f_name == "q":
        break
    l_name = input("Last name:")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello,"+formatted_name+"!")
