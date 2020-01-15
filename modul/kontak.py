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