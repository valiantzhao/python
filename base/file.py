# -*- coding:utf-8 -*-
with open('file.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

filename = 'file.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
