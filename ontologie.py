class Vehicul:
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni):
        self.model = model
        self.greutate = greutate
        self.viteza = viteza
        self.culoare = culoare
        self.an_fabricatie = an_fabricatie
        self.dimensiuni = dimensiuni  # (L, l, h)

    def afisare(self):
        print(f"Model: {self.model}, Greutate: {self.greutate}kg, "
              f"Viteza: {self.viteza}km/h, Culoare: {self.culoare}, "
              f"An: {self.an_fabricatie}, Dimensiuni: {self.dimensiuni[0]} x {self.dimensiuni[1]} x {self.dimensiuni[2]} m")
    def porneste(self):
        print(f"{self.model} a pornit.")

    def opreste(self):
        print(f"{self.model} s-a oprit.")
        
    def accelereaza(self, plus):
        self.viteza += plus
        print(f"{self.model} accelereaza la {self.viteza} km/h.")

    def franeaza(self, minus):
        self.viteza = max(0, self.viteza - minus)
        print(f"{self.model} franeaza la {self.viteza} km/h.")

    def vopseste(self, culoare_noua):
        self.culoare = culoare_noua
        print(f"{self.model} a fost vopsit în {self.culoare}.")
        
    def setGreutate(self, greutate_noua):
        self.greutate = greutate_noua
        print(f"Greutatea noua a {self.model} este {self.greutate} kg.")

    def varsta(self, an_curent=2025):
        return an_curent - self.an_fabricatie

    def volumTotal(self):
        L, l, h = self.dimensiuni
        return L * l * h
    
    def esteClasic(self, an_limita=1980):
        return self.an_fabricatie < an_limita
    
    def timpDeplasare(self, distanta):
        if self.viteza == 0:
            return print("Vehiculul stationeaza.")
        return distanta / self.viteza
    

v1=Vehicul("Dacia Logan", 1200, 180, "Alb", 2015, (4.3, 1.7, 1.5))
print("\n\n----VEHICUL----\n")
v1.afisare()

v1.accelereaza(20)
v1.franeaza(50)
v1.vopseste("rosu")
print(f"Varsta vehiculului: {v1.varsta()} ani")
print(f"Volumul total al vehiculului: {v1.volumTotal()} metri cubi")

class Masina(Vehicul):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 motorizare, nr_usi, putere, transmisie, cutie_viteze, caroserie, volum_portbagaj):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni)
        self.motorizare = motorizare
        self.nr_usi = nr_usi
        self.putere = putere
        self.transmisie = transmisie
        self.cutie_viteze = cutie_viteze
        self.caroserie = caroserie
        self.volum_portbagaj = volum_portbagaj
        
    def afisare(self):
        super().afisare()
        print(f"Motorizare: {self.motorizare}, Nr. usi: {self.nr_usi}, Putere: {self.putere}CP, "
              f"Transmisie: {self.transmisie}, Cutie viteze: {self.cutie_viteze}, "
              f"Caroserie: {self.caroserie}, Volum portbagaj: {self.volum_portbagaj}L")
    
    def schimbaViteza(self, treapta):
        print(f"{self.model} a schimbat in treapta {treapta}.")
        
    def tuning(self, cai_putere):
        self.putere += cai_putere
        print(f"{self.model} a fost tunat la {self.putere} CP.")
        
    def clima(self, temperatura):
        print(f"Clima setata la {temperatura} grade Celsius in {self.model}.")
        
    def modifCaroserie(self, noua_caroserie):
        self.caroserie = noua_caroserie
        print(f"Caroseria {self.model} a fost modificata in {self.caroserie}.")
        
    def schimbaCutia(self, noua_cutie):
        self.cutie_viteze = noua_cutie
        print(f"Cutia de viteze a {self.model} a fost schimbata in {self.cutie_viteze}.")
        
    def schimbaTransmisia(self, noua_transmisie):
        self.transmisie = noua_transmisie
        print(f"Transmisia {self.model} a fost schimbata in {self.transmisie}.")
        
    def performanta(self):
        scor = self.putere / self.greutate
        if scor > 0.15:
            return "Performanta acestei masini este una sportiva."
        elif scor > 0.1:
            return "Performanta acestei masini este una medie."
        else:
            return "Performanta acestei masini este una slaba."
        
m1 = Masina("BMW M3", 1600, 250, "Negru", 2020, (4.7, 1.9, 1.4),
             "Benzina", 4, 480, "Spate", "Automata", "Sedan", 480)
print("\n\n----MASINA----\n")
m1.afisare()
m1.tuning(50)
print(m1.performanta())
m1.clima(22)
m1.schimbaViteza(3)
m1.modifCaroserie("Coupe")
m1.schimbaCutia("manuala")
m1.schimbaTransmisia("integrala")


class MasinaElectrica(Masina):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 motorizare, nr_usi, putere, transmisie, cutie_viteze, caroserie, volum_portbagaj, 
                 capacitate_baterie, nivel_baterie, autonomie):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                         motorizare, nr_usi, putere, transmisie, cutie_viteze, caroserie, volum_portbagaj)
        self.capacitate_baterie = capacitate_baterie #capacitate totala in kWh
        self.nivel_baterie = nivel_baterie #capacitatea actuala in %
        self.autonomie = autonomie #km     
        
    def afisare(self):
        super().afisare()
        print(f"Capacitate baterie: {self.capacitate_baterie}kWh, Baterie curenta: {self.nivel_baterie}%, "
              f"Autonomie: {self.autonomie}km")

    def baterieActuala(self): #capacitatea actuala in kwh
        return self.capacitate_baterie * (self.nivel_baterie / 100) #ex: 4000 * 0.8

    def incarcare(self, kwh):
        baterie = self.baterieActuala()
        if (baterie + kwh) <= self.capacitate_baterie:
            baterie += kwh
            return baterie
        else:
            print("Bateria este deja incarcata.")

    def autonomieParcurs(self, viteza): #autonomia scade in functie de viteza
        if viteza <= 0:
            return 0
        elif viteza > 120:
            return self.autonomie * 0.7
        else:
            return self.autonomie
        
    def consumBaterie(self):
        return round(self.capacitate_baterie / self.autonomieParcurs(self.viteza),1) #ex: 4000 / 500 = 8 kWh/km

    def poateParcurgeBaterie(self, distanta):
        return distanta * self.consumBaterie() <= self.baterieActuala()

    def consumRutaBaterie(self, distanta):  #consumul total pe baza unei distante prestabilite
        return round(distanta * self.consumBaterie(), 2)  

ev1 = MasinaElectrica("Tesla Model 3", 1625, 225, "Alb", 2021, (4.7, 1.8, 1.4),
                      "Electrica", 4, 283, "Spate", "Automata", "Sedan", 425,
                      4000, 80, 500)
print("\n\n----MASINA ELECTRICA----\n")
ev1.afisare()
print(f"Baterie curenta: {ev1.baterieActuala()} kWh")
print(f"Incarcare dupa 50 kWh: {ev1.incarcare(50)} kWh")
print(f"Autonomie la 130 km/h: {ev1.autonomieParcurs(130)} km")
print(f"Consumul pe km: {ev1.consumBaterie()} kWh/km")
print(f"Poate parcurge 200 km: {ev1.poateParcurgeBaterie(200)}")
print(f"Consum pentru 200 km: {ev1.consumRutaBaterie(200)} kWh")


class MasinaCombustibil(Masina):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 motorizare, nr_usi, putere, transmisie, cutie_viteze, caroserie, volum_portbagaj,
                 tip_combustibil, capacitate_cilindrica, capacitate_rezervor, nivel_combustibil, consum_mediu):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                         motorizare, nr_usi, putere, transmisie, cutie_viteze, caroserie, volum_portbagaj)
        self.tip_combustibil = tip_combustibil
        self.capacitate_cilindrica = capacitate_cilindrica  
        self.capacitate_rezervor = capacitate_rezervor  
        self.nivel_combustibil = nivel_combustibil #litri    
        self.consum_mediu = consum_mediu 

    def afisare(self):
        super().afisare()
        print(f"Tip combustibil: {self.tip_combustibil}, Capacitate cilindrica: {self.capacitate_cilindrica}cc, "
              f"Capacitate rezervor: {self.capacitate_rezervor}L, Nivel combustibil: {self.nivel_combustibil} litri, Consum mediu: {self.consum_mediu}L/100km")
        
    def autonomie(self):
        return round(((self.nivel_combustibil / self.consum_mediu) * 100),1)  #ex: autonomie = (34L / 9L/100km) * 100
    
    def procentCombustibil(self):
        procent = round(self.nivel_combustibil / self.capacitate_rezervor * 100, 1)
        return f"{self.model} are {procent}% combustibil."
    
    def alimentare(self, litri):
        if ((self.nivel_combustibil + litri) <= self.capacitate_rezervor):
            self.nivel_combustibil += litri
            return self.nivel_combustibil
        else:
            return print("Volumul alimentarii depaseste volumul din rezervor.")
        
    def poateParcurgeLitrii(self, distanta):
        if distanta * self.consum_mediu <= self.nivel_combustibil:
            return print("Da, poate parcurge aceasta distanta.")
        else:
            return print("Nu, nu are destul combustibil pentru aceasta distanta.")
    
    def consumRutaLitrii(self, distanta):
        return round((distanta * self.consum_mediu)/100, 1)  #regula de 3 simple
    
mc1 = MasinaCombustibil("Audi A5", 1500, 120, "gri", 2023, (1.4, 2.3, 1.2), 
                        "combustibil", 5, 345, "spate", "automata", "sedan", 345, 
                        "diesel", 3100, 50, 34, 9)

print("\n\n----MASINA COMBUSTIBIL----\n")
mc1.afisare()
print("Autonomie:", mc1.autonomie(), "km")
print(mc1.procentCombustibil())
print("Nivel dupa alimentare:", mc1.alimentare(10), "litri.")
print("Poate parcurge 200 km?:"), mc1.poateParcurgeLitrii(200)
print("Consum pentru 150 km:", mc1.consumRutaLitrii(150), "litri")


class MasinaHybrid(MasinaElectrica, MasinaCombustibil):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 motorizare, nr_usi, putere, transmisie, cutie_viteze, caroserie, volum_portbagaj,
                 capacitate_baterie, nivel_baterie, autonomie,
                 tip_combustibil, capacitate_cilindrica, capacitate_rezervor, nivel_combustibil, consum_mediu):

        Masina.__init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                        motorizare, nr_usi, putere, transmisie, cutie_viteze, caroserie, volum_portbagaj)

        self.capacitate_baterie = capacitate_baterie
        self.nivel_baterie = nivel_baterie
        self.autonomie = autonomie

        self.tip_combustibil = tip_combustibil
        self.capacitate_cilindrica = capacitate_cilindrica
        self.capacitate_rezervor = capacitate_rezervor
        self.nivel_combustibil = nivel_combustibil
        self.consum_mediu = consum_mediu


    def afisare(self):
        super().afisare()

    def conduce(self, distanta):
        print(f"Incercam sa parcurgem {distanta} km...")

        consum_electric = (distanta * (self.capacitate_baterie / self.autonomie))  #baterie / autonomie = consum kWh / km

        if self.nivel_baterie >= (consum_electric / self.capacitate_baterie * 100):
            self.nivel_baterie -= (consum_electric / self.capacitate_baterie * 100)
            print(f"Parcurgerea s-a facut ELECTRIC. Baterie ramasa: {round(self.nivel_baterie,1)}%")
        else:
            print("Baterie insuficienta, trecere pe combustibil")
            consum_combustibil = (distanta * self.consum_mediu) / 100
            
            if consum_combustibil <= self.nivel_combustibil:
                self.nivel_combustibil -= consum_combustibil
                print(f"Parcurgerea s-a facut pe COMBUSTIBIL. Combustibil ramas: {round(self.nivel_combustibil,1)} L")
            else:
                print("Nu exista suficient combustibil pentru aceasta distanta.")

mh = MasinaHybrid(
    "Toyota Prius", 1400, 90, "alb", 2022, (1.5, 2.0, 1.3),
    "hibrid", 5, 120, "fata", "automata", "hatchback", 400,
    8.8, 50, 55,
    "benzina", 1800, 43, 20, 4.5
)

print("\n\n----MASINA HIBRID----\n")
mh.afisare()
mh.conduce(70)



class Avion(Vehicul):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 tip, autonomie, capacitate_combustibil, nivel_combustibil, consum, altitudine, nr_motoare, putere):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni)
        
        self.tip = tip
        self.autonomie = autonomie
        self.capacitate_combustibil = capacitate_combustibil
        self.nivel_combustibil = nivel_combustibil
        self.consum = consum #L/h
        self.altitudine = altitudine #maxima
        self.nr_motoare = nr_motoare
        self.putere = putere

    def afisare(self):
        super().afisare()
        print(f"Tip avion: {self.tip}, Motoare: {self.nr_motoare}, Putere motor: {self.putere} kN")
        print(f"Autonomie: {self.autonomie} km, Altitudine maxima: {self.altitudine} m")
        print(f"Combustibil disponibil: {self.nivel_combustibil}/{self.capacitate_combustibil} L, Consum: {self.consum} L/oră")

    def schimbaAltitudine(self, alt):
        print(f"{self.model} schimba altitudinea la {alt} m.")

    def autonomieRamasa(self):  #autonomia ramasa in functie de ce nivel de combustibil avem
        ore = self.nivel_combustibil / self.consum
        return round(ore * self.viteza , 1)

    def consumRuta(self, distanta):  #consumul total in functie de distanta
        timp_ore = distanta / self.viteza   
        return round(timp_ore * self.consum, 1)
    
    def poate_parcurge(self, distanta):
        return self.autonomieRamasa() >= distanta

    def alimentare(self, litri):
        if (self.nivel_combustibil + litri) <= self.capacitate_combustibil:
            self.nivel_combustibil += litri
            return self.nivel_combustibil
        else:
            return print("Rezervorul este plin.")


a1 = Avion("Boeing 737",41400,850,"alb",2018,(35.8, 28.9, 12.5),
    "Privat",7800,26000,8000,2500,12500,2,120                       
)

print("\n\n----AVION----\n")
a1.afisare()
a1.schimbaAltitudine(10000)
print("Autonomie ramasa:", a1.autonomieRamasa(), "km")
print("Consum pentru 2000 km:", a1.consumRuta(2000), "L")
print(a1.poate_parcurge(3000))
print("Nivel combustibil după alimentare:", a1.alimentare(3000), "L")


class AvionPrivat(Avion):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
            tip, autonomie, capacitate_combustibil, nivel_combustibil, consum, altitudine, nr_motoare, putere,
            nr_locuri,nr_pasageri,clasa):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                    tip, autonomie, capacitate_combustibil, nivel_combustibil, consum, altitudine, nr_motoare, putere)
        
        self.nr_locuri=nr_locuri
        self.nr_pasageri=nr_pasageri
        self.clasa=clasa
        
    def afisare(self):
        super().afisare()
        print(f"Numarul total de locuri: {self.nr_locuri}")
        print(f"Numarul de pasageri: {self.nr_pasageri}")
        print(f"Clasa: {self.clasa}")
        
    def imbarcarePasageri(self,nr):
        if (self.nr_pasageri + nr) <= self.nr_locuri:
            self.nr_pasageri += nr
            return self.nr_pasageri
        else:
            return print("Nu mai exista locuri disponibile.")
        
    def debarcarePasageri(self,nr):
        if nr <= self.nr_pasageri:
            self.nr_pasageri -= nr
            return self.nr_pasageri
        else:
            return print("Nu mai exista pasageri.")
                
ap1 = AvionPrivat("Boeing 342",30600,950,"gri",2024,(30.3, 20.4, 10.0),
    "Privat",6500,20000,13000,2500,12500,2,100, 10, 5, "Clasa I")

print("\n\n----AVION PRIVAT----\n")
ap1.afisare()
print("Numarul total de pasageri dupa imbarcare", ap1.imbarcarePasageri(2))
print("Numarul total de pasageri dupa debarcare: ",ap1.debarcarePasageri(4))


class AvionMarfa(Avion):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 tip, autonomie, capacitate_combustibil, nivel_combustibil, consum, altitudine,
                 nr_motoare, putere, capacitate, marfa):
        
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                         tip, autonomie, capacitate_combustibil, nivel_combustibil,
                         consum, altitudine, nr_motoare, putere)

        self.capacitate = capacitate  
        self.marfa = marfa       

    def afisare(self):
        super().afisare()
        print(f"Capacitate marfa: {self.capacitate} kg, Marfa încărcată: {self.marfa} kg")

    def incarcaMarfa(self, kg):
        if self.marfa + kg < self.capacitate:
            self.marfa += kg
            return self.marfa
        else:
            print("S-a atins capacitatea maximă de marfă.")

    def descarcaMarfa(self, kg):
        if kg <= self.marfa:
            self.marfa -= kg
            return self.marfa
        else:
            print("Nu mai exista marfa de descarcat.")

am1 = AvionMarfa("Boeing 747 Cargo",183500,900,"alb",2015,(70.6, 64.4, 19.4),
                 "cargo",8000,183380,90000,10800,13100,4,280,120000, 100000)

print("\n\n----AVION MARFA----\n")
am1.afisare()
print(f"In urma incarcarii, marfa totala este acum:", am1.incarcaMarfa(50000))
print(f"In urma descarcarii, marfa ramasa este acum: ", am1.descarcaMarfa(30000))  

class AvionPasageri(AvionPrivat, AvionMarfa):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 tip, autonomie, capacitate_combustibil, nivel_combustibil, consum, altitudine, nr_motoare, putere,
                 nr_locuri, nr_pasageri, clasa,   
                 capacitate_marfa, marfa,         
                 nr_echipa):                       

        Avion.__init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                             tip, autonomie, capacitate_combustibil, nivel_combustibil,
                             consum, altitudine, nr_motoare, putere)

    
        self.nr_locuri=nr_locuri
        self.nr_pasageri=nr_pasageri
        self.clasa=clasa
        
        self.capacitate = capacitate_marfa
        self.marfa = marfa

        self.nr_echipa = nr_echipa

    def afisare(self):
        super().afisare()
        
aps = AvionPasageri(
    "Airbus A380", 280000, 940, "alb", 2020, (72.7, 79.8, 24.1),
    "comercial", 15000, 310000, 200000, 12000, 13100, 4, 320,
    500, 350, "Business/Economy",50000, 10000,22)

print("\n----AVION PASAGERI----\n")
aps.afisare()
print("Numarul total de pasageri dupa imbarcare: ", aps.imbarcarePasageri(20))
print("Numarul total de pasageri dupa debarcare: ",aps.debarcarePasageri(150))

print(f"In urma incarcarii, greutatea totala a bagajelor este acum:", am1.incarcaMarfa(20000))
print(f"In urma descarcarii, greutatea totala ramasa a bagajelor este acum: ", am1.descarcaMarfa(5000))



class Bicicleta(Vehicul):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 lungime_cadru, latime_ghidon, transmisie, diametru_roti,
                 latime_cauciucuri, frane):
        
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni)

        self.lungime_cadru = lungime_cadru        
        self.latime_ghidon = latime_ghidon        
        self.transmisie = transmisie              
        self.diametru_roti = diametru_roti        
        self.latime_cauciucuri = latime_cauciucuri  
        self.frane = frane                        

    def afisare(self):
        super().afisare()
        print(f"Lungime cadru: {self.lungime_cadru} cm, "
            f"Latime ghidon: {self.latime_ghidon} cm, "
            f"Transmisie: {self.transmisie}, "
            f"Diametru roti: {self.diametru_roti} inch, "
            f"Latime cauciucuri: {self.latime_cauciucuri} mm, "
            f"Frane: {self.frane}")


    def timpParcurgere(self, distanta):
        if self.viteza <= 0:
            return 0
        return round(distanta / self.viteza, 2)

    def performanta(self):
        scor = 0

        if self.frane.lower() == "hidraulice":
            scor += 3
        elif self.frane.lower() == "disc":
            scor += 2
        elif self.frane.lower() == "v-brake":
            scor += 1

        try:
            viteze = int(self.transmisie)   
        except:
            viteze = 1

        if viteze >= 21:
            scor += 3
        elif viteze >= 7:
            scor += 2
        else:
            scor += 1

        return f"Scor performanta: {scor}/6"

    def adultCopil(self):
        if self.diametru_roti < 20:
            return "Potrivita pentru copil"
        elif 20 <= self.diametru_roti <= 26:
            return "Potrivita pentru adolescent"
        else:
            return "Potrivita pentru adult"

    def tipDrum(self):
        if self.latime_cauciucuri <= 30:
            return "Recomandata pentru sosea (road bike)."
        elif self.latime_cauciucuri <= 50:
            return "Recomandata pentru drumuri mixte (trekking, cross)."
        else:
            return "Recomandata pentru off-road (MTB)."

b1 = Bicicleta("Cross MTB X5",14,25,"negru",2021,(1.7, 0.6, 1.1),
               45,60,"21",29,55,"hidraulice")

print("\n\n----BICICLETA----\n")
b1.afisare()
print("Timp pentru a parcurge 10 km:", b1.timpParcurgere(10), "ore")
print(b1.performanta())
print(b1.adultCopil())
print("Tip drum:", b1.tipDrum())


class MTB(Bicicleta):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 lungime_cadru, latime_ghidon, transmisie, diametru_roti,
                 latime_cauciucuri, frane, suspensie, nivel):
        
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                         lungime_cadru, latime_ghidon, transmisie, diametru_roti,
                         latime_cauciucuri, frane)
        
        self.suspensie = suspensie  #hardtail/full/fata
        self.nivel = nivel  #incepator/intermediar/avansat


    def afisare(self):
        super().afisare()
        print(f"Suspensie: {self.suspensie}, Nivel: {self.nivel}")


    def dificultateTraseu(self):
        if self.nivel == "incepator":
            return "Potrivita pentru trasee usoare si forestiere."
        elif self.nivel == "intermediar":
            return "Potrivita pentru trasee mixte, poteci si urcari moderate."
        else:
            return "Potrivita pentru trasee tehnice, coborari si teren dificil."


    def tipMTB(self):
        if self.suspensie == "full" and self.latime_cauciucuri > 2.3:
            return "Downhill / Enduro"
        elif self.suspensie == "hardtail":
            return "Cross-Country (XC)"
        else:
            return "Trail MTB"


    def eficientaUrcare(self):
        scor = 0
        if self.suspensie == "hardtail":
            scor += 2
        if "1x" in self.transmisie:   
            scor += 1
        if self.greutate < 13:
            scor += 1
        return f"Eficienta urcare: {scor}/4"


    def eficientaCoborare(self):
        scor = 0
        if self.suspensie == "full":
            scor += 2
        if "hidraulice" in self.frane:
            scor += 1
        if self.latime_cauciucuri >= 2.2:
            scor += 1
        return f"Eficienta coborare: {scor}/4"


mtb1 = MTB("Cube Aim Pro",14,25,"negru",2023,(1.8, 0.6, 1.1),
           45,72,"Shimano 2x9",29,2.25,"disc hidraulice",
           "hardtail","intermediar")

print("\n\n----MOUNTAIN BIKE----\n")
mtb1.afisare()
print("Dificultate traseu:", mtb1.dificultateTraseu())
print("Tipul bicicletei: ", mtb1.tipMTB())
print("Eficienta Urcare: ", mtb1.eficientaUrcare())
print("Eficienta Coborare: ", mtb1.eficientaCoborare())


class BicicletaElectrica(Bicicleta):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 lungime_cadru, latime_ghidon, transmisie, diametru_roti,
                 latime_cauciucuri, frane,
                 autonomie, capacitate_baterie, nivel_baterie, timp_incarcare):

        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                         lungime_cadru, latime_ghidon, transmisie, diametru_roti,
                         latime_cauciucuri, frane)

        self.autonomie = autonomie                
        self.capacitate_baterie = capacitate_baterie 
        self.nivel_baterie = nivel_baterie #%
        self.timp_incarcare = timp_incarcare  #ore


    def afisare(self):
        super().afisare()
        print(f"Autonomie: {self.autonomie} km, "
        f"Capacitate baterie: {self.capacitate_baterie} kWh, "
        f"Nivel baterie: {self.nivel_baterie}%, "
        f"Timp incarcare: {self.timp_incarcare} ore")


    def baterieActuala(self):
        return round(self.capacitate_baterie * (self.nivel_baterie / 100), 1)


    def consum(self):
        return round(self.capacitate_baterie / self.autonomie, 1)


    def autonomieRamasa(self):
        return round(self.autonomie * (self.nivel_baterie / 100), 1)


    def consumRuta(self, distanta):
        return round(distanta * self.consum(), 2)

eb1 = BicicletaElectrica("E-Trek Power 500",22,30,"albastru",2024,(1.8, 0.6, 1.2),
                            50,65,"9 viteze",28,40,"hidraulice",80,1576,75,4)

print("\n\n----BICICLETA ELECTRICA----\n")
eb1.afisare()
print("Baterie actuala (kWh):", eb1.baterieActuala())
print("Consum kWh/km:", eb1.consum())
print("Autonomie ramasa (km):", eb1.autonomieRamasa())
print("Consum pentru 20 km (kWh):", eb1.consumRuta(20))


class MTBElectric(MTB, BicicletaElectrica):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 lungime_cadru, latime_ghidon, transmisie, diametru_roti,
                 latime_cauciucuri, frane, suspensie, nivel,
                 autonomie, capacitate_baterie, nivel_baterie, timp_incarcare):
        
        Bicicleta.__init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                     lungime_cadru, latime_ghidon, transmisie, diametru_roti,
                     latime_cauciucuri, frane)
        
        self.suspensie = suspensie
        self.nivel = nivel
        self.autonomie = autonomie                
        self.capacitate_baterie = capacitate_baterie 
        self.nivel_baterie = nivel_baterie #%
        self.timp_incarcare = timp_incarcare  #ore

    def afisare(self):
        super().afisare()
        
mtb_elec = MTBElectric("Haibike XDURO 10",24,35,"rosu",2025,(1.85, 0.65, 1.2),
                       48,70,"12 viteze",29,2.4,"hidraulice","full","avansat",
                       100,0.6,80,5)

print("\n\n----MTB ELECTRIC----\n")
mtb_elec.afisare()

print("Baterie actuala (kWh):", mtb_elec.baterieActuala())
print("Consum kWh/km:", mtb_elec.consum())
print("Autonomie ramasa (km):", mtb_elec.autonomieRamasa())
print("Consum pentru 30 km (kWh):", mtb_elec.consumRuta(30))

print("Dificultate traseu:", mtb_elec.dificultateTraseu())
print("Tip MTB:", mtb_elec.tipMTB())
print("Eficienta urcare:", mtb_elec.eficientaUrcare())
print("Eficienta coborare:", mtb_elec.eficientaCoborare())

print("Scor performanta:", mtb_elec.performanta())
print("Potrivita pentru:", mtb_elec.adultCopil())
print("Tip drum:", mtb_elec.tipDrum())
print("Timp pentru 10 km:", mtb_elec.timpParcurgere(10), "ore")


class Barca(Vehicul):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 tip,tip_propulsie, material):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni)
        self.tip = tip
        self.tip_propulsie = tip_propulsie
        self.material = material

    def afisare(self):
        super().afisare()
        print(f"Tip barca: {self.tip}, "
              f"Tip propulsie: {self.tip_propulsie}, "
              f"Material: {self.material}")

    def navigheaza(self, distanta):
        if self.viteza <= 0:
            print("Barca nu se poate deplasa.")
            return 0
        timp = round(distanta / self.viteza, 1)
        print(f"{self.model} va parcurge {distanta} km în {timp} ore.")
        return timp
    

b1 = Barca("Yamaha 500", 800, 30, "alb", 2022, (6, 2, 1.5),
            "ambarcatiune de agrement", "motor","metal")

print("\n\n----BARCA----\n")
b1.afisare()
b1.navigheaza(60)


class Caiac(Barca):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 tip, tip_propulsie, material, nr_locuri):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                         tip,tip_propulsie, material)
        self.nr_locuri = nr_locuri  

    def afisare(self):
        super().afisare()
        print(f"Numar locuri caiac: {self.nr_locuri}")

    def adaugaLoc(self, nr):
        self.nr_locuri += nr
        print(f"Numarul de locuri a fost actualizat: {self.nr_locuri}")

    def adunaVasle(self):
        return self.nr_locuri * 2

c1 = Caiac("Caiac Rapid", 50, 15, "albastru", 2023, (4, 0.8, 0.5),
               "caiac", "vasle", "plastic", 2)

print("\n\n----CAIAC----\n")
c1.afisare()
c1.adaugaLoc(1) 
print("Număr total vâsle necesare:", c1.adunaVasle())


class BarcaPescuit(Barca):
    def __init__(self, model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                 tip, tip_propulsie, material, capacitate_totala, capacitate_actuala):
        super().__init__(model, greutate, viteza, culoare, an_fabricatie, dimensiuni,
                         tip, tip_propulsie, material)
        self.capacitate_totala = capacitate_totala  
        self.capacitate_actuala = capacitate_actuala

    def afisare(self):
        super().afisare()
        print(f"Capacitate totala: {self.capacitate_totala} kg, "
              f"Capacitate actuala: {self.capacitate_actuala} kg")

    def incarcareBarca(self, kg):
        if (self.capacitate_actuala + kg) > self.capacitate_totala:
            print(f"Incărcare prea mare! Poate fi incarcata doar {self.capacitate_totala - self.capacitate_actuala} kg.")
        else:
            self.capacitate_actuala += kg
            print(f"Barca a fost încărcata cu {kg} kg. Capacitate actuala: {self.capacitate_actuala} kg.")

    def descarcareBarca(self, kg):
        if kg > self.capacitate_actuala:
            print(f"Nu exista suficienti pesti de descarcat. Se descarca {self.capacitate_actuala} kg.")
            self.capacitate_actuala = 0
        else:
            self.capacitate_actuala -= kg
            print(f"Barca a fost descarcata cu {kg} kg. Capacitate actuala: {self.capacitate_actuala} kg.")

bp1 = BarcaPescuit("Fisher 300", 400, 20, "verde", 2021, (5, 1.5, 1.2),
                    "barca de pescuit", "motor", "lemn", 300, 100)

print("\n\n----BARCA PESCUIT----\n")
bp1.afisare()

bp1.incarcareBarca(50)
bp1.incarcareBarca(160) 

bp1.descarcareBarca(30)
bp1.descarcareBarca(130)  
