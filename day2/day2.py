# === DAY 2: IF-ELSE & KALKULATOR SEDERHANA ===

# -----------------------------
# BAGIAN 1: CEK GANJIL / GENAP
# -----------------------------

angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print("Angka tersebut Genap")
else:
    print("Angka tersebut Ganjil")


# -----------------------------
# BAGIAN 2: KALKULATOR SEDERHANA
# -----------------------------

print("\n=== Kalkulator Sederhana ===")

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

operasi = input("Pilih operasi (+ atau -): ")

if operasi == "+":
    hasil = angka1 + angka2
    print("Hasil:", hasil)
elif operasi == "-":
    hasil = angka1 - angka2
    print("Hasil:", hasil)
else:
    print("Operasi tidak valid")
