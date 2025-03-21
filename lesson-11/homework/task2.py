import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Books')
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
""")

# Insert data
data = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]
cursor.executemany('INSERT INTO Books VALUES (?,?,?,?)', data)

# Update year published
cursor.execute('UPDATE Books SET Year_Published = 1950 WHERE Year_Published=1949')


# Query data
cursor.execute('SELECT Title, Author FROM Books WHERE Genre = "Dystopian"')
dystopian = cursor.fetchall()
print("dystopian charachters: ")
for title, author in dystopian:
    print(f"Title:{title}, Author:{author}")
# Remove data
cursor.execute('DELETE FROM Books WHERE Year_Published < 1950')

# Add new column
cursor.execute('ALTER TABLE Books ADD COLUMN Rating FLOAT')
rating_data =[
    ('To Kill a Mockingbird', 4.8),
    ('1984', 4.7),
    ('The Great Gatsby', 4.5)
]
for title, rating in rating_data:
    cursor.execute('UPDATE Books SET Rating=? WHERE Title=?', (rating, title))
# advanced query
cursor.execute('SELECT * FROM Books ORDER BY Year_Published ASC')
all_characters = cursor.fetchall()
print("_"*40)
for title, author, year_published, rating, genre in all_characters:
    print(f"Title: {title}, Author: {author}, year published: {year_published}, rating: {rating}, Genre: {genre}")
conn.commit()
conn.close()
