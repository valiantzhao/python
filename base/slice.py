players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[1:])

for plaer in players[:3]:
    print(plaer.title())

plaers1 = players[:]
print(plaers1)
