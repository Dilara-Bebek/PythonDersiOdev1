faiz = 1.59
vade = "36"
krediAdi= "ihtiyaç kredisi"

# print(vade +12) hatalı

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) +12)
# print(int(krediAdi)) bu inte cevrilemez

faiz = str(faiz)
print(type(faiz))

vade = input("lütfen istediğiniz vade sayısını giriniz:")
print(vade)
print(type(vade)) # şuan string
print(int(vade) +12)

#---------

vade = int(input("lütfen istediğiniz vade sayısını giriniz:"))
print(vade)
print(type(vade)) # şuan integer
vade = vade + 12

#------------------

# string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade:

print("seçtiğiniz vade sonucu ortaya çıkan vade :" + str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi = 36)) 

metin = "Merhaba {name}".format(name="Dilara")  
print(metin)

isim = "Dilara"

#f string
metin = f"Hoş geldiniz {isim}"
metin2 = f"Hoş geldiniz {3+5}"
print (metin2)


#listeler
#döngüler
#fonksiyonlar

#listeler------------------------------------
dizi = ["ihtiyaç kredisi",10,4.3,True]
print(dizi)

krediler = ["ihtiyaç kredisi","Taşıt kredisi","konut kredisi"]
print(type(krediler))

print(krediler[0]) #ihtiyaç kredisi

#print(krediler[5]) INDEX ERROR

print(len(krediler)) # length 3 elemanlı

# print(krediler[3]) INDEX ERROR

krediler.append("Özel kredi")
print(krediler)

krediler.append("Eğitim kredisi")
print(krediler)

krediler.pop() # son eleman silindi
print(krediler)

krediler.pop(0) # ilk eleman silindi
print(krediler)

krediler.append("Taşıt kredisi") # aynısını ekledik
print(krediler)

krediler.remove("Taşıt kredisi") #silindi
print(krediler) # ilk buldugunu sıldı

krediler.extend(["Y kredisi","Z kredisi"]) #birden fazla degısken eklendı
print(krediler)

#DONGULER

# FOR DONGUSU----------------------------

for i in range(10):     #0 dan 10 a kadar olan sayılar(10 dahıl degıl)
    print("xx")
    print(i)
    
print("---------------------------")

for i in range(5,10):   # 5 den 10 a kadar
               print(i)
      
    
print("---------------------------")


for i in range(0,51,10): # 0 dan 51 e kadar 10ar 10ar yaz
    print(i)
    
    
print("---------------------------")

#for i in range(0.1,0.5):
#    print(i)
        
print("---------------------------")


krediler = ["ihtiyaç kredisi","Taşıt kredisi","konut kredisi"]
for kredi in krediler:
    print(kredi) # "ihtiyaç kredisi","Taşıt kredisi","konut kredisi"


print("---------------------------")
    
for i in range(len(krediler)):
    print(i) # 0,1,2




#WHİLE DONGUSU---------------------------

#sonsuz dongu

#while True:
#    print("x")
    
i=0
while i<10:
    print("x")
    i+=1

print("y")    


while True:
    print("X")
    break

print( "*********************")

#1. dongu
i=0
while i<len(krediler):
    if krediler[i] == "konut kredisi":
        break
    print(krediler[i])
    i+=1
    
    
#yukarıdakıyle farkı var  
i=0
while i<len(krediler):
    print(krediler[i])
    i+=1    
    if krediler[i] == "konut kredisi":
        break
    
    
#definition define
def calculate():
    print(100-20)
    
calculate()    
calculate()    # 3 kere 80 yazdı    
calculate()       
    
    
    
def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
  
calculateWithParams(50,10)    
calculateWithParams(100,30)
 


def sayHello(name):
    print(f"Merhaba {name}")
    
sayHello("Dilara")   
sayHello("Ayşe")   

#void - geriye deger dondurmez
def calculatePrice(price,discount):
    print( price - discount)

# geriye deger dondurur
def calculateAndReturn(price,discount):
    return price - discount


yeniFiyat = calculateAndReturn(200, 40)
print(yeniFiyat)







