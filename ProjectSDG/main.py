import sys, time
import sqlite3

koneksi = sqlite3.connect('./basisdata.db')
kursor = koneksi.cursor()
kursor.execute('''
        CREATE TABLE IF NOT EXISTS data_nutrisi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            usia INTEGER,
            tinggi REAL,
            berat REAL,
            jenis_kelamin TEXT,
            kalori REAL,
            bmr REAL,
            protein REAL,
            lemak REAL,
            karbohidrat REAL,
            bmi REAL
        )
    ''')
koneksi.commit()

""" MENAMPILKAN MENU"""
def show_menu(): 
    print("\n")
    print("----------- MENU UTAMA ----------")
    print("[1] Menghitung Kebutuhan Nutrisi")
    print("[2] Pelacakan Asupan Makanan")
    print("[3] Laporan Harian")
    print("[4] Keluar")

    menu = int(input("PILIH MENU> "))
    print("\n")
    if menu == 1:
        utama()
    elif menu == 2:
        pelacakan_asupan()
    elif menu == 3:
        laporan_harian()    
    elif menu == 4:
        print("Terima kasih banyak!\n\nShoutout kepada Sdr. Bima Mukhlisin Bil Sajjad karena sudah membantu programmer untuk mempelajari sqlite.\nTerima kasih juga kepada semua anggota yang sudah terlibat dalam pengembangan program ini!")
        exit()
    else:
        print("Salah pilih kocak!")
    if __name__ == "__main__":
        while(True):
            show_menu()

"""PROGRAM NOMOR 1"""
def utama():
    print("Menu [1] - Menghitung Kebutuhan Nutrisi")
    nama = input("Masukkan nama: ")
    if nama == " ":
        print("Nama tidak boleh kosong!")
        utama()
    elif nama.isdigit():
        print("Masukkan nama dengan format teks!")
        utama()
    try:
        usia = int(input("Masukkan usia: "))
        if usia < 1:
            print("Usia tidak boleh negatif!")
            return utama()
    except ValueError:
        print("Masukkan harus berupa angka!")
        return utama()  
    try:
        tinggi = float(input("Masukkan tinggi (cm): "))
        if tinggi < 1:
            print("Tinggi tidak boleh negatif!")
            return utama()
    except ValueError:
        print("Masukkan harus berupa angka!")
        return utama()  
    try:
        berat = float(input("Masukkan berat (kg): "))
        if berat < 0:
            print("Berat tidak boleh negatif!")
            return utama()
    except ValueError:
        print("Masukkan harus berupa angka!")
        return utama()  
    jenis_kelamin = input("Jenis kelamin (lk/pr): ")
    aktivitas = input("Tingkat aktivitas (rendah/sedang/tinggi): ")

    # Hitung BMR
    bmr = hitung_bmr(jenis_kelamin, berat, tinggi, usia)

    # Hitung kebutuhan kalori total
    kebutuhan_kalori = hitung_kebutuhan_kalori(bmr, aktivitas)

    # Hitung kebutuhan makro
    protein = kebutuhan_kalori * 0.15
    lemak = kebutuhan_kalori * 0.25
    karbohidrat = kebutuhan_kalori * 0.6

    # Hitung BMI
    bmi = hitung_bmi(berat, tinggi)

    # Tentukan kategori berat badan
    if bmi < 18.5:
        kategori_berat_badan = "Kurus"
    elif 18.5 <= bmi <= 25:
        kategori_berat_badan = "Normal"
    elif 25 <= bmi <= 30:
        kategori_berat_badan = "Gemuk"
    else:
        kategori_berat_badan = "Obesitas"

# Cetak hasil
    print("\nHasil Perhitungan:")
    bmr = int(bmr)
    kebutuhan_kalori = int(kebutuhan_kalori)
    protein = int(protein)
    lemak = int(lemak)
    karbohidrat = int(karbohidrat)
    bmi = int(bmi)

    hasil_akhir = ("Halo, ", nama, "!\nBMR Kamu: ", str(bmr), "\nKebutuhan Kalori Total: ", str(kebutuhan_kalori), " kal\nKebutuhan Protein: ", str(protein), " gr\nKebutuhan Lemak: ", str(lemak), " kal\nKebutuhan Karbohidrat: ", str(karbohidrat), " gr\nBMI: ", str(bmi), "\nKategori Berat Badan: ", kategori_berat_badan)
    hasil_utama(hasil_akhir)

    kursor.execute('''
        INSERT INTO data_nutrisi (nama, usia, tinggi, berat, jenis_kelamin, kalori, bmr,  protein, lemak, karbohidrat, bmi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama, usia, tinggi, berat, jenis_kelamin, kebutuhan_kalori, bmr, protein, lemak, karbohidrat, bmi))
    koneksi.commit()
    print("\n\nHitung lagi? (y/n) ")
    back = input().upper()
    if back == "Y":
        utama()
    else:
        show_menu()
    return

def hitung_bmr(jenis_kelamin, berat, tinggi, usia):
  """
  Menghitung Basal Metabolic Rate (BMR).

  Keterangan :
    jenis_kelamin: 'Laki-laki' atau 'Perempuan'
    berat: Berat badan dalam satuan kilogram(kg).
    tinggi: Tinggi badan dalam centimeter(cm).
    usia: Usia dalam satuan per tahun.
  """

  if jenis_kelamin == 'laki' or 'laki laki' or 'laki-laki' or 'lk':
    bmr = 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia)
  elif jenis_kelamin == 'perempuan' or 'pr' or 'women':
     bmr = 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia)
  else:
     print("\nKamu tidak memasukkan jenis kelamin dengan benar. Hanya ada dua jenis kelamin di dunia ini.")
     hitung_bmr()
  return bmr

def hitung_kebutuhan_kalori(bmr, aktivitas):
  """
  Menghitung kebutuhan kalori total.

  Keterangan :
    bmr: Basal Metabolic Rate.
    aktivitas: Faktor aktivitas (rendah, sedang, tinggi).

  Kembalian : Nilai BMR
  """

  faktor_aktivitas = {
      'rendah': 1.2,
      'sedang': 1.55,
      'tinggi': 1.725,
      'Rendah':1.2,
      'Sedang':1.55,
      'Tinggi':1.725
  }
  return bmr * faktor_aktivitas[aktivitas]

def hitung_bmi(berat, tinggi):
  """Menghitung Body Mass Index (BMI).

  Keterangan:
    berat: Berat badan dalam kg.
    tinggi: Tinggi badan dalam meter.

  Kembalian:
    Nilai BMI.
  """

  tinggi_meter = tinggi / 100
  bmi = berat / (tinggi_meter ** 2)
  return bmi

def hasil_utama(hasil_akhir):
    for chara in hasil_akhir:
        sys.stdout.write(chara)
        sys.stdout.flush()
        time.sleep(0.3)

"""PROGRAM 2"""

def pelacakan_asupan():
    kursor.execute('''
      CREATE TABLE IF NOT EXISTS riwayat_konsumsi (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          makanan_id INTEGER,
          porsi REAL,
          tanggal DATE,
          kalori_total REAL,
          karbohidrat_total REAL,
          protein_total REAL,
          lemak_total REAL,
          FOREIGN KEY(makanan_id) REFERENCES makanan(id)
      )
  ''')
    koneksi.commit()
    kursor.execute('''
        CREATE TABLE IF NOT EXISTS makanan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_makanan TEXT,
            kalori REAL,
            
            karbohidrat REAL,
            protein REAL,
            lemak REAL,
            porsi REAL
        )
    ''')
    print("Makanan yang tersedia dalam database :")
    koneksi.commit()
    kursor.execute(f'SELECT id, nama_makanan FROM makanan')
    semua_makanan = kursor.fetchall()    
    for index, (id, nama) in enumerate(semua_makanan, start=1):
        print(f"{index}. {nama}")
    # Minta pengguna memilih makanan
    while True:
        try:
            pilihan_user = int(input("\nMasukkan nomor makanan yang Anda makan hari ini: "))
            if pilihan_user <= 0 or pilihan_user > len(semua_makanan):
                print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")
            else:
                break
        except ValueError:
            print("Masukkan harus berupa angka!")
    kursor.execute("SELECT * FROM makanan WHERE id=?", (pilihan_user,))
    makanan_terpilih = kursor.fetchone()
   

    kalori_total = makanan_terpilih[2]
    karbohidrat_total = makanan_terpilih[3] 
    protein_total = makanan_terpilih[4] 
    lemak_total = makanan_terpilih[5] 

    kursor.execute('''
        INSERT INTO riwayat_konsumsi (makanan_id, tanggal, kalori_total, karbohidrat_total, protein_total, lemak_total)
        VALUES (?, date('now'), ?, ?, ?, ?)
    ''', (pilihan_user, kalori_total, karbohidrat_total, protein_total, lemak_total))
    koneksi.commit()
    print(f"\nInformasi nutrisi untuk {makanan_terpilih[1]}:")
    print(f"Kalori: {kalori_total:.2f} kal")
    print(f"Karbohidrat: {karbohidrat_total:.2f} gram")
    print(f"Protein: {protein_total:.2f} gram")
    print(f"Lemak: {lemak_total:.2f} gram")
  
    lanjut = input("\nIngin input makanan lagi? (y/n): ")
    if lanjut.lower() == 'y':
        pelacakan_asupan()
    else:
        show_menu()

def kesimpulan(simpulan):
    for karakter in simpulan:
        sys.stdout.write(str(karakter))
        sys.stdout.flush()
        time.sleep(0.02)

def laporan_harian():
    print("\nPilih data user untuk dibandingkan dengan makanan yang dimakan hari ini:")
    kursor.execute(f'SELECT id, nama FROM data_nutrisi')
    data_user = kursor.fetchall()    
    for index, (id, nama) in enumerate(data_user, start=1):
        print(f"{index}. {nama}")
    kursor.execute('''
        SELECT * FROM riwayat_konsumsi
        WHERE tanggal == date('now')
    ''')
    riwayat = kursor.fetchall()
    total_riwayat_kalori = 0
    for isi in riwayat:
        total_riwayat_kalori+= isi[4] 
    total_riwayat_karbo = 0
    for isi in riwayat:
        total_riwayat_karbo+= isi[5] 
    total_riwayat_protein = 0
    for isi in riwayat:
        total_riwayat_protein+= isi[6] 
    total_riwayat_lemak = 0
    for isi in riwayat:
        total_riwayat_lemak += isi[7] 
    while True:
        try:
            pilihan_user = int(input("\nMasukkan id user yang ingin Anda pilih: "))
            if pilihan_user <= 0 or pilihan_user > len(data_user):
                print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")
            else:
                break
        except ValueError:
            print("Masukkan harus berupa angka!")
    kursor.execute('''SELECT kalori FROM data_nutrisi WHERE id=?''', (pilihan_user,))
    kebutuhan_kalori = float(kursor.fetchone()[0])
    kursor.execute('''SELECT protein FROM data_nutrisi WHERE id=?''', (pilihan_user,))
    kebutuhan_protein = float(kursor.fetchone()[0])
    kursor.execute('''SELECT lemak FROM data_nutrisi WHERE id=?''', (pilihan_user,))
    kebutuhan_lemak = float(kursor.fetchone()[0])
    kursor.execute('''SELECT karbohidrat FROM data_nutrisi WHERE id=?''', (pilihan_user,))
    kebutuhan_karbohidrat = float(kursor.fetchone()[0])    
    # print(kebutuhan_kalori)
    # print(total_riwayat)
    
    print("\nBerdasarkan dari perbandingan antara user yang dipilih dan riwayat konsumsi hari ini.\nDi dapatkan hasil berupa :")
    if total_riwayat_kalori < kebutuhan_kalori:
        rk = print("- Anda perlu meningkatkan asupan kalori.")
    elif total_riwayat_kalori > kebutuhan_kalori:
        rk = print("- Anda perlu mengurangi asupan kalori.")
    else:
        rk = print("- Asupan kalori Anda sudah sesuai.")

    if total_riwayat_protein < kebutuhan_protein:
        rp = print("- Anda perlu meningkatkan asupan protein.")
    elif total_riwayat_protein > kebutuhan_protein:
        rp = print("- Anda perlu mengurangi asupan protein.")
    else:
        rp = print("- Asupan protein Anda sudah sesuai.")

    if total_riwayat_karbo < kebutuhan_karbohidrat:
        rkar = print("- Anda perlu meningkatkan asupan karbohidrat.")
    elif total_riwayat_karbo > kebutuhan_karbohidrat:
        rkar = print("- Anda perlu mengurangi asupan karbohidrat.")
    else:
        rkar = print("- Asupan karbohidrat Anda sudah sesuai.")

    if total_riwayat_lemak < kebutuhan_lemak:
        rlem = print("- Anda perlu meningkatkan asupan lemak.")
    elif total_riwayat_lemak > kebutuhan_lemak:
        rlem = print("- Anda perlu mengurangi asupan lemak.")
    else:
        rlem = print("- Asupan lemak Anda sudah sesuai.")
        show_menu()

    simpulan = "\nBerdasarkan dari perbandingan antara user yang dipilih dan riwayat konsumsi hari ini.\nDi dapatkan hasil berupa :\n",rk,rp,rkar,rlem 
    # kesimpulan(simpulan)


    

    # Tampilkan laporan nutrisi lainnya (karbohidrat, protein, lemak)

    # riwayat = kursor.fetchall()

    
# def pemantauan_kalori():

#     total_kalori_hari_ini = 0
#     total_protein_hari_ini = 0
#     total_karbo_hari_ini = 0
#     total_lemak_hari_ini = 0
#     while True:
#         nama_makanan = input("Masukkan nama makanan: ")
#         kalori_makanan = cari_makanan(nama_makanan)
#         if kalori_makanan:
#             porsi = int(input("Masukkan jumlah porsi: "))
#             total_kalori_hari_ini += hitung_kalori(nama_makanan, porsi)
#             persentase_kalori_tercapai = (total_kalori_hari_ini / target_kalori) * 100

#             total_protein_hari_ini += hitung_protein(nama_makanan, porsi)
#             persentase_protein_tercapai = (total_protein_hari_ini / target_protein) * 100

#             total_karbo_hari_ini += hitung_karbo(nama_makanan, porsi)
#             persentase_karbo_tercapai = (total_karbo_hari_ini / target_karbohidrat) * 100

#             total_lemak_hari_ini += hitung_lemak(nama_makanan, porsi)
#             persentase_lemak_tercapai = (total_lemak_hari_ini / target_lemak) * 100


#             status_kalori = evaluasi_kalori(total_kalori_hari_ini)
#             status_protein = evaluasi_kalori(total_protein_hari_ini)
#             status_karbo = evaluasi_kalori(total_karbo_hari_ini)
#             status_lemak = evaluasi_kalori(total_lemak_hari_ini)
#             print("\n--------------------------------------------------")

#             print("\nTotal kalori hari ini:", int(total_kalori_hari_ini)," kal")
#             print("Persentase kalori tercapai:", int(persentase_kalori_tercapai), "%")
#             print("Status:", status_kalori)

#             print("\nTotal protein hari ini:", int(total_protein_hari_ini)," gr")
#             print("Persentase protein tercapai:", int(persentase_protein_tercapai), "%")
#             print("Status:", status_protein)

#             print("\nTotal karbohidrat hari ini:", int(total_karbo_hari_ini), " gr")
#             print("Persentase karbohidrat tercapai:", int(persentase_karbo_tercapai), "%")
#             print("Status:", status_karbo)

#             print("\nTotal lemak hari ini:", int(total_lemak_hari_ini)," kal")
#             print("Persentase lemak tercapai:", int(persentase_lemak_tercapai), "%")
#             print("Status:", status_lemak)
#             print("--------------------------------------------------")

#         else:
#             print("Makanan tidak ditemukan")
            

#         lanjut = input("\nIngin input makanan lagi? (y/n): ")
#         if lanjut.lower() != 'y':
#             break
pesan = """\nSelamat Datang di
┓┏    •  ┳  •  ┳┳┓  ┓       ┏┓    ┏┓
┣┫┏┓┏┓┓  ┃┏┓┓  ┃┃┃┏┓┃┏┏┓┏┓  ┣┫┏┓┏┓┏┛
┛┗┗┻┛ ┗  ┻┛┗┗  ┛ ┗┗┻┛┗┗┻┛┗  ┛┗┣┛┗┻• 
                              ┛     
Oleh : Keysha, Naufalda, Azura, Alran """ #tidak bisa di skip

def typewriter(pesan):
    for karakter in pesan:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.03)

masukan_pesan = input("Tekan 1 untuk memulai.\n")

# show_menu()
if masukan_pesan == "1":
    typewriter(pesan)
    show_menu()
else:
    print("Kamu tidak menekan 1, aq ngambek.")

