
def main():
    masuk = []
    keluar = []

    choice = 0

    while choice != 6:
        print("*** PROGRAM PENCATAT KEUANGAN ***")
        print("1) Setor uang")
        print("2) Tarik uang")
        print("3) List uang masuk")
        print("4) List uang keluar")
        print("5) Selisih uang masuk dan keluar")
        print("6) Keluar aplikasi")
        print("*********************************")

        choice = int(input("Pilih menu: "))

        match choice:
            case 1:
                print("*********************************")
                uang = int(input("Masukkan jumlah uang masuk: "))
                masuk.append(uang)
                print("Berhasil mencatat uang masuk")
                input()
            case 2:
                uang = int(input("Masukkan jumlah uang keluar: "))
                keluar.append(uang)
                print("Berhasil mencatat uang keluar")
                input()
            case 3:
                print("List uang masuk: ", masuk)
                print("Total: ", sum(masuk))
                input()
            case 4:
                print("List uang keluar: ", keluar)
                print("Total: ", sum(keluar))
                input()
            case 5:
                print("Total uang masuk: ", sum(masuk))
                print("Total uang keluar: ", sum(keluar))
                print("Selisih uang masuk dan keluar (Net Profit): ",
                      sum(masuk)-sum(keluar))
                input()
            case 6:
                print("Tekan enter untuk keluar dari program...")
                input()
                return
            case _:
                print("Jangan ngaco...")
                input()


main()
