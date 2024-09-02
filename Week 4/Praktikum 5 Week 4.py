"""Buat flowchart, algoritma dan program untuk menampilkan siswa yang lulus dan
tidak lulus dari lima data siswa yang diinputkan, bila lulus, nilai ≥ 70 serta
berilah analisis dari program yang anda buat."""

siswa1 = input("Masukkan nama siswa 1 :") #Baris 5 - 14
nilai_siswa1 = int(input("Masukkan nilai {} : ".format(siswa1)))
siswa2 = input("Masukkan nama siswa 2 :")
nilai_siswa2 = int(input("Masukkan nilai {} : ".format(siswa2)))
siswa3 = input("Masukkan nama siswa 3 :")
nilai_siswa3 = int(input("Masukkan nilai {} : ".format(siswa3)))
siswa4 = input("Masukkan nama siswa 4 :")
nilai_siswa4 = int(input("Masukkan nilai {} : ".format(siswa4)))
siswa5 = input("Masukkan nama siswa 5 :")
nilai_siswa5 = int(input("Masukkan nilai {} : ".format(siswa5)))

if nilai_siswa1 >= 70: #Baris 16 - 39
    print(siswa1, "lulus anjay! Ga nyangka anjir.\n")
else:
    print(siswa1, "belum lulus. Coba lagi, bray! Selamat nambah semester.\n")

if nilai_siswa2 >= 70:
    print(siswa2, "lulus? Seriusan?\n")
else:
    print(siswa2, "gak lulus AWKWAKKkWKW. Ketebak kocak, main mulu si.\n")

if nilai_siswa3 >= 70:
    print(siswa3, "lulus? Jelas dia mah, yakali kagak lulus.\n")
else:
    print(siswa3, "gak lulus? Hah?\n")

if nilai_siswa4 >= 70:
    print(siswa4, "lulus cihuyy. Otw traktiran ni yee!\n")
else:
    print(siswa4, "disuru nyoba lagi semester depan, gapapa.\n")

if nilai_siswa5 >= 70:
    print(siswa5, "LULUS WOY LULUS! Congrats!\n")
else:
    print(siswa5, "otw jadi donatur kampus inimah.\n")
          
print("Selamat kepada seluruh siswa yang lulus!") #Baris 41
