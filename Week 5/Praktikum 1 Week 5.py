awal = 1 #Baris 1
akhir = 10 #Baris 2

for angka in range(awal, akhir + 1): #Baris 4-6
    print(angka, end=' ') #mencetak angka 1-10 seperti biasa
    print(akhir + 1 - angka, end=' ') #mencetak angka 1-10 secara terbalik
