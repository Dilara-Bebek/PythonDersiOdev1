 print("kodlamio")

baslik = "taşıt kredisi"
print(baslik)

# string = metinsel ifade
baslik = "ihtiyaç kredisi"
print(baslik)

# int, integer = tam sayı

vade = 36
vade2 = "36"

# float,decimal,double
aylikOdeme = 200.50

# bool,boolean = true ve false
yuksekListeMi = False
ekvade = 10

# matematiksel operatörler
#+
print( 5+5)
print( vade + 12)
print(vade + ekvade )
print(36 + 6)

#-
print(5 -5)
print(vade -12)
print(vade - ekvade)
print(36 -6)

# *
print( 5*5)
print(vade*5)
print(vade*ekvade)
print(10*10)

# / 
print(5/5)
print(vade/2)
print(vade/ekvade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimliFİyat = fiyat -20

print(yeniVade)
print(indirimliFİyat)

# mod operatoru %

print(10%2)
print(vade % 5)
print(vade % ekvade)
print(30 % 10)


# mantıksal operatörler
print(1==1)
print( 1==2)

print(1>2)
print(3>1)

print(1>1)
print(1>= 1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print(1!=1)
print(1!=2)

# or - and
# or = veya
print(1 > 2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)

print(1>2 and 5>2 and 3>2)

print(2>1 or 1>2 and 3>2)


# karar yapıları
# if - else

sayi1 =10
sayi2 = 15

# sayi1>sayi2 ise 1 yaz
#condition

#indent
if sayi1>sayi2 :
    print("sayi1 sayi2 den küçüktür")
    print("hala if blogunun icerisinde")

elif sayi1 == sayi2 :
    print("iki sayı eşittir")

else:
    print("sayi1 sayi2 den büyüktür")

print("burası if blogunun dısıdır.")
  
print("---------------------------------------")  

#indent 2    
if sayi1>sayi2 :
    print("sayi1 sayi2 den küçüktür")

if sayi1 == sayi2 :
    print("iki sayı eşittir")

else:
    print("sayi1 sayi2 den büyüktür")
    
    
    
















