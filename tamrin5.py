sen = int(input())
b2 = 0

while sen != int(-1):
    #get values from users
    x = sen
    sen = int(input())
    if sen == int(-1):
        break 
    y = sen
    if b2 > y :
        y = b2
    else:
        y = sen
    if y > x : 
        b1 = y 
        b2 = x
    else:
        b2 = y
        b1 = x
    sen = int(input())
    if sen == int(-1):
        break
    z = sen
    #chek the big 1 and big 2 (compare values)
    if x > z > y :
        b1 = x
        b2 = z
    elif x > y > z :
        b1 = x
        b2 = y
    elif z > x > y :
        b1 = z
        b2 = x  
    elif z > y > x : 
        b1 = z
        b2 = y
    elif y > x > z :
        b1 = y 
        b2 = x
    elif y > z > x :
        b1 = y
        b2 = z
    sen = b1
    


print(b1,b2)

    

        

