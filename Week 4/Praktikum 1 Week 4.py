#Program Persyaratan SIM

umur = int(input("Masukan Umur Anda = ")) #Baris 3
nilai = int(input("Masukan Nilai Tes Anda = ")) #Baris 4
lulus = "Selamat Anda Berhak Mendapatkan Sim Anda" #Baris 5
gagal = "Maaf, Anda tidak berhak mendapatkan sim Anda.\nSilahkan coba lagi bulan atau tahun depan!" #Baris 6
if(umur>17) : #Baris 7 - 13
    if(nilai<60) :
        print(gagal)
    else :
        print(lulus)
else :
    print(gagal)
