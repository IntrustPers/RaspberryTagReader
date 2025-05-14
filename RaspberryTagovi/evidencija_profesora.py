import sqlite3
from datetime import datetime

# Funkcija za kreiranje tablice
def create_table():
    conn = sqlite3.connect('dolazak_odusci_profesora.db')
    cursor = conn.cursor()

    # Kreiraj tablicu ako ne postoji
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dolasci_odlasci (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            profesor_id TEXT NOT NULL,
            ime_profesora TEXT NOT NULL,
            vrijeme_dolaska DATETIME,
            vrijeme_oduska DATETIME
        )
    ''')

    conn.commit()
    conn.close()
    print("Tablica je uspješno stvorena (ako već ne postoji).")


# Funkcija za unos podataka o dolasku
def add_dolazak(profesor_id, ime_profesora):
    conn = sqlite3.connect('dolazak_odusci_profesora.db')
    cursor = conn.cursor()

    vrijeme_dolaska = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
        INSERT INTO dolasci_odlasci (profesor_id, ime_profesora, vrijeme_dolaska)
        VALUES (?, ?, ?)
    ''', (profesor_id, ime_profesora, vrijeme_dolaska))

    conn.commit()
    conn.close()

# Funkcija za unos podataka o odlasku
def add_odlazak(profesor_id):
    conn = sqlite3.connect('dolazak_odusci_profesora.db')
    cursor = conn.cursor()

    vrijeme_odlaska = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
        UPDATE dolasci_odlasci
        SET vrijeme_oduska = ?
        WHERE profesor_id = ? AND vrijeme_oduska IS NULL
    ''', (vrijeme_odlaska, profesor_id))

    conn.commit()
    conn.close()

# Funkcija za dohvat i ispis svih podataka
def show_dolasci_odlasci():
    conn = sqlite3.connect('dolazak_odusci_profesora.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dolasci_odlasci")

    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Profesor ID: {row[1]}, Ime profesora: {row[2]}, "
              f"Vrijeme dolaska: {row[3]}, Vrijeme odlaska: {row[4]}")

    conn.close()


def delete_table():
    # Poveži se na SQLite bazu podataka
    conn = sqlite3.connect('dolazak_odusci_profesora.db')
    cursor = conn.cursor()

    # SQL naredba za brisanje tablice
    cursor.execute('DROP TABLE IF EXISTS dolasci_odlasci')

    # Potvrdi promjene
    conn.commit()

    # Zatvori vezu s bazom podataka
    conn.close()

    print("Tablica 'dolasci_odlasci' je uspješno obrisana!")



#create_table()


add_dolazak('654321', 'Stevo Glavic')


#add_odlazak('123456')



#show_dolasci_odlasci()




