import sqlite3 #menghubungkan ke sqlite
import database #menghubungkan ke file database
from penjual import * #menghubungkan ke file penjual

class User(database.getDatabase):

    def home(self):
        database.getDatabase().deleteScreen()
        daftar_menu = int(input('''============Selamat datang di Stock.id============
        
        1. Registrasi
        2. Log in

======================================================\n'''))

        if daftar_menu == 1:
            User().registrasi()
        elif daftar_menu == 2:
            User().login()

        else:
            print("Menu tidak tersedia, silahkan coba lagi!")
            self.home()

    def registrasi(self):
        database.getDatabase().deleteScreen() #untuk menghapus tulisan yang diatasnya
        email = str(input("Email: "))
        username = str(input("Username: "))
        password = str(input("Password: "))

        query = "INSERT INTO dataRegistrasi (email, username, password) VALUES('{}', '{}', '{}');".format(email, username, password)
        self.cursor.execute(query)
        self.database.commit() #mengakhiri dan disimpan permanen

        cont = str(input('Selamat anda berhasil terdaftar!^^, continue to login? (yes/ no)\n'))
        if cont == 'yes':
            User().login()
        elif cont == 'no':
            User().home()
        else:
            User().home()

    def login(self):
        database.getDatabase().deleteScreen()
        username = str(input("Username: "))
        password = str(input("Password: "))

        query = "INSERT INTO dataLogin (username, password) VALUES('{}', '{}');".format(username, password)
        self.cursor.execute(query)
        self.database.commit()

        print ("Login Berhasil, Selamat Datang di Stock.Id", username, "^^")
        user = input("Ketik 'ya' untuk melanjutkan!")
        
        if user == 'ya':
            Penjual().menuPenjual()

User().home()
