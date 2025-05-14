📚 Raspberry Pi RFID Prijava Dolaska za Profesore
Ovaj projekt koristi Raspberry Pi i RFID čitač za evidenciju dolazaka profesora u školu. Svaki profesor ima svoj RFID tag, a kad ga prisloni na čitač, uređaj automatski očita kod i zabilježi vrijeme dolaska u bazu podataka.

🔧 Funkcionalnosti:
📟 Očitavanje RFID tagova pomoću čitača povezanog na Raspberry Pi

🕒 Automatsko bilježenje datuma i vremena dolaska

🧑‍🏫 Svaki tag je povezan s točno određenim profesorom

💾 Spremanje podataka u SQLite (ili drugi) database

🖥️ Mogućnost prikaza podataka putem jednostavnog web sučelja (opcionalno)

🧰 Tehnologije:
Raspberry Pi (Python)

RFID čitač (npr. RC522)

SQLite baza podataka

Python knjižnice: gpiozero, pysqlite3, datetime

🎯 Cilj:
Olakšati administraciju i vođenje evidencije dolazaka profesora bez potrebe za ručnim upisivanjem ili potpisivanjem.
