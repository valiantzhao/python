abc = {'color': 'green', 'points': 5}
print(abc['color'])
print(abc['points'])

abc['newdic'] = 0
abc['newdic1'] = 1

print(abc)

abc['color'] = 'red'

print(abc)

del abc['newdic1']

print(abc)

favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python', }
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title()
      + ".")

for key, value in abc.items():
    print("\nkey:"+key)
    print("vallue:"+str(value))
