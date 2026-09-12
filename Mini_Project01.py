cuaca_sejuk = (23, 24, 25)
cuaca_hangat = (26, 27, 28, 29)
cuaca_panas = (30, 31, 32, 33, 34)
cuaca_terik = (35, 36, 37, 38, 39, 40)

semua_suhu = []
cuaca = []
hapus_suhu = []

while True:
    suhu = input("Masukkan suhu (°C): ")

    if suhu.lower() == 'selesai':
        print("Input suhu selesai.")
        break

    suhu_masuk = int(suhu)

    if suhu_masuk in cuaca_sejuk:
        print ("Cuaca sejuk")
        semua_suhu.append(int(suhu))
        cuaca.append("Cuaca sejuk")
    elif suhu_masuk <= 22:
        print ("Cuaca dingin")
        semua_suhu.append(int(suhu))
        cuaca.append("Cuaca dingin")   
    elif suhu_masuk in cuaca_hangat:
        print ("Cuaca hangat")
        semua_suhu.append(int(suhu))
        cuaca.append("Cuaca hangat")
    elif suhu_masuk in cuaca_panas:
        print ("Cuaca panas")
        semua_suhu.append(int(suhu))
        cuaca.append("Cuaca panas")
    elif suhu_masuk in cuaca_terik:
        print ("Cuaca panas terik")
        semua_suhu.append(int(suhu))
        cuaca.append("Cuaca panas terik")
    else:
        print ("Suhu ekstrem")
        semua_suhu.append(int(suhu))
        cuaca.append("Suhu ekstrem")
        continue

hapus_suhu = input("Apakah Anda salah menginput suhu?: ")
if hapus_suhu.lower() == 'ya':
    suhu_hapus = int(input("Masukkan suhu yang ingin dihapus: "))
    if suhu_hapus in semua_suhu:
        index_hapus = semua_suhu.index(suhu_hapus)
        semua_suhu.remove(suhu_hapus)
        cuaca.pop(index_hapus)
        print(f"Suhu {suhu_hapus} telah dihapus.")

suhu_masuk = input("Apakah Anda ingin menambahkan suhu?: ")
if suhu_masuk.lower() == 'ya':
    while True:
        suhu = input("Masukkan suhu (°C): ")

        if suhu.lower() == 'selesai':
            print("Input suhu selesai.")
            break

        suhu_masuk = int(suhu)

        if suhu_masuk in cuaca_sejuk:
            print ("Cuaca sejuk")
            semua_suhu.append(int(suhu))
            cuaca.append("Cuaca sejuk")
        elif suhu_masuk in cuaca_hangat:
            print ("Cuaca hangat")
            semua_suhu.append(int(suhu))
            cuaca.append("Cuaca hangat")
        elif suhu_masuk in cuaca_panas:
            print ("Cuaca panas")
            semua_suhu.append(int(suhu))
            cuaca.append("Cuaca panas")
        elif suhu_masuk in cuaca_terik:
            print ("Cuaca panas terik")
            semua_suhu.append(int(suhu))
            cuaca.append("Cuaca panas terik")
        else:
            print ("Suhu ekstrem")
            semua_suhu.append(int(suhu))
            cuaca.append("Suhu ekstrem")
            continue

print(f"\nTotal suhu yang diinput: {len(semua_suhu)}")
print(f"Daftar suhu yang diinput: {semua_suhu}")
print(f"Daftar cuaca: {cuaca}")