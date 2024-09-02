sekon = int(input("Masukkan jumlah detik :"))

#rumus hari
a = 60  * 60 * 24 
hari = sekon//a 

#rumus jam
b = a * hari 
c = sekon - b 
jam = c//(60*60) 

#rumus menit
d = jam*(60*60)
e = c - d
menit = e//60

#rumus detik
detik = sekon%60

print ("Hari, jam, menit, dan detik hari ini adalah :", (hari),"hari ", (jam), "jam ", (menit), "menit ", (detik), "detik")
