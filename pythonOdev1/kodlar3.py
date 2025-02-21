#sınıflar - class
#modules
#paket yonetımı

class Human:
    name = "Dilara"
    def talk(self,sentence):
        name ="Ayşe"
        print(f"{self.name} : {sentence}")
        
        # self.name olunca = Dilara
        # sadece name olunca Ayşe olur
        self.walk() # BAŞKA BİR FONKSİYONA ERİŞİM
   
    
    
    def walk(self): 
        print("Human is walking")
        
        
        
#instance  ornek

human1 = Human()
human1.name = "Ali" #nesnenin name i değişti
#human1.talk()
human1.talk("is talking")
human1.walk()


human2 = Human()
human2.name = "Can"
human2.talk("Selam")
human2.walk()
