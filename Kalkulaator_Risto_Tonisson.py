
import math #importime math teeki


class calc: #loome calc pea klassi
    def liitmine(self, arv1, arv2): #defineerime liitmise meetodi
        return arv1 + arv2 #tagastame arv1 ja arv2 summa
    
    def lahutamine(self, arv1, arv2): #defineerime lahutamise meetodi
        return arv1 - arv2   #tagastame arv1 ja arv2 vahe
    
    def korrutamine(self, arv1, arv2): #defineerime korrutamise meetodi
        return arv1 * arv2 #tagastame kahe arvu korrutise
    
    def jagamine(self, arv1, arv2): #defineerime jagamis meetodi
        if arv2 != 0: #kontrollitakse et jagatav pole 0
            return arv1 / arv2 #kui arv pole 0 tagastatakse jagatise vastus
        else:
            print("ei saa nulliga jagada") #kui jagatav on 0 siis väljastatakse vea kood
            
    def astendamine(self,arv1, astendaja):  #astendamise meetod
        return arv1 ** astendaja  #tagastatakse astendamine
    
    def ruutjuur(self, arv): #defineerime ruutjuure meetodi
        return math.sqrt(arv) # tagastatakse arvu ruutjuure
    
class protsentcalc(calc): # Defineerib klassi nimega 'protsentcalc', mis pärib klassi 'calc'
    def protsent(self, arv1, arv2): #defineerime protsendi meetodi
        return (arv1 * arv2) / 100   #tagastatakse protsent
    
    
    
if __name__ == "__main__":  # Kui skripti käivitatakse otse, siis käivitatakse järgnev kood
    kalkulaator = protsentcalc() 
    
    tehe = input("sisestage: '+', '-', '*', '/', '**', 'sqrt', või protsent: ") #kasutaja input valimiseks mis tehet soovitakse teha
   
   
    # Järgnevad if/elif-lause blokid kontrollivad, millist tehet kasutaja soovib teha, ja väljastatakse see
    if tehe in('+', '-', '*', '/'):
        arv1 = float(input("esimene arv: "))
        arv2 = float(input("teine arv: "))
        
        if tehe == '+':
            vastus = kalkulaator.liitmine(arv1, arv2)
            
        elif tehe == '-':
            vastus = kalkulaator.lahutamine(arv1, arv2)
            
        elif tehe == '*':
            vastus = kalkulaator.korrutamine(arv1, arv2)
            
        elif tehe == '/':
            vastus = kalkulaator.jagamine(arv1, arv2)
            
    elif tehe == '**':
        arv1 = float(input("arv: "))
        arv2 = float(input("arv: "))
        vastus = kalkulaator.korrutamine(arv1, arv2)
        
    elif tehe == 'sqrt':
        arv = float(input("arv: "))
        vastus = math.sqrt(arv)
        
    elif tehe == 'protsent':
        arv1 = float(input("arv1: "))
        arv2 = float(input("arv2: "))
        vastus = kalkulaator.protsent(arv1, arv2)
        
    else:
        print("ei saa teha") # Kui tehe ei vasta ühelegi tingimusele, prinditakse veateade
        
print(f"vastus: {vastus}")   # Lõpuks prinditakse tehte tulemus

    
    
