Username = "Grace Vies Angel"
Password = "2409116005"

statusLogin = "logout"

print("Login Sistem")
while True:
    if statusLogin == "logout":
        batasLogin = 2
        print("Silahkan login terlebih dahulu yaa..")
        while True:
            print("Batas login tersisa", batasLogin, "kali\n")
            loginUsername = input("> Username: ")
            loginPassword = input("> Password: ")

            if loginUsername == Username and loginPassword == Password:
                print("Login berhasil!")
                statusLogin = "login"
                break

            else:
                print("Username atau Password salah")
                batasLogin = batasLogin - 1
                if batasLogin == 0:
                    print("Batas login sudah habis, otomatis keluar dari sistem!")
                    statusLogin = "batasHabis"
                    break

    elif statusLogin == "login":
        batasLogin = 2
        print("\nSistem Menghitung Gaji Karyawan Berdasarkan Jam Kerja dan Tarif Kerja")
        print("Menu:")
        print("1. Hitung Gaji Karyawan")
        print("2. Keluar")
        menu = int(input("> Pilih Menu: "))

        if menu == 1:
            while True:
                print("\nMenghitung Gaji Karyawan")
                print("Contoh:")
                print("Jam Kerja: 120")
                print("Tarif Kerja: 12000\n")
                jamKerja = int(input("> Jam Kerja: "))
                tarifKerja = int(input("> Tarif Kerja: "))

                if jamKerja >= 160:
                    rumusGaji = jamKerja * tarifKerja
                    rumusBonus = rumusGaji * 0.1
                    rumusTotalGaji = rumusGaji + rumusBonus
                    print("Gaji tersebut adalah Rp."+str(rumusGaji))
                    print("Bonus sebesar 10% yaitu Rp."+str(rumusBonus))
                    print("Total gaji adalah Rp."+str(rumusTotalGaji))
                else:
                    rumusTotalGaji = jamKerja * tarifKerja
                    print("Total gaji adalah Rp." + str(rumusTotalGaji))

                konfirmasi = input("Apakah ingin menghitung gaji lagi? (y/n): ")
                if konfirmasi == 'y':
                    continue
                elif konfirmasi == 'n':
                    break
                else:
                    print("Pilihan tidak tersedia!\n")
                    break

        elif menu == 2:
            print("Keluar!")
            break
        else:
            print("Pilihan tidak tersedia!")
    elif statusLogin == "batasHabis":
        break
