import sqlite3
import database
import os
from user import *
from pembeli import *

class Penjual(database.getDatabase):
    def menuPenjual(self):
        database.getDatabase().deleteScreen()

        daftar_menu = int(input('''============Selamat datang di MENU PENJUAL Stock.id============
        
        1. Tambah Produk
        2. Hapus Produk
        3. Cek Stok Produk
        4. Keluar

===============================================================\n'''))

        if daftar_menu == 1:
            Penjual().addProduk('produk')
        elif daftar_menu == 2:
            Penjual().deleteProduk()
        elif daftar_menu == 3:
            Penjual().cekProduk()
        else:
            User().home()
            
    def addProduk(self, tabel):
        self.tabel = tabel

        namaProduk = str(input("Nama produk: "))
        stok = int(input("Stok Produk: "))
        harga = int(input('Harga Produk: '))

        query = "INSERT INTO {} (namaProduk, stok, harga) VALUES('{}', '{}', '{}');".format(tabel, namaProduk, stok, harga)
        self.cursor.execute(query)
        self.database.commit()

        print("Produk berhasil ditambahkan.")
        cont = input("Apakah ingin kembali ke menu? (yes/ no\n)")
        if cont == 'yes':
            Penjual().menuPenjual()
        else:
            database.getDatabase().deleteScreen()
            Penjual().addProduk('produk')

    def deleteProduk(self):
        hapusProduk = str(input('Masukkan Produk yang akan dihapus : '))

        query = "DELETE FROM produk WHERE namaProduk = '{}'".format(hapusProduk)
        self.cursor.execute(query)
        self.database.commit()

        input("Produk ", hapusProduk, " berhasil dihapus")
        cont = input("Apakah ingin kembali ke menu? (yes/ no)")
        if cont == 'yes':
            Penjual().menuPenjual()
        

    def cekProduk(self):
        cekProduk = str(input("Cek Stok Produk: "))

        query = "SELECT namaProduk from produk where namaProduk = '{}'".format(cekProduk)
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.database.commit()

        try:
            print('Untuk stok ', all_results[0][0], 'masih tersedia')
            input('Klik enter untuk kembali ke Menu Penjual')
            Penjual().menuPenjual()

        except IndexError:
            print("Untuk produk ", cekProduk, "tidak tersedia")
            input('Klik enter untuk kembali ke Menu Penjual')
            Penjual().menuPenjual()

#Penjual().menuPenjual()