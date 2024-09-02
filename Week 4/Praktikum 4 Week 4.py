#Nama file: nested_if_statement.py

jenis_kelamin = "Pria" #Baris 3

umur = 20 #Baris 5

if (jenis_kelamin=="Pria"): #Baris 7 - 11
    if (umur >= 25):
        print ("Pria boleh menikah")
    else:
        print ("Pria tidak boleh menikah")
elif(jenis_kelamin=="Wanita"): #Baris 12 - 16
    if (umur >= 20):
        print ("Wanita boleh menikah")
    else:
        print ("Wanita tidak boleh menikah")
else: #Baris 17
    print ("Jenis kelamin tidak terdaftar") 
