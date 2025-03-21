import sqlite3
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Roster")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster(
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")
# Insert data
data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]
cursor.executemany('INSERT INTO Roster VALUES (?, ?, ?)', data)
# Update Jadzia Dax to Ezri Dax
cursor.execute('UPDATE Roster SET Name = "Ezri Dax" WHERE Name ="Jadzia Dax"')
# Select Name and Age of Bajoran characters (fixing the missing comma)
cursor.execute('SELECT Name, Age FROM Roster WHERE Species = "Bajoran"')
bajorans = cursor.fetchall()
print("Bajoran Characters: ")
for name, age in bajorans:
    print(f"Name: {name}, Age: {age}")
# Delete characters over 100 years
cursor.execute('DELETE FROM Roster WHERE Age > 100')
# Add Rank column and update with values
cursor.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
rank_update = [
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major', 'Kira Nerys')
]
cursor.executemany('UPDATE Roster SET Rank = ? WHERE Name = ?', rank_update)
# Advanced query
cursor.execute('SELECT Name, Age FROM Roster ORDER BY Age DESC')
sorter_characters = cursor.fetchall()
print("characters sorted by Age in descending order", sorter_characters)
conn.commit()
conn.close()
