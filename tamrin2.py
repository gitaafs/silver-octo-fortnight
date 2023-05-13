x = int(input())
counter = 0

for i in range(1,x):
    if x % i == 0:
        counter += 1

if counter == 1:
    print('prime')
else:
    print('not prime')

    