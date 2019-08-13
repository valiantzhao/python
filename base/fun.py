# -*- coding:utf-8 -*-
def greet_user(names):
    for name in names:
        msg = "Hello,"+name.title()+"!"
        names[1] = "test"
        print(msg)


def greet_user1(*params):
    print(params)


def greet_user2(**params):
    for key, value in params.items():
        print(value)


usernames = ['haha', 'hehe', 'hiahia']
# greet_user(usernames)
# 副本
greet_user(usernames[:])
print(usernames)

greet_user2(a=1, b=2)
