import random

suit_pengguna = input("Pilih batu, gunting, atau kertas? ") #Baris 3 berisi permintaan input kepada user
pilihan = ["batu", "kertas", "gunting"] #Baris 4 berisi opsi suit yang dapat kita ambil
suit_komputer = random.choice(pilihan) #Baris 5 berfungsi untuk mendeklarasikan opsi suit dari komputer dengan mengacaknya
print(f"\nKamu memilih {suit_pengguna}, Komputer memilih {suit_komputer}.\n") #Baris 6 mencetak opsi yang kita ambil dan komputer ambil

if suit_pengguna == suit_komputer:#Baris 8 - 9
    print(f"Dua pemain memilih {suit_pengguna}. Imbang, cuy!")
elif suit_pengguna == "batu": #Baris 10 - 14
    if suit_komputer == "gunting":
        print("Batu lawan gunting, kamu menang! Guntingnya patah, wak.")
    else:
        print("Kertas lawan batu, komputer menang! Batunya dibungkus kertas, wak.")
elif suit_pengguna == "kertas": #Baris 15 - 19
    if suit_komputer == "batu":
        print("Kertas lawan batu, kamu menang! Batunya dibungkus kertas, wak.")
    else:
        print("Gunting lawan kertas, komputer menang! Kertasnya dipotong, wak.")
elif suit_pengguna == "gunting": #Baris 20 - 24
    if suit_komputer == "kertas":
        print("Gunting lawan kertas, kamu menang! Kertasnya dipotong, wak.")
    else:
        print("Batu lawan gunting, komputer menang! Guntingnya patah, wak.")
