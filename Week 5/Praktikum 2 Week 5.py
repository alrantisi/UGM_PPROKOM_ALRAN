awal = int(input("Masukan saldo awal\t:"))
sisa = awal #bila tidak ada pengeluaran
while (True):
    pengeluaran = int(input("Masukan pengeluaran hari ini (1 untuk keluar): "))
    if pengeluaran == 1 : #untuk berhenti   
        print("Sisa saldo = ", sisa) #sisa bila di berhentikan
        break
    sisa = sisa - pengeluaran
    if sisa <0:
        print("Saldo tidak cukup")
        print("Sisa saldo ", sisa+pengeluaran)
        break
