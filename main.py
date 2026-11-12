
# PROGRAM DATA PASIEN RUMAH SAKIT

pasien = [
    ["Naila", 2],
    ["Viana", 5],
    ["Sahira", 3],
    ["Vina", 7],
    ["Rahmatin", 1],
    ["Fahmi", 4],
    ["Farel", 6],
    ["Rifa", 2],
    ["Zweta", 8],
    ["Nabila", 3]
]

print("=== DATA PASIEN RAWAT INAP ===")

for data in pasien:
    nama = data[0]
    lama_rawat = data[1]

    print("\nNama Pasien :", nama)
    print("Lama Rawat  :", lama_rawat, "hari")

    if lama_rawat >= 7:
        print("Status      : Rawat inap lama")
    elif lama_rawat >= 3:
        print("Status      : Rawat inap sedang")
    elif lama_rawat >= 1:
        print("Status      : Rawat inap singkat")
    else:
        print("Status      : Data tidak valid")

    if lama_rawat > 5:
        print("Keterangan  : Perlu evaluasi dokter")
    else:
        print("Keterangan  : Lama rawat di bawah 6 hari")
