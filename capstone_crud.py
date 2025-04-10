from tabulate import tabulate
from datetime import datetime

# Data CRUD
data_keluhan = [
    {"id_tiket": "T001", "nama": "Angga", "no_telp": "081234567890", "tanggal": "2025-04-02", "jenis_keluhan": "Gangguan Internet", "status": "Open"},
    {"id_tiket": "T002", "nama": "Karina", "no_telp": "081234567891", "tanggal": "2025-04-03", "jenis_keluhan": "Jaringan Lemot", "status": "In Progress"},
    {"id_tiket": "T003", "nama": "Jasmine", "no_telp": "081234567892", "tanggal": "2025-04-04", "jenis_keluhan": "Tidak Bisa Telepon", "status": "Closed"},
    {"id_tiket": "T004", "nama": "Nabil", "no_telp": "081234567893", "tanggal": "2025-04-05", "jenis_keluhan": "Tagihan Tidak Sesuai", "status": "Open"},
    {"id_tiket": "T005", "nama": "Putri", "no_telp": "081234567894", "tanggal": "2025-04-06", "jenis_keluhan": "Gangguan Sinyal", "status": "In Progress"},
]

def tabel_data(data_list):
    print("\n=== Semua Data Keluhan ===")
    if not data_list:
        print("Tidak ada data yang tersedia.")
    else:
        table = []
        for i in range(len(data_list)):
            data = data_list[i]
            table.append([
                i + 1,
                data["id_tiket"],
                data["nama"],
                data["no_telp"],
                data["tanggal"],
                data["jenis_keluhan"],
                data["status"]
            ])
        print(tabulate(table, headers=["No", "ID Tiket", "Nama", "Telepon", "Tanggal", "Jenis Keluhan", "Status"],
                       tablefmt="fancy_grid", stralign="center", numalign="center"))
        
# CREATE
def create_data():
    while True:
        print("\n=== Tambah Data Keluhan ===")
        print("1. Tambah dengan input ID Tiket")
        print("2. Kembali ke menu utama")
        opsi = input("Pilih opsi (1/2): ")

        if opsi == "1":
            tabel_data(data_keluhan)  

            while True:  
                id_tiket = input("Masukkan ID Tiket (misal: T006): ").upper()
                if any(data["id_tiket"] == id_tiket for data in data_keluhan):
                    print("ID Tiket sudah ada. Gunakan ID lain.")  
                else:
                    break  

            nama = input("Nama: ").title()

            while True:
                no_telp = input("Telepon: ")
                if no_telp.isdigit() and len(no_telp) <= 12:
                    break
                else:
                    print("Nomor telepon maksimal 12 digit angka. Coba lagi.")

            tanggal = datetime.today().strftime("%Y-%m-%d")
            print(f"Tanggal: {tanggal}")

            jenis_keluhan = input("Jenis Keluhan: ").title()
            status = "Open"
            print(f"Status: {status}")

            konfirmasi = input("Simpan data ini? (ya/tidak): ").lower()
            if konfirmasi == "ya":
                keluhan_baru = {
                    "id_tiket": id_tiket,
                    "nama": nama,
                    "no_telp": no_telp,
                    "tanggal": tanggal,
                    "jenis_keluhan": jenis_keluhan,
                    "status": status
                }
                data_keluhan.append(keluhan_baru)
                print("Data keluhan berhasil disimpan.")
                tabel_data(data_keluhan)  
            else:
                print("Data tidak disimpan.")

        elif opsi == "2":
            break
        else:
            print("Opsi tidak valid.")

# READ
def read_data():
    while True:
        print("\n=== Lihat Data Keluhan ===")
        print("1. Tampilkan semua data")
        print("2. Cari berdasarkan ID Tiket")
        print("3. Filter berdasarkan Status Keluhan")
        print("4. Kembali ke menu utama")
        opsi = input("Pilih opsi (1/2/3/4): ")

        if opsi == "1":
            if not data_keluhan:
                print("Belum ada data keluhan yang tersedia.")
                continue
            tabel_data(data_keluhan)

        elif opsi == "2":
            if not data_keluhan:
                print("Belum ada data keluhan yang tersedia.")
                continue

            while True:  
                cari_id = input("Masukkan ID Tiket yang ingin dicari: ").upper()
                hasil = [data for data in data_keluhan if data["id_tiket"] == cari_id]

                if hasil:
                    print("\n=== Data Ditemukan ===")
                    tabel_data(hasil)
                    break  
                else:
                    print("ID Tiket tidak ditemukan. Coba lagi.")

        elif opsi == "3":
            if not data_keluhan:
                print("Belum ada data keluhan yang tersedia.")
                continue
            
            print("\nPilih status keluhan untuk ditampilkan:")
            print("1. Open")
            print("2. In Progress")
            print("3. Closed")
            status_opsi = input("Pilih status (1/2/3): ")

            if status_opsi == "1":
                status_filter = "Open"
            elif status_opsi == "2":
                status_filter = "In Progress"
            elif status_opsi == "3":
                status_filter = "Closed"
            else:
                print("Opsi tidak valid. Kembali ke menu utama.")
                continue

            hasil = [data for data in data_keluhan if data["status"] == status_filter]
            if hasil:
                print(f"\n=== Keluhan dengan Status '{status_filter}' ===")
                tabel_data(hasil)
            else:
                print(f"Tidak ada keluhan dengan status '{status_filter}'.")

        elif opsi == "4":
            print("Kembali ke menu utama.")
            break

        else:
            print("Opsi tidak valid.")

# UPDATE
def update_data():
    while True:
        print("\n=== Ubah Data Keluhan ===")
        
        if not data_keluhan:
            print("Belum ada data keluhan yang tersedia.")
            return

        print("1. Update data berdasarkan ID Tiket")
        print("2. Kembali ke menu utama")
        opsi = input("Pilih opsi (1/2): ")

        if opsi == "1":
            tabel_data(data_keluhan)  

            while True:  
                id_input = input("Masukkan ID Tiket yang ingin diubah (misal: T001): ").upper()

                for i in range(len(data_keluhan)):
                    if data_keluhan[i]["id_tiket"] == id_input:
                        data = data_keluhan[i]
                        print("\n=== Data Keluhan ===")
                        print(tabulate([[data["id_tiket"], data["nama"], data["no_telp"], data["tanggal"], data["jenis_keluhan"], data["status"]]], 
                                       headers=["ID Tiket", "Nama", "Telepon", "Tanggal", "Jenis Keluhan", "Status"],
                                       tablefmt="fancy_grid"))
                        
                        lanjut_update = input("Ingin ubah data? (ya/tidak): ").lower()
                        if lanjut_update == "ya":
                            kolom_valid = ["id_tiket", "nama", "no_telp", "tanggal", "jenis_keluhan", "status"]
                            
                            kolom_input = input(f"Masukkan nama kolom yang ingin diubah (id_tiket/nama/no_telp/tanggal/jenis_keluhan/status): ").lower()

                            if kolom_input not in kolom_valid:
                                print("Nama kolom tidak valid.\n")
                                continue

                            nilai_baru = input(f"Masukkan nilai baru untuk {kolom_input}: ")

                            if kolom_input == "no_telp":
                                while not (nilai_baru.isdigit() and len(nilai_baru) <= 12):
                                    print("Nomor telepon maksimal 12 angka.")
                                    nilai_baru = input(f"Masukkan nomor telepon baru untuk {kolom_input}: ")

                            konfirmasi = input("Simpan perubahan data ini? (ya/tidak): ").lower()
                            if konfirmasi == "ya":
                                data_keluhan[i][kolom_input] = nilai_baru
                                print(f"{kolom_input} berhasil diperbarui.\n")
                                
                                tabel_data(data_keluhan)

                                break  
                        break
                else:
                    print("Data dengan ID Tiket tersebut tidak ditemukan. Coba lagi.\n")
                break  
        elif opsi == "2":
            break
        else:
            print("Opsi tidak valid.\n")

# DELETE
def delete_data():
    while True:
        print("\n=== Hapus Data Keluhan ===")

        if not data_keluhan:
            print("Tidak ada data keluhan yang bisa dihapus.")
            return

        print("1. Hapus berdasarkan ID Tiket")
        print("2. Kembali ke menu utama")
        opsi = input("Pilih opsi (1/2): ")

        if opsi == "1":
            while True:
                tabel_data(data_keluhan)

                id_tiket_input = input("Masukkan ID Tiket yang ingin dihapus (misal: T001): ").upper()

                for i in range(len(data_keluhan)):  
                    data = data_keluhan[i]
                    if data["id_tiket"] == id_tiket_input:
                        
                        print("\nData yang akan dihapus:")
                        print(tabulate([[ 
                            data["id_tiket"],
                            data["nama"],
                            data["no_telp"],
                            data["tanggal"],
                            data["jenis_keluhan"],
                            data["status"]
                        ]], headers=["ID Tiket", "Nama", "Telepon", "Tanggal", "Jenis Keluhan", "Status"],
                            tablefmt="fancy_grid"))

                        konfirmasi = input("Yakin ingin menghapus data ini? (ya/tidak): ").lower()
                        if konfirmasi == "ya":
                            del data_keluhan[i]  
                            print("Data berhasil dihapus.\n")

                            tabel_data(data_keluhan)

                            lagi = input("Apakah Anda ingin menghapus data lagi? (ya/tidak): ").lower()
                            if lagi == "ya":
                                break  
                            else:
                                return 

                        else:
                            print("Penghapusan dibatalkan.\n")
                            return  

        elif opsi == "2":
            break 
        else:
            print("Opsi tidak valid. Silakan pilih 1 atau 2.\n")

# MENU CRUD
def menu_utama():
    while True:
        pilihan = input('''
            Sistem CRUD Keluhan Customer Telekomunikasi

            1. Tambah Keluhan
            2. Tampilkan Data Keluhan
            3. Ubah Data Keluhan
            4. Hapus Data Keluhan
            5. Keluar
            Pilih menu (1-5):
            ''')

        if pilihan == "1":
            create_data()
        elif pilihan == "2":
            read_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            delete_data()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

menu_utama()
