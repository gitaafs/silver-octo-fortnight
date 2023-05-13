import random

a = 1
b = 99
hads = random.randint(a,b)
print(hads)

vaziat = input()

while vaziat != 'd':
    if vaziat == 'k':
        b = hads
        hads = random.randint(a,b)
        print(hads)
        vaziat = input()
    elif vaziat == 'b':
        a = hads 
        hads = random.randint(a,b)
        print(hads)
        vaziat = input()

