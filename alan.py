a = int(input('lutfen bir deger giriniz. '))
n = int(input('lutfen bir deger giriniz. '))
toplam_alan = 0
i = 1

while i<= n :
    toplam_alan +=(a/(2**(i-1)))**2
    i += 1

print(toplam_alan) 