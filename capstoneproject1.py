# project capstone modul 1
# nama : Muhamad Fajar Latiful Habib
# Topic : Buat program untuk data pasien rumah sakit dengan CRUD

datapasien = [
    {
        "nik"  : 2501478,
        "nama" : "aliya",
        "jk"  : "perempuan",
        "umur" : 3,
        "status gizi" : "obesitas"
    },
    {
        "nik"  : 2501479,
        "nama" : "daffa",
        "jk"  : "laki-laki",
        "umur" : 5,
        "status gizi" : "gizi lebih"
    },
    {
        "nik"  : 2501480,
        "nama" : "siti",
        "jk"  : "perempuan",
        "umur" : 2,
        "status gizi" : "resiko gizi lebih"
    },
    {
        "nik"  : 2501481,
        "nama" : "indra",
        "jk"  : "laki-laki",
        "umur" : 3,
        "status gizi" : "gizi baik"
    }
]

def menampilkandatapasien ():
    print("=" * 80)
    print("Daftar Data Pasien Rumah Sakit Mursada Jaya")
    print("=" * 80)
    print('Index\t| Nik    \t|  Nama  \t| Jenis Kelamin\t| Umur\t|  Status Gizi')
    print("=" * 80)
    for i in range(len(datapasien)):
        print(f"{i}\t| {datapasien[i]['nik']}\t|  {datapasien[i]['nama']}    \t| {datapasien[i]['jk']}  \t| {datapasien[i]['umur']}\t|  {datapasien[i]['status gizi']}")
    print("=" * 80) 


def menudata():
    while True:
        data = input(''' 
    ======== |Data Pasien Rumah Sakit Mursada Jaya| ========
    ========================================================                 
                     
    list menu :
    1. menampilkan data pasien rumah sakit
    2. menampilkan daftar data pasien rumah sakit tertentu
    3. kembali ke menu utama
                     
    Pilih Menu (1 - 3) :  ''')
        
        if(data == "1"):
            tampil = input("Apakah Anda Ingin Melihat Data Pasein (ya/tidak) ? ")
            if(tampil.lower() == "ya"):
                menampilkandatapasien()
            if(tampil.lower() == "tidak"):
                continue
        elif(data == "2"):
            while True:
                indexpasien = int(input("Masukan Index Data Pasien Tertentu: "))
                if indexpasien >= len(datapasien) or indexpasien < 0:
                    print("Index data pasien yang anda masukan tidak ada")
                else:
                    print("Daftar Data Pasien")
                    print("=" * 80)
                    print('Index\t| Nik    \t|  Nama  \t| Jenis Kelamin\t| Umur\t|  Status Gizi')
                    print("=" * 80)
                    pasien = datapasien[indexpasien]
                    print(f"{indexpasien}\t| {pasien['nik']}\t|  {pasien['nama']}    \t| {pasien['jk']}  \t| {pasien['umur']}\t|  {pasien['status gizi']}")
                    break  # Keluar dari loop setelah berhasil menampilkan data
        elif(data == "3"):
            tampil = input("Apakah Anda Yakin Ingin Keluar Dari Program Data Pasien (ya/tidak) ? ")
            if(tampil.lower() == "ya"):
                break  # Keluar dari loop untuk kembali ke menu utama
            if(tampil.lower() == "tidak"):
                continue # Balik ke program data pasien
        else :
            print("Pilihan Menu Tidak Valid. Silakan Pilih Menu (1 - 3)")

def menambahdata():
    while True:
        datatambah = input(''' 
    ======== |Data Pasien Rumah Sakit Mursada Jaya| ========
    ========================================================
                                       
    list menu :
    1. menambah daftar baru data pasien rumah sakit
    2. keluar dari menambah daftar data pasien rumah sakit
                           
    Pilih Menu (1 - 2) :  ''')
        
        if(datatambah == "1"):
            nikpasien = int(input("Masukan NIK Pasien = "))

            for pasien in datapasien:
                if(pasien['nik'] == nikpasien):
                    print("NIK yang anda masukan sudah tersedia")
                    break
            else:
                namapasien = input("Masukan Nama Pasien : ").lower()
                jeniskelamin = input("Masukan Jenis Kelamin : ").lower()
                umurpasien = int(input("Masukan Umur Pasien : "))
                gizipasien = input("Masukan Status Gizi Pasien : ").lower()
                save = input("Apakah Anda Yakin Ingin Menyimpan Data Pasien Ini (ya/tidak) ? ")
                if(save.lower() == "ya"):
                    datapasien.append({
                        'nik' : nikpasien,
                        'nama' : namapasien,
                        'jk' : jeniskelamin,
                        'umur' : umurpasien,
                        'status gizi' : gizipasien
                    })
                    print("Data Berhasil Disimpan")
                if(save.lower() == "tidak"):
                    print("Data gagal ditambah")
                    continue
    
        elif(datatambah == "2"):
            tampil = input("Apakah Anda Yakin Ingin Keluar Dari Program Data Pasien (ya/tidak) ? ")
            if(tampil.lower() == "ya"):
                break  # Keluar dari loop untuk kembali ke menu utama
            if(tampil.lower() == "tidak"):
                continue # Balik ke program data pasien
        else :
                print("Pilihan Menu Tidak Valid. Silakan Pilih Menu (1 - 2)")

def menghapusdata():
    while True :
        datahapus = input(''' 
    ======== |Data Pasien Rumah Sakit Mursada Jaya| ========
    ======================================================== 
                                     
    list menu :
    1. menghapus daftar data pasien rumah sakit
    2. keluar dari menghapus daftar data pasien rumah sakit
                          
    Pilih Menu (1 - 2) :  ''')
        
        if(datahapus == "1"):
            menampilkandatapasien()
            nik = int(input("Masukan nik yang ingin dihapus : "))
            for pasien in datapasien:            
                if(pasien['nik'] == nik) :
                    delete = input("Apakah anda yakin ingin menghapus data ini(ya/tidak) : ")
                    if(delete.lower() == "ya"):
                         datapasien.remove(pasien)
                         print("Data pasien berhasil dihapus")
                    elif(delete.lower() == "tidak"):
                        print("Tidak jadi menghapus data")
                    break
            else : 
                print("NIK tidak ditemukan didalam data pasien rumah sakit")     

        elif(datahapus == "2"):
            tampil = input("Apakah Anda Yakin Ingin Keluar Dari Program Menghapus Data Pasien (ya/tidak) ? ")
            if(tampil.lower() == "ya"):
                break  # Keluar dari loop untuk kembali ke menu utama
            if(tampil.lower() == "tidak"):
                continue # Balik ke program data pasien
        else :
                print("Pilihan Menu Tidak Valid. Silakan Pilih Menu (1 - 2)")           

def updatedata():
    while True :
        dataupdate = input(''' 
    ======== |Data Pasien Rumah Sakit Mursada Jaya| ========
    ========================================================            
    list menu :
    1. mengupdate daftar data pasien rumah sakit
    2. keluar dari mengupdate daftar data pasien rumah sakit
                           
    Pilih Menu (1 - 2) :  ''')
        
        if(dataupdate == "1"):
            menampilkandatapasien()
            updatedataindex = int(input("Masukan data(index) yang ingin diupdate : "))
            if updatedataindex >= len(datapasien) or updatedataindex < 0:
                    print("Index data pasien yang anda masukan tidak ada")
            else :
                    index = datapasien[updatedataindex]
                    print('Index\t| Nik    \t|  Nama  \t| Jenis Kelamin\t| Umur\t|  Status Gizi')
                    print("=" * 80)
                    print(f"{updatedataindex}\t| {index['nik']}\t|  {index['nama']}    \t| {index['jk']}  \t| {index['umur']}\t|  {index['status gizi']}")
   
                    update = input("Apakah anda yakin ingin mengupdate data ini (ya/tidak) ?")
                    if (update == "ya"):
                        kolom = input("Masukan nama kolom yang ingin diupdate (NIK/NAMA/JENIS KELAMIN/UMUR/STATUS GIZI) : ").lower()
                        if (kolom == "nik"):
                            nik = int(input("Masukan NIK : ")) 
                            simpan = input("Simpan Update (ya/tidak) : ").lower()
                            if (simpan == "ya"):                
                                datapasien[updatedataindex]['nik'] = nik
                                print("Data berhasil diperbarui.")
                                menampilkandatapasien()
                            elif(simpan == "tidak"):
                                print("Data gagal diupdate")
                        elif (kolom == "nama"):
                            nama = input("Masukan Nama : ").lower()
                            simpan = input("Simpan Update (ya/tidak) : ").lower()
                            if (simpan == "ya"):                
                                datapasien[updatedataindex]['nama'] = nama
                                print("Data berhasil diperbarui.")
                                menampilkandatapasien()
                            elif(simpan == "tidak"):
                                print("Data gagal diupdate")
                        elif (kolom == "jk"):
                            jk = input("Masukan Jenis Kelamin : ").lower()
                            simpan = input("Simpan Update (ya/tidak) : ").lower()
                            if (simpan == "ya"):                
                                datapasien[updatedataindex]['jk'] = jk
                                print("Data berhasil diperbarui.")
                                menampilkandatapasien()
                            elif(simpan == "tidak"):
                                print("Data gagal diupdate")
                        elif (kolom == "umur"):
                            umur = int(input("Masukan Umur : "))
                            simpan = input("Simpan Update (ya/tidak) : ").lower()
                            if (simpan == "ya"):                
                                datapasien[updatedataindex]['umur'] = umur
                                print("Data berhasil diperbarui.")
                                menampilkandatapasien()
                            elif(simpan == "tidak"):
                                print("Data gagal diupdate")
                        elif (kolom == "status gizi"):
                            gizi = int(input("Masukan Status Gizi : "))
                            simpan = input("Simpan Update (ya/tidak) ? : ").lower()
                            if (simpan == "ya"):                
                                datapasien[updatedataindex]['gizi'] = gizi
                                print("Data berhasil diperbarui.")
                                menampilkandatapasien()
                            elif(simpan == "tidak"):
                                print("Data gagal diupdate")
                        else :
                            print("Kolom tersebut tidak ada di dalam data pasien")
            
                    if(update == 'tidak'):
                        print("Data tidak jadi diupdate")
                       
        elif(dataupdate == "2"):
            tampil = input("Apakah Anda Yakin Ingin Keluar Dari Program Mengupdate Data Pasien (ya/tidak) ? ")
            if(tampil.lower() == "ya"):
                break  # Keluar dari loop untuk kembali ke menu utama
            if(tampil.lower() == "tidak"):
                continue # Balik ke program data pasien
        else :
                print("Pilihan Menu Tidak Valid. Silakan Pilih Menu (1 - 2)")
        

while True:
    menu = input(''' 
======== |Selamat Datang di Rumah Sakit Mursada Jaya| =========
===============================================================       
                      
list menu :
1. menampilkan data pasien rumah sakit
2. menambah daftar data pasien rumah sakit
3. menghapus daftar data pasien rumah sakit
4. mengubah daftar data pasien rumah sakit
5. exit program
                 
Pilih Menu (1 - 5) :  ''')
    
    if(menu == "1"):
        menudata()
    elif(menu == "2"):
        menambahdata()
    elif(menu == "3"):
        menghapusdata()
    elif(menu == "4"):
        updatedata()
    elif(menu == "5"):
        print("Terima kasih sudah datang \nSemoga sehat selalu ")
        break
    else:
        print("Input yang anda masukan tidak ada dalam daftar menu")

