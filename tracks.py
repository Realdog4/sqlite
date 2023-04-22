import sqlite3
from faker import Faker

fake = Faker()

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

try:
    cur.execute("CREATE TABLE Tracks(title, artist, album, duration)")
    for x in range(0, 11):
        title = fake.sentence(nb_words=3)
        artist = fake.name()
        album = fake.sentence(nb_words=2)
        duration = fake.random_int(min=60, max=300)
        cur.execute("""
        INSERT INTO Tracks(title, artist, album, duration) VALUES (?, ?, ?, ?)
    """, (title, artist, album, duration))
except:
    for x in range(0, 11):
        title = fake.sentence(nb_words=3)
        artist = fake.name()
        album = fake.sentence(nb_words=2)
        duration = fake.random_int(min=60, max=300)
        cur.execute("""
        INSERT INTO Tracks(title, artist, album, duration) VALUES (?, ?, ?, ?)
    """, (title, artist, album, duration))
con.commit()
con.close()
