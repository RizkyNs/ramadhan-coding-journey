# === DAY 3: LOOP ===

# -----------------------------
# BAGIAN 1: TABEL PERKALIAN
# -----------------------------

print("=== Tabel Perkalian ===")

angka = int(input("Masukkan angka: "))

for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")


# -----------------------------
# BAGIAN 2: GAME TEBAK ANGKA
# -----------------------------

print("\n=== Game Tebak Angka ===")

import random

angka_rahasia = random.randint(1, 10)
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print("Benar! 🎉")
