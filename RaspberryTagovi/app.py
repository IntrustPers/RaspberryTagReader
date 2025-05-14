from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Funkcija za dohvat podataka iz SQLite baze
def get_dolasci_odlasci():
    conn = sqlite3.connect('dolazak_odusci_profesora.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dolasci_odlasci")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Ruta za prikaz podataka na web stranici
@app.route('/')
def index():
    # Dohvati sve podatke
    dolasci_odlasci = get_dolasci_odlasci()
    return render_template('index.html', dolasci_odlasci=dolasci_odlasci)

if __name__ == '__main__':
    app.run(debug=True)
