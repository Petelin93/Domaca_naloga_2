print("Zdravo! To je pretvornik enot, ki pretvori kilometre v milje.")

#Uporabniški vnos kilometrov
while True:
    kilometri = float(input("Vnesite vrednost v kilometrih (Vnašaj samo števila!): "))
    print(kilometri, "kilometer/ov je enako", 0.621371*kilometri, "milji/am")
    vprasanje = input("Želite opraviti novo pretvorbo? (da/ne): ")
    if vprasanje.lower() != "d" and vprasanje.lower() != "da":
        break
