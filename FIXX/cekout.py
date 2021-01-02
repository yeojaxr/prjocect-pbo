import sqlite3
import database
import os
from user import User



class Pembeli(database.getDatabase):
    def menuPembeli(self):
        database.getDatabase().deleteScreen()

        daftar_menu = int(input('''============Selamat datang di MENU PEMBELI Stock.id============
        
        1. Beli Produk
        2. Checkout
        4. Keluar

===============================================================\n'''))

        if daftar_menu == 1:
            Pembeli().selectProduk()
        elif daftar_menu == 2:
            Pembeli().Checkout()
        else:
            User().home()
            


    def selectProduk(self):
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

    def Checkout(self):
        barang = input('Mau beli apa? : ')
        banyak = int(input('Berapa banyak? : '))

        if barang == barang.cekProduk():
            Produk.total = banyak * barang.harga
            print('''\n\tAnda telah membeli {} sebanyak {}
            Jumlah yang harus dibayar adalah {}'''.format(b1.namaProduk,banyak,Produk.total))
        else:
            print ("barang tidak ada")

