import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE Roster(
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Insert the data
cursor.executemany('''
INSERT INTO Roster(Name, Species, Age)
VALUES (?, ?, ?)''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# Update the name
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# Select and display Bajoran entries
cursor.execute('''
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
''')

results = cursor.fetchall()
for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")

conn.close()


import sqlalchemy as sa
import pandas as pd

# Connection string (modify based on your authentication method)
connection_string = 'mssql+pyodbc://XTREMELITE-PC/NewDatabase?driver=SQL+Server'

# Create engine and connect to the database
engine = sa.create_engine(connection_string)
con = engine.connect()

# Step 1: Update the Name of Jadzia Dax to Ezri Dax
con.execute(sa.text('''
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
'''))

# Step 2: Fetch and display the Name and Age of everyone classified as Bajoran
df_bajoran = pd.read_sql(sa.text('''
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran'
'''), con=con)

# Display the result
print(df_bajoran)

# Close the connection
con.close()
