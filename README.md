# MODULE 7
## Package & Module
* main.py berisi logika untuk tampilan menu
* kontak.py berisi module untuk menambah, merubah, menghapus, dan mencari data
* imput_data.py berisi module untuk menginput data
* lihat_nilai.py berisi module untuk menampilkan format list data

## coding
### main.py
```python
from view.lihat_data import *

while True:
    c = input("\nA)dd, E)dit, S)earch, D)elete L)ist, Q)uit: ")

    if c.lower() == 'a':
        tambah_data()

    elif c.lower() == 'e':
        ubah_data()

    elif c.lower() == 's':
        cetak_hasil_pencarian()

    elif c.lower() == 'd':
        hapus_data()

    elif c.lower() == 'l':
        cetak_daftar_nilai()

    elif c.lower() == 'q':
        break

    else:
        print("Silahkan pilih menu yang tersedia")
```
### lihat_data.py
```python
from view.lihat_data import *

while True:
    c = input("\nA)dd, E)dit, S)earch, D)elete L)ist, Q)uit: ")

    if c.lower() == 'a':
        tambah_data()

    elif c.lower() == 'e':
        ubah_data()

    elif c.lower() == 's':
        cetak_hasil_pencarian()

    elif c.lower() == 'd':
        hapus_data()

    elif c.lower() == 'l':
        cetak_daftar_nilai()

    elif c.lower() == 'q':
        break

    else:
        print("Silahkan pilih menu yang tersedia")
```
### input_data.py
```python
def input_nama():
    global nama
    nama = input("Masukkan Nama        : ")
    return nama


def input_nim():
    global nim
    nim = input("Masukkan NIM         : ")
    return nim


def input_tugas():
    global tugas
    tugas = int(input("Masukkan Nilai Tugas : "))
    return tugas


def input_uts():
    global uts
    uts = int(input("Masukkan Nilai UTS   : "))
    return uts


def input_uas():
    global uas
    uas = int(input("Masukkan Nilai UAS   : "))
    return uas
```
### kontak.py
```python
from view.input_data import *
kontak = {}
def tambah_data():
    global kontak
    nama = input_nama()
    nim = input_nim()
    uts = input_uts()
    uas = input_uas()
    tugas = input_tugas()
    akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
    kontak[nama] = nim, tugas, uts, uas, akhir
    return kontak


def ubah_data():
    nama = input("Masukkan Nama: ")
    if nama in kontak.keys():
        nim = input_nim()
        uts = input_uts()
        uas = input_uas()
        tugas = input_tugas()
        akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        kontak[nama] = nim, tugas, uts, uas, akhir
    else:
        print("Nama {0} tidak ditemukan".format(nama))


def hapus_data():
    nama = input("Masukkan Nama:  ")
    if nama in kontak.keys():
        del kontak[nama]
    else:
        print("Nama {0} Tidak Ditemukan".format(nama))


def cari_data():
    nama = input("Masukkan Nama        : ")
    if nama in kontak.keys():
        print("=" * 73)
        print("|                             Daftar Mahasiswa                          |")
        print("=" * 73)
        print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("=" * 73)
        print("| {0:15s} | {1:15s} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
              .format(nama, kontak[nama][0], kontak[nama][1], kontak[nama][2], kontak[nama][3], kontak[nama][4]))
        print("=" * 73)
```
#### hasil output
 ![Imgur](https://i.imgur.com/x3EnXec.png)
