#tabe tedad maghsommon alayh 
def ma_counter(x):
    counter = 0
    for i in range(1,x+1):
        if x % i == 0:
            counter += 1
    return counter

tedad = 0
vrdk = 0
# نکته : زمانی که متغیرها رو خارج از حلقه تعریف کنی و داخل حلقه تغییر بدی
#  همه چیز رواله البته یکم خنگ شدم سرش ولی  سعی کن الگوریتم رو بهتر درک کنی و بنویسی ایولللللل
# الگوریتم خوب نوشتن هنر هست

for i in range(1,21):
    vrd = int(input())
    cnt = ma_counter(vrd)
    if cnt > tedad:
        tedad = cnt
        vrdk = vrd
    elif tedad < cnt:
        tedad = tedad
        vrdk = vrdk
    elif tedad == cnt:
        tedad = tedad
        vrdk = max(vrdk,vrd)

print(vrdk,tedad)
    

    

        






        









    







    








    

