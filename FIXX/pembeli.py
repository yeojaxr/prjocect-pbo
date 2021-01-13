import sqlite3
import database
import os
from user import *
from penjual import *

class Pembeli(database.getDatabase):
    belanja = []
    harga = []

    def menuPembeli(self):
        database.getDatabase().deleteScreen()

        daftar_menu = int(input('''============Selamat datang di MENU PEMBELI Stock.id============
        
        1. Beli Produk
        2. Checkout
        4. Keluar

===============================================================\n'''))

        if daftar_menu == 1:
            Pembeli().cariProduk()
        elif daftar_menu == 2:
            beli = str(input("Beli produk terlebih dahulu!\n (yes/no)"))
            if beli == 'yes':
                Pembeli().menuPembeli()
            else:
                User().home()
        else:
            User().home()
    
    def cariProduk(self):
        database.getDatabase().deleteScreen()

        cari = input("Produk yang dicari: ")
        query = "SELECT namaProduk, stok, harga from produk where namaProduk = '{}'".format(cari)

        self.cursor.execute(query)
        barang = self.cursor.fetchall()
        self.database.commit()

        try: #dilakukan try dan except biar kalo ada error ngeprint yang except
            print([0][0]," dengan harga ", barang[0][1] ," Tersedia ditoko kami")
            tambah = input("Apakah  ingin ditambahkan dikeranjang ? \nyes/no")
            if tambah == 'yes':
                Pembeli.belanja.append(barang[0])
                Pembeli.harga.append(barang[0][1])
                mauTambah = input("Tambah Produk? \n yes/no")
                if mauTambah == "yes":
                    Pembeli().cariProduk()
                elif mauTambah == "no":
                    Pembeli().menuPembeli()

            elif tambah == 'no':
                Pembeli().menuPembeli()

        except IndexError:
            print("Maaf, Barang yang anda cari tidak tersedia di toko kami")
            Pembeli().menuPembeli()

Pembeli().menuPembeli()